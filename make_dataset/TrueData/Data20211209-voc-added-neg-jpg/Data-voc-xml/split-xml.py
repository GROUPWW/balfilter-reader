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
xmls = os.listdir("Annotations")
for xml in xmls:
    if xml.split(".")[0] in train:
        print("copy Annotations/"+xml+" Annotations-split-by-train-val/train/"+xml)
        shutil.copy("Annotations/"+xml,"Annotations-split-by-train-val/train/"+xml)

    if xml.split(".")[0] in val:
        shutil.copy("Annotations/"+xml,"Annotations-split-by-train-val/val/"+xml)