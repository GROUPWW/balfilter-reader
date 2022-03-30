import sys
sys.path.append('./yolov5')
sys.path.append('./CenterNet/src')
from cut_and_detect import cut_and_detect_mini

import os
import glob


listDir = "big_img_in/"

l_neg = ['2_1004509.jpg', '2_1004510.jpg', '2_1004516.jpg',
         "3_1005256.jpg"]

l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg', '2_1004515.jpg',
         '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
         "3_1005250.jpg", "3_1005251.jpg", "3_1005253.jpg"]


# imgList = os.listdir(listDir)

imgList = l_neg+l_pos
imgList = ['2_1004521.jpg']

# imgList = glob.glob(r'big_img_in/tmp/black/*.jpg')
print(imgList)
import time
timeList = []
for ele in imgList :
    ele = listDir + ele
    if ele.split(".")[-1] == "jpg":
        t0 = time.time()
        cut_and_detect_mini(ele)
        psTime = time.time() - t0
        print(psTime)
        timeList.append(psTime)
import numpy as np
print(timeList)
print(np.mean(timeList))
