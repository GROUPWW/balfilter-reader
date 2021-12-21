with open("ImageSets/Main/train.txt", "r") as f:  # 打开文件
    train = f.readlines()  # 读取文件
    train = list(map(lambda x:x[:-1],train))
    print(train)

with open("ImageSets/Main/val.txt", "r") as f:  # 打开文件
    val = f.readlines()  # 读取文件
    val = list(map(lambda x:x[:-1],val))
    print(val)

import os
import shutil
xmls = os.listdir("JPEGImages")
for xml in xmls:
    if xml.split(".")[0] in train:
        shutil.copy("JPEGImages/"+xml,"JPEGImages-split-by-train-val/train/"+xml)

    elif xml.split(".")[0] in val:
        shutil.copy("JPEGImages/"+xml,"JPEGImages-split-by-train-val/val/"+xml)

    else:
        shutil.copy("JPEGImages/" + xml, "JPEGImages-split-by-train-val/neg/" + xml)