import os
for ele in os.listdir("train2017"):
    os.rename("train2017/"+ele,"train2017/"+ele.split(".")[0]+".jpg")

for ele in os.listdir("val2017"):
    os.rename("val2017/"+ele,"val2017/"+ele.split(".")[0]+".jpg")