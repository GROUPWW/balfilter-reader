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

    l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg','2_1004515.jpg',
             '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
             "3_1005250.jpg", "3_1005251.jpg", "3_1005253.jpg"]

    l_neg_trans = ['2_1004509_trans.jpg', '2_1004510_trans.jpg', '2_1004516_trans.jpg',
             "3_1005256_trans.jpg"]

    l_pos_trans = ['2_1004518_trans.jpg', '2_1004519_trans.jpg', '2_1004521_trans.jpg', '2_1004522_trans.jpg',
             '1003989_trans.jpg', '1003993_trans.jpg', '1003994_trans.jpg', '1003995_trans.jpg', '1003997_trans.jpg', '1003998_trans.jpg',
             "3_1005250_trans.jpg", "3_1005251_trans.jpg", "3_1005253_trans.jpg"]

    # imgList = os.listdir(listDir)

    imgList = l_neg + l_pos+     l_neg_trans + l_pos_trans


    imgList = ["zjx1.jpg","zjx001.jpg"]
    for ele in imgList:
        print(ele)



    # imgList = ['2_1004518.jpg',  '2_1004522.jpg',
    #          '1003989.jpg',  '1003998.jpg',
    #          "3_1005253.jpg"]

    # imgList = ['2_1004521.jpg']

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
    neg_list_std, pos_list_std = [],[]



    for ele in l_neg:
        ele = listDir + ele
        if ele.split(".")[-1] == "jpg":

            avg,num,std = cut_and_detect_mini(ele)
            neg_list_avg.append(avg)
            neg_list_num.append(num)
            neg_list_std.append(std)



    for ele in l_pos:
        ele = listDir + ele
        if ele.split(".")[-1] == "jpg":

            avg,num,std = cut_and_detect_mini(ele)
            pos_list_avg.append(avg)
            pos_list_num.append(num)
            pos_list_std.append(std)

    import numpy as np
    neg_list_std = np.array(neg_list_std)
    pos_list_std = np.array(pos_list_std)

#################################################################
    print("下方输出std")
    point3_neg = neg_list_std[:, 0]
    point6_neg = neg_list_std[:, 1]
    point9_neg = neg_list_std[:, 2]
    point3_pos = pos_list_std[:, 0]
    point6_pos = pos_list_std[:, 1]
    point9_pos = pos_list_std[:, 2]
    # print(point9_pos)

    print("\n\n\n\n")
    for ele in np.concatenate((point3_neg, point3_pos)):
        print(ele)

    print("###############################")

    for ele in np.concatenate((point6_neg, point6_pos)):
        print(ele)

    print("###############################")

    for ele in np.concatenate((point9_neg, point9_pos)):
        print(ele)

    print("###############################")
   #########################################







    import numpy as np
    return np.array(neg_list_num), np.array(pos_list_num), np.array(neg_list_avg), np.array(pos_list_avg)