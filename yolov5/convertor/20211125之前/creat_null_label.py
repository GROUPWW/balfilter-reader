import os
l = os.listdir('./null_pic/')
import shutil

b = os.getcwd() + '/labels/train2017/'


for ele in l:
    s=ele.split('.')
    if s[-1] =='png':
        #print(b+s[0]+'.txt')
        #print('./null_pic/' + ele)
        open(b+s[0]+'txt', "w")
        shutil.copy('./null_pic/'+ele, "images/train2017/")