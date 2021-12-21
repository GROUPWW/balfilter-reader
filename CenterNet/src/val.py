import os
import json
import cv2
import numpy as np
import time
import torch

from opts_and_utils import all_opts
opts=all_opts()


from coco_ctdet import COCO

from test import CtdetDetector

def test(load_modelStr = opts.load_model):

    dataset = COCO('val')
    detector = CtdetDetector(load_modelStr)

    results = {}
    num_iters = len(dataset)

    for ind in range(num_iters):
        img_id = dataset.images[ind]
        img_info = dataset.coco.loadImgs(ids=[img_id])[0]
        img_path = os.path.join(dataset.img_dir, img_info['file_name'])

        ret = detector.run(img_path)

        results[img_id] = ret

    # print(results)
    return dataset.run_eval(results,".")


if __name__ == '__main__':
    test()
