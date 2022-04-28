# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

n_groups = 18

# new
class1 = [105.86021089553833, 87.89690279960632, 141.05293655395508, 74.49554395675659, 119.69012761116028, 129.21043705940247, 107.42768621444702, 123.32591724395752, 126.21786665916443, 146.14937043190002, 143.96780371665955, 140.02471542358398, 175.80521965026855, 140.82756757736206, 152.73157739639282, 105.59659337997437, 116.16135144233704, 77.78008079528809]
# 123
print(np.mean(class1))

# class1 = [107.03137230873108, 90.55175924301147, 146.03998565673828, 80.00892305374146, 100.07995104789734, 111.01265478134155, 73.88073992729187, 110.35244011878967, 90.30904817581177, 146.85333824157715, 117.95156764984131, 125.79521203041077, 185.5463297367096, 141.00152611732483, 148.74208617210388, 110.86102604866028, 105.8961615562439, 78.59804344177246]
class1 = [int(c) for c in class1]
#
# def to_percent(temp, position=None):
#     return str(int(temp*100)) + '%'
# plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))


# plt.yticks([0,0.11,0.175,0.24,0.4,0.6,0.8,1.0,1.2,1.4])
# plt.ylim(0,0.9)
index = np.arange(n_groups) 
bar_width = 0.35

opacity = 0.6 #不透明度
# error_config = {'ecolor': '0.3'}

plt.bar(index, class1, bar_width,
    alpha=opacity, color='r',
    label='BALFilter Reader')





for x,y in zip(index,class1):
    plt.text(x,y+0.003,y,ha='center',va='bottom')





# ax.set_ylabel('时间')
# ax.set_title('加速情况')
plt.xticks([])
plt.ylabel("大视场图像的推理时间")
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