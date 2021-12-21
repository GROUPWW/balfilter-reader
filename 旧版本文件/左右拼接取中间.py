import cv2
import numpy as np
import pandas as pd

import datetime
data_time_str=str(datetime.datetime.now())
time_id=data_time_str.split(' ')[0]+'-'+data_time_str.split(' ')[1].split(':')[0]+'-'+data_time_str.split(' ')[1].split(':')[1]
img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')
image = np.concatenate([img1, img2], axis=1)
image_cut=image[:,100:356]
cv2.imwrite(time_id+'.png',image_cut)