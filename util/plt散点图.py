import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import FuncFormatter
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.xlim(-1,8.8)
plt.ylim(0,2.1)


def to_percent(temp, position):
    return str(temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))


x1 = [1.8,2,1.8,2]
x2 = [5.8,6,5.8,6,5.8,6,5.8,6,5.8,6,5.8,6,5.8,6]
y1 = [0.27,0.15,0.25,0.13]
y2 = [0.32,0.57,2.04,0.05,0.19,0.14,1.46,0.9,0.32,1.32,0.2,0.72,1.47,0.52]


print(np.mean(y1))
print(np.mean(y2))


# 10个点
# x1 = np.arange(4)
# x2 = np.arange(4,18)
# y1 = [0.20,0.09,0.10,0.12]
# y2 = [0.08,0.37,0.53,0.15,0.04,0.07,0.23,0.63,0.18,1.16,0.10,0.48,1.30,0.25]



# x1 = [1,6,11,16]
# x2 = [0,2,3,4,5,7,8,9,10,12,13,14,15,17]
# y1 = [0.20,0.09,0.10,0.12]
# y2 = [0.08,0.37,0.53,0.15,0.04,0.07,0.23,0.63,0.18,1.16,0.10,0.48,1.30,0.25]




'''
# z = y1 + y2
# z.sort() #[0.04, 0.07, 0.08, 0.09, 0.1, 0.1, 0.12, 0.15, 0.18, 0.2, 0.23, 0.25, 0.37, 0.48, 0.53, 0.63, 1.16, 1.3]
'''






# x1 = [3,4,6,9]
# x2 = [0,1,2,5,7,8,10,11,12,13,14,15,16,17]
# y1 = [0.09,0.10,0.12,0.20]
# y2 = [0.04, 0.07, 0.08, 0.1,0.15, 0.18,0.23, 0.25, 0.37, 0.48, 0.53, 0.63, 1.16, 1.3]
plt.ylabel("含癌细胞图像块的占比")

plt.scatter(x1, y1,c = "b",label = "阴性")
plt.scatter(x2, y2,c = "r",label = "阳性")
plt.xticks([1.9,5.9],['阴性', '阳性'])
plt.yticks([0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2])
# plt.hlines(0.11, 1, 2.8, colors = "b",linestyles = "dashed",label="阴性中值")
# plt.hlines(0.24, 5, 6.8, colors = "r",linestyles = "dashed",label="阳性中值")
plt.hlines(0.2, 1, 2.8, colors = "b",linestyles = "dashed",label="阴性均值")
plt.hlines(0.73, 5, 6.8, colors = "r",linestyles = "dashed",label="阳性均值")
# plt.hlines(0.175, -1, 8.8, colors = "black",linestyles = "dashed",label="诊断分界线")
plt.legend()
plt.show()

