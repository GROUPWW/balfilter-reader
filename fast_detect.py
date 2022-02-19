import sys
sys.path.append('./yolov5')
sys.path.append('./CenterNet/src')
from cut_and_detect import cut_and_detect_mini

import os
import glob


listDir = "big_img_in/"
imgList = os.listdir(listDir)
# imgList = glob.glob(r'big_img_in/tmp/black/*.jpg')
print(imgList)

for ele in imgList :
    ele = listDir + ele
    if ele.split(".")[-1] == "jpg":
        cut_and_detect_mini(ele)
