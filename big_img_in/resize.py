import cv2
import os

for ele in os.listdir():
    if ele.split(".")[-1] == "jpg":
        img = cv2.imread(ele)
        img = cv2.resize(img,(1024,1024))
        cv2.imwrite("resize/"+ele,img)