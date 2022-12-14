from PIL import Image
Image.MAX_IMAGE_PIXELS = None

#直接转int可能会越界，所以使用取整，舍去右下部分边缘
import math
import numpy as np
import os
import shutil
import cv2
import torch
from torchvision import transforms
import getopt

import config

import sys
sys.path.append('./yolov5')
#yolov5
from models.experimental import attempt_load
from utils.general import  non_max_suppression
from utils.torch_utils import select_device

# from PyQt5.QtWidgets import QApplication

sys.path.append('./CenterNet/src')
#centernet
from msra_resnet import get_pose_net
from opts_and_utils_for_pyqt import _gather_feat, _transpose_and_gather_feat,all_opts
from CenterNet.src.test import _nms,_topk,ctdet_decode,load_model

from util.mysql import in_mysql
from util.filter import doFilter

from mysq_heatmap import createHeatmap

#属于centernet的，暂时放这
class CtdetDetector():
    def __init__(self,database,opts):
        # print('\n正在创建模型...')

        self.database = database

        self.opts = opts
        self.model = get_pose_net(opts.res_layers, opts.classes, train_or_test='test')

        # 官方代码中加载模型的函数，应该是保存的模型引入了额外的一些参数
        self.model = load_model(self.model, opts.load_model)
        # 一种常见用法,在这会出错
        # pretrained_dict = torch.load(opt_load_model)
        # model_dict = self.model.state_dict()
        # pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}
        # model_dict.update(pretrained_dict)
        # self.model.load_state_dict(model_dict)

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = self.model.to(self.device)

        # model.eval() ：不启用BatchNormalization和Dropout
        self.model.eval()
        self.pause = True

    def process(self, images):
        with torch.no_grad():
            output = self.model(images)[-1]
            hm = output['hm'].sigmoid_()
            wh = output['wh']
            reg = output['reg']

            # 通过最后三层得到[bbox、置信度、类别]
            dets = ctdet_decode(hm, wh, reg, self.opts.max_object)

        return dets

    def run(self,image_copy,path,nxn,window):
        temp_image = ((image_copy / 255. - self.opts.mean) / self.opts.std).astype(np.float32)
        temp_image = temp_image.transpose(2, 0, 1)[np.newaxis, :]
        image = torch.from_numpy(temp_image)

        image = image.to(self.device)

        dets = self.process(image)
        if torch.cuda.is_available():
            dets = dets.detach().cpu().numpy()

        max_det_4 = 0
        for det in np.array(dets[-1]):
            if det[4] > 0.3:
                det[4] = round(det[4], 3)

                max_det_4 = max(max_det_4, det[4])
                det[0], det[1], det[2], det[3] = 4 * det[0], 4 * det[1], 4 * det[2], 4 * det[3]

                # 0.6以上红色
                if det[4] >= 0.6:
                    color = (0, 0, 255)
                else:
                    color = (0, 255, 255)

                cv2.rectangle(image_copy, (det[0], det[1]), (det[2], det[3]), color, 2)
                cv2.putText(image_copy, str(det[4]), (det[0], det[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        # print(type(image_copy))
        window.pic_name_dic[nxn+'.jpg'] = str(max_det_4)
        cv2.imwrite(path+nxn+'.jpg', image_copy)
        self.database.write_in_database(nxn, str(max_det_4), 'CenterNet')


def plot_one_box_liuzheng(x, img_copy, label=None):
    if label >= 0.3:

        label = str(label)
        c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
        cv2.rectangle(img_copy, c1, c2,  (0,0,255), 2)
        if label:
            cv2.putText(img_copy, label, (c1[0], c1[1] - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)





# 用于直接使用
def cut_and_detect_mini(big_img_path,chosen_model='yolov5'):

    case_id = big_img_path.split('/')[-1].split('.')[0]
    database = in_mysql(case_id)
    out = config.ROOT_PATH + '/image_output/' + case_id + '/'

    if os.path.exists(out):
        shutil.rmtree(out)  # delete output folder
    os.makedirs(out)  # make new output folder


    if chosen_model=='yolov5':
        yolov5_opt = {'weights': [config.ROOT_PATH + '/yolov5/weights/infer.pt'], 'img_size': 256,
                      'conf_thres': 0.01, 'iou_thres': 0.5, 'device': '', 'classes': None, 'agnostic_nms': False,
                      'augment': False}
        img_size = yolov5_opt['img_size']
        loader = transforms.Compose([transforms.ToTensor()])

        with torch.no_grad():
            weights = yolov5_opt['weights']
            device = select_device(yolov5_opt['device'])
            print('device={}'.format(device))

            half = device.type != 'cpu'  # half precision only supported on CUDA  #半精度浮点数（fp16，Half-precision floating-point）

            # Load model
            model = attempt_load(weights, map_location=device)  # load FP32 model
            if half:
                model.half()  # to FP16
                print('model half')
    else:
        opts = all_opts()
        img_size = opts.img_size
        detector = CtdetDetector(database,opts)

    # Run inference
    image = Image.open(big_img_path)
    width, height = image.size
    item_width =math.floor(img_size)
    item_height=math.floor(img_size)
    the_shorter=min(width,height)
    the_shorter_num = int(the_shorter/img_size)
    # print('短边长度为： ', the_shorter_num)


    import time
    timeList = []

    for i in range(0,the_shorter_num):
        for j in range(0,the_shorter_num):
            box = (j*item_width,i* item_height,(j+1)*item_width,(i+1)*item_height)
            temp=image.crop(box)
            # PIL竟然直接就是0-1之间,不用除以255

            img_copy = np.array(temp).astype('uint8')
            img_copy = cv2.cvtColor(np.array(img_copy), cv2.COLOR_RGB2BGR)
            #img_copy=np.array(temp)[:, :, (2, 1, 0)]

            doFilterRes = doFilter(img_copy)
            #TODO(wny)
            if doFilterRes !=1 :
                # database.write_in_database(str(i) + "x" + str(j), "0", 'yolov5', doFilterRes)
                pass

            else:



                if chosen_model == 'yolov5':

                    # t0 = time.time()

                    img = loader(temp)
                    print('img {} {}'.format(i, j))

                    # img = img[[2, 1, 0]].unsqueeze(0)
                    if img.ndimension() == 3:
                        img = img.unsqueeze(0)

                    # 不行，这里报错，换保存吧
                    # img = np.float32(img)
                    # cv2.imshow("hello", img)
                    # cv2.waitKey()
                    # print(img)

                    img = img.to(device)
                    img = img.half() if half else img.float()  # uint8 to fp16/32
                    # img /= 255.0  # 0 - 255 to 0.0 - 1.0



                    # Inference
                    pred = model(img, augment=yolov5_opt['augment'])[0]


                    # Apply NMS
                    pred = non_max_suppression(pred, yolov5_opt['conf_thres'], yolov5_opt['iou_thres'], classes=yolov5_opt['classes'], agnostic=yolov5_opt['agnostic_nms'])

                    # psTime = time.time() - t0
                    # timeList.append(psTime)


                    # Process detections

                    for det in pred:  # detections per image
                        if det is not None and len(det):
                            # Write results
                            for *xyxy, conf, cls in reversed(det):
                                label = round(float(conf),3)
                                # print("啊")

                                plot_one_box_liuzheng(xyxy, img_copy, label=label)


                                database.write_in_database(str(i)+"x"+str(j), str(label), 'yolov5',1)

            cv2.imwrite(out + str(i) + "x" + str(j) + ".jpg", img_copy)
            # torch.cuda.empty_cache()
            # gc.collect()
            # print(torch.cuda.memory_stats())
            # print(torch.cuda.memory_summary())

    # timeList = timeList[1:]
    # print("##################################")
    # for ele in timeList:
    #     print(ele)
    #
    #
    # print("###################################")


    database.db.commit()
    database.db.close()
    createHeatmap(case_id+".jpg")


if __name__ == "__main__":
    inputfile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:",["input-file="])
    except getopt.GetoptError:
        print('cut_and_detect.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('cut_and_detect.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--input-file"):
            inputfile = arg

    cut_and_detect_mini(inputfile)
