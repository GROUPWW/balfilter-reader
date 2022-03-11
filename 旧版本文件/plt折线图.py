import matplotlib.pyplot as plt
# fig, axes = plt.subplots(1, 1, figsize=(8, 4))
# 折线图
plt.figure(figsize=(10,6))

x = [15,25.6,31.2,46.3,79.5,128,198]
y = [0.876,0.904,0.916,0.913,0.91,0.906,0.832]
x2 = [14.4,41.9,91.6,170]
y2 = [0.902,0.914,0.906,0.921]
x3 = [264]
y3 = [0.852]
z = ["D0","D1","D2","D3","D4","D5","D6"]
z2 = ["s","m","l","x"]
z3 = ["CenterNet"]

plt.plot(x, y, color='r',marker="*",ms=10,label = "EfficientDet")
plt.plot(x2, y2, color='g',marker="*",ms=10,label = "Yolov5")
plt.plot(x3, y3, color='b',marker="*",ms=10,label = "CenterNet")
# 设置最小刻度间隔
# axes.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
# axes.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
# 画网格线
# axes.grid(which='minor', c='lightgrey')
# 设置x、y轴标签
plt.ylabel("mAP@0.5")
plt.xlabel("Model Size")
# 设置y轴的刻度
# axes.set_yticks([70, 75, 80, 85, 90, 95])
plt.yticks([0.82, 0.85, 0.88, 0.91, 0.93])
# 对每个数据点加标注
for x_, y_ ,z_ in zip(x, y,z):
    plt.text(x_, y_+0.001, z_, ha='left', va='bottom',color = "r",size=12)
for x_, y_,z_ in zip(x2, y2,z2):
    plt.text(x_-3, y_+0.001, z_, ha='left', va='bottom',color ="g",size=15)
for x_, y_,z_ in zip(x3, y3,z3):
    plt.text(x_-25, y_+0.001, z_, ha='left', va='bottom',color ="b",size=15)
# 展示图片
plt.legend()
plt.show()
