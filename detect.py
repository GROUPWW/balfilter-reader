import numpy as np
import time
from pathlib import Path
import os
from cut_and_detect import cut_and_detect_mini
import sys

def fast_detect():

    listDir = "big_img_in/"

    imgList = [
        '001.jpg',
        '002.jpg',
        '003.jpg',
        '004.jpg',
        '005.jpg',
        '006.jpg',
        '007.jpg',
        '008.jpg',
        '009.jpg',
        '010.jpg',
        '011.jpg',
        '012.jpg',
        '013.jpg',
        '014.jpg',
        '015.jpg',
        '016.jpg',
        '017.jpg',
        '018.jpg',
        '019.jpg',
        '020.jpg',
        '021.jpg',
        '022.jpg',
        '023.jpg',
        '024.jpg',
        '025.jpg',
        '026.jpg',
        '027.jpg',
        '028.jpg',
        '029.jpg',
        '030.jpg',
        '031.jpg',
        '032.jpg',
        '033.jpg',
        '034.jpg',
        '035.jpg',
        '036.jpg',
        '037.jpg',
        '038.jpg',
        '039.jpg',
        '040.jpg',
        '041.jpg'
    ]

    # imgList = []
    # for root, ds, fs in os.walk(listDir):
    #     for f in fs:
    #         print(root, f)
    #         fullname = os.path.join(root + '/', f)
    #         if Path(fullname).suffix == '.jpg':
    #             imgList.append(fullname)

    timeList = []
    for ele in imgList:
        ele = listDir + ele
        if ele.split(".")[-1] != "jpg":
            print(ele, 'not jpg')
            continue
        print('detecting', ele)
        t0 = time.time()
        cut_and_detect_mini(ele)
        psTime = time.time() - t0
        print('infer time=', psTime)
        timeList.append(psTime)

    print('all infer time=', timeList)
    print('mean infer time=', np.mean(timeList))


if __name__ == "__main__":
    fast_detect()
