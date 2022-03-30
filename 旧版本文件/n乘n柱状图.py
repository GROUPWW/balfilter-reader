# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from matplotlib.ticker import FuncFormatter
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

n_groups = 3

class1 = (0.75,0.64,0.67)


def to_percent(temp, position=None):
    return str(int(temp*100)) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))


# plt.yticks([0,0.11,0.175,0.24,0.4,0.6,0.8,1.0,1.2,1.4])
plt.ylim(0,0.9)
index = np.arange(n_groups) 
bar_width = 0.35

opacity = 0.3 #不透明度
# error_config = {'ecolor': '0.3'}

plt.bar(index, class1, bar_width,
    alpha=opacity, color='b',
    label='BALFilter Reader')





for x,y in zip(index,class1):
    plt.text(x,y+0.003,to_percent(y),ha='center',va='bottom')





# ax.set_ylabel('时间')
# ax.set_title('加速情况')
plt.xticks(index,['Specificity', 'Sensitivity','Accuracy'])
plt.ylabel("Ratio")
# plt.xticks()
# plt.xticklabels(('specificity', 'sensitivity','accuracy'))
# plt.legend() #右上角显示的图像

# fig.tight_layout() #自动调整子图参数，使之填充整个图像区域
plt.show()














#
#
# # -*- coding: utf-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator
# from collections import namedtuple
# from matplotlib.ticker import FuncFormatter
# # plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#
# n_groups = 3
#
# class1 = (0.75,0.64,0.67)
# class2 = (0.25,0.64,0.56)
#
# def to_percent(temp, position=None):
#     return str(int(temp*100)) + '%'
# plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
# plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
#
# # plt.yticks([0,0.11,0.175,0.24,0.4,0.6,0.8,1.0,1.2,1.4])
# plt.ylim(0,0.9)
# index = np.arange(n_groups)
# bar_width = 0.35
#
# opacity = 1 #不透明度
# # error_config = {'ecolor': '0.3'}
#
# plt.bar(index, class1, bar_width,
#     alpha=opacity, color='b',
#     label='BALFilter Reader')
#
# plt.bar(index + bar_width, class2, bar_width,
#     alpha=opacity, color='r',
#     label='Manual Inspection')
#
#
#
# for x,y in zip(index,class1):
#     plt.text(x,y+0.003,to_percent(y),ha='center',va='bottom')
#
#
#
# for x,z in zip(index,class2):
#     plt.text(x+bar_width ,z+0.003,to_percent(z),ha='center',va='bottom')
#
# # ax.set_ylabel('时间')
# # ax.set_title('加速情况')
# plt.xticks(index + bar_width / 2,['Specificity', 'Sensitivity','Accuracy'])
# plt.ylabel("Ratio")
# # plt.xticks()
# # plt.xticklabels(('specificity', 'sensitivity','accuracy'))
# plt.legend() #右上角显示的图像
#
# # fig.tight_layout() #自动调整子图参数，使之填充整个图像区域
# plt.show()