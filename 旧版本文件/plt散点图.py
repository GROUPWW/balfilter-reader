import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import FuncFormatter

plt.xlim(-1,18)
plt.ylim(-0.1,1.4)


def to_percent(temp, position):
    return str(temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))



# 10个点
# x1 = np.arange(4)
# x2 = np.arange(4,18)
# y1 = [0.20,0.09,0.10,0.12]
# y2 = [0.08,0.37,0.53,0.15,0.04,0.07,0.23,0.63,0.18,1.16,0.10,0.48,1.30,0.25]

x1 = [1,6,11,16]
x2 = [0,2,3,4,5,7,8,9,10,12,13,14,15,17]
y1 = [0.20,0.09,0.10,0.12]
y2 = [0.08,0.37,0.53,0.15,0.04,0.07,0.23,0.63,0.18,1.16,0.10,0.48,1.30,0.25]

# z = y1 + y2
# z.sort() #[0.04, 0.07, 0.08, 0.09, 0.1, 0.1, 0.12, 0.15, 0.18, 0.2, 0.23, 0.25, 0.37, 0.48, 0.53, 0.63, 1.16, 1.3]

# x1 = [3,4,6,9]
# x2 = [0,1,2,5,7,8,10,11,12,13,14,15,16,17]
# y1 = [0.09,0.10,0.12,0.20]
# y2 = [0.04, 0.07, 0.08, 0.1,0.15, 0.18,0.23, 0.25, 0.37, 0.48, 0.53, 0.63, 1.16, 1.3]
plt.ylabel("Proportion of suspicious image blocks")

plt.scatter(x1, y1,c = "b",label = "neg")
plt.scatter(x2, y2,c = "r",label = "pos")
plt.xticks([])
plt.yticks([0,0.11,0.175,0.24,0.4,0.6,0.8,1.0,1.2,1.4])
plt.hlines(0.11, -1, 19, colors = "b",linestyles = "dashed",label="neg median")
plt.hlines(0.24, -1, 19, colors = "r",linestyles = "dashed",label="pos median")
plt.hlines(0.175, -1, 19, colors = "black",linestyles = "dashed",label="threshold")
plt.legend()
plt.show()

