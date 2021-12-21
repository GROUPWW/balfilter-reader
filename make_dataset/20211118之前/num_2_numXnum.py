import os
import shutil

l = os.listdir('all_img')
for ele in l:
    ele1 = int(ele.split('.')[0])-1
    x = ele1//98
    y = ele1%98
    new = str(x)+'x'+str(y)+'.png'
    shutil.copy('all_img/'+ele,'res/'+new)