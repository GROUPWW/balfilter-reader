# pycocotools windows按这个链接就好
# http://www.mamicode.com/info-detail-2660241.html
import pycocotools.coco as coco
import numpy as np
import os
import torch.utils.data as data
import cv2
from opts_and_utils import gaussian_radius, draw_umich_gaussian
import math
from opts_and_utils import all_opts
opts=all_opts()

from pycocotools.cocoeval import COCOeval
import json

class COCO(data.Dataset):

  #split 是 trian或者test
  def __init__(self, split):
    super().__init__()
    self.mean=opts.mean
    self.std=opts.std
    self.num_classes = opts.classes
    self.img_dir = opts.data_dir+'\\'+split+'2017'
    self.annot_path = os.path.join(opts.data_dir, 'annotations','instances_{}2017.json').format(split)

    print(self.annot_path)

    self.max_objs = 50

    #用于检测时显示，由于我的代码里只简单使用方框框出，所以暂时没用到
    self.class_name = ['cancer_cell',]
    self._valid_ids = [0]


    #例如{0：0}
    self.cat_ids = {v: i for i, v in enumerate(self._valid_ids)}
    self.split = split
    self.coco = coco.COCO(self.annot_path)

    #例如，val时返回图片号[8151, 8474, 8882, 8958, 9142, 9173, 9176, 9452, 9462, 7488, 7684, 7873, 7878, 7988, 7993, 8011, 8027, 6549, 6716]
    self.images = self.coco.getImgIds()

    print('Loaded {} {} samples\n'.format(split, len(self.images)))

  #必须配置这个
  def __len__(self):
    return len(self.images)

  def _coco_box_to_bbox(self, box):
    bbox = np.array([box[0], box[1], box[0] + box[2], box[1] + box[3]],
                    dtype=np.float32)
    return bbox


  # #    def __getitem__(self, index):
  #       ＃1。从文件中读取一个数据（例如，使用numpy.fromfile，PIL.Image.open）。
  #        ＃2。预处理数据（例如torchvision.Transform）。
  #        ＃3。返回数据对（例如图像和标签）。
  def __getitem__(self, index):
    img_id = self.images[index]
    file_name = self.coco.loadImgs(ids=[img_id])[0]['file_name']
    img_path = os.path.join(self.img_dir, file_name)
    ann_ids = self.coco.getAnnIds(imgIds=[img_id])
    anns = self.coco.loadAnns(ids=ann_ids)

    #print(anns)
    #     例如可以从标签里得到：
    # [{'area': 1600, 'iscrowd': 0, 'image_id': 4677, 'bbox': [139,211, 40, 40],
    # 'category_id': 0, 'id': 60,'ignore': 0, 'segmentation': []}]
    #其实后面只用到了bbox和category_id

    num_objs = min(len(anns), self.max_objs)

    # print(img_path)

    img = cv2.imread(img_path)

    inp = (img.astype(np.float32) / 255.)
    inp = (inp - self.mean) / self.std
    inp = inp.transpose(2, 0, 1)

    output_h = opts.img_size // 4
    output_w = opts.img_size // 4
    num_classes = self.num_classes

    hm = np.zeros((num_classes, output_h, output_w), dtype=np.float32)
    wh = np.zeros((self.max_objs, 2), dtype=np.float32)
    reg = np.zeros((self.max_objs, 2), dtype=np.float32)

    ind = np.zeros((self.max_objs), dtype=np.int64)
    reg_mask = np.zeros((self.max_objs), dtype=np.uint8)
    cat_spec_wh = np.zeros((self.max_objs, num_classes * 2), dtype=np.float32)
    cat_spec_mask = np.zeros((self.max_objs, num_classes * 2), dtype=np.uint8)

    gt_det = []
    for k in range(num_objs):
      ann = anns[k]
      bbox = self._coco_box_to_bbox(ann['bbox'])

      # 当dict取值时，如果key在dict的key()中不存在，就会报错KeyError: 0
      cls_id = int(self.cat_ids[ann['category_id']])

      bbox[:2] = bbox[:2]/4
      bbox[2:] =bbox[2:]/4

      #缩小4倍后bbox的h和w
      h, w = bbox[3] - bbox[1], bbox[2] - bbox[0]
      if h > 0 and w > 0:


        #math.ceil函数返回一个大于或等于 x 的的最小整数
        #当h=w=10.0时，得到的int(radius)是2，半径还整挺小
        radius = gaussian_radius((math.ceil(h), math.ceil(w)))
        radius = max(0, int(radius))

        #计算出了center点
        ct = np.array([(bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2], dtype=np.float32)

        #这玩意就是取小于它的最大整数，而非四舍五入
        ct_int = ct.astype(np.int32)
        #！！！！！！！因为下方画高斯图必须用int型的中心坐标画，所以引入了reg，而ct之所以不是int，就是下采样导致的


        #生成方形的高斯图，例如： #！！！！
        # [[0.00315111 0.02732372 0.05613476 0.02732372 0.00315111]
        #  [0.02732372 0.23692776 0.48675226 0.23692776 0.02732372]
        #  [0.05613476 0.48675226 1. 0.48675226 0.05613476]
        #  [0.02732372 0.23692776 0.48675226 0.23692776 0.02732372]
        #  [0.00315111 0.02732372 0.05613476 0.02732372 0.00315111]]
        draw_umich_gaussian(hm[cls_id], ct_int, radius)

        #调试程序，暂时保留
        #hm = (hm[0]*255).astype(np.uint8)
        #cv2.imwrite('hm.jpg',hm)
        #cv2.waitKey()

        wh[k] = 1. * w, 1. * h
        ind[k] = ct_int[1] * output_w + ct_int[0]

        reg[k] = ct - ct_int
        reg_mask[k] = 1

        cat_spec_wh[k, cls_id * 2: cls_id * 2 + 2] = wh[k]
        cat_spec_mask[k, cls_id * 2: cls_id * 2 + 2] = 1

        gt_det.append([ct[0] - w / 2, ct[1] - h / 2,
                       ct[0] + w / 2, ct[1] + h / 2, 1, cls_id])

    ret = {'input': inp, 'hm': hm, 'reg_mask': reg_mask, 'ind': ind, 'wh': wh,'reg': reg}

    return ret

  def save_results(self, results, save_dir):
    json.dump(self.convert_eval_format(results),
              open('{}/results.json'.format(save_dir), 'w'))

  def run_eval(self, results, save_dir):
    # result_json = os.path.join(save_dir, "results.json")
    # detections  = self.convert_eval_format(results)
    # json.dump(detections, open(result_json, "w"))
    self.save_results(results, save_dir)
    coco_dets = self.coco.loadRes('{}/results.json'.format(save_dir))

    # coco_dets = self.coco.loadRes("../data/coco/annotations/instances_val2017.json")
    # print(coco_dets)
    coco_eval = COCOeval(self.coco, coco_dets, "bbox")
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return coco_eval.stats[:2]

  def convert_eval_format(self, all_bboxes):
    # print(all_bboxes)


    # import pdb; pdb.set_trace()
    detections = []
    for image_id in all_bboxes:
      for cls_ind in all_bboxes[image_id]:
        category_id = self._valid_ids[cls_ind - 1]
        for bbox in all_bboxes[image_id][cls_ind]:
          bbox[2] -= bbox[0]
          bbox[3] -= bbox[1]
          score = bbox[4]
          bbox_out  = list(map(lambda x:float("{:.2f}".format(x)), 4*bbox[0:4]))

          detection = {
              "image_id": int(image_id),
              "category_id": int(category_id),
              "bbox": bbox_out,
              "score": float("{:.2f}".format(score))
          }

          # print(detection)


          detections.append(detection)
    return detections
