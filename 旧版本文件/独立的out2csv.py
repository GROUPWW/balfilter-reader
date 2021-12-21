import os
import pandas as pd
val = []
for ele in os.listdir('./cut_and_detect_out')[::-1]:
    name = os.path.splitext(ele)[0]
    conf = name.split('-')[0]
    xy = '第'+name.split('-')[1].split('x')[0]+'行 第'+name.split('-')[1].split('x')[1]+'列'
    val.append([name,conf,xy,'123456','98'])
df = pd.DataFrame(val,columns=['name','图像块可疑度','图像块在原图的位置','病例编号','图片总行数'])
df.to_csv('fakecatalog.csv',index=None)