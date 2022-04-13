import sys
sys.path.append('./yolov5')
sys.path.append('./CenterNet/src')
from cut_and_detect import cut_and_detect_mini


import os
import glob

def fast_detect():

    listDir = "big_img_in/"

    l_neg = ['2_1004509.jpg', '2_1004510.jpg', '2_1004516.jpg',
             "3_1005256.jpg"]

    l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg',
             '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
             "3_1005250.jpg", "3_1005251.jpg", "3_1005253.jpg"]


    # imgList = os.listdir(listDir)

    imgList = l_neg+l_pos
    # imgList = ['2_1004518.jpg',  '2_1004522.jpg',
    #          '1003989.jpg',  '1003998.jpg',
    #          "3_1005253.jpg"]

    imgList = ['2_1004521.jpg']

    # imgList = glob.glob(r'big_img_in/tmp/black/*.jpg')

    import time
    timeList = []
    res = []



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
    return res

if __name__=="__main__":
    fast_detect()

def fast_detect_cnt():

    listDir = "big_img_in/"

    l_neg = ['2_1004509.jpg', '2_1004510.jpg', '2_1004516.jpg',
             "3_1005256.jpg"]

    l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg',
             '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
             "3_1005250.jpg", "3_1005251.jpg", "3_1005253.jpg"]

    # l_neg = ['2_1004509.jpg', '2_1004510.jpg']
    # l_pos = ['2_1004521.jpg', '2_1004519.jpg']



    neg_list_num, pos_list_num = [],[]
    neg_list_avg, pos_list_avg = [],[]



    for ele in l_neg:
        ele = listDir + ele
        if ele.split(".")[-1] == "jpg":

            avg,num = cut_and_detect_mini(ele)
            neg_list_avg.append(avg)
            neg_list_num.append(num)



    for ele in l_pos:
        ele = listDir + ele
        if ele.split(".")[-1] == "jpg":

            avg,num = cut_and_detect_mini(ele)
            pos_list_avg.append(avg)
            pos_list_num.append(num)


    import numpy as np
    return np.array(neg_list_num), np.array(pos_list_num), np.array(neg_list_avg), np.array(pos_list_avg)