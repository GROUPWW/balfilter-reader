import os
import shutil
l = os.listdir('xml')

out = '和xml标签数量对应的图像/'
if os.path.exists(out):
    shutil.rmtree(out)  # delete output folder
os.makedirs(out)  # make new output folder

for ele in l:
    name = '包含已经看过的不确定的图像_无需重复看不确定的/'+ele.split('.')[0]+'.png'
    shutil.copy(name, out)

