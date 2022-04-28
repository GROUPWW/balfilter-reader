# 导入需要的包
import numpy as np
import cv2
import gc


if __name__ == '__main__':

  listDir = "big_img_in/"

  # l_neg = ['2_1004509.jpg', '2_1004510.jpg', '2_1004516.jpg',
  #   #          "3_1005256.jpg"]

  l_neg = ['2_1004510.jpg', '2_1004516.jpg',
           "3_1005256.jpg"]

  #
  l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg', '2_1004515.jpg',
           '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
           "3_1005250.jpg", "3_1005251.jpg", "3_1005253.jpg"]



  # imgList = os.listdir(listDir)

  imgList = l_neg + l_pos

  for ele in imgList:
    ip = listDir + ele

    target = cv2.imread(ip)

    target = target.astype("float32")

    # 实则BGR,之前统计的结果
    lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc = 214.08909683735374, 40.23375111464699, 203.7828368003964, 50.66645962771195, 216.84143803944804, 39.31514752104765
    (l, a, b) = cv2.split(target)
    # l, _, _ = cv2.split(target)
    #
    # 啊


    (lMeanTar, lStdTar) = (l.mean(), l.std())
    (aMeanTar, aStdTar) = (a.mean(), a.std())
    (bMeanTar, bStdTar) = (b.mean(), b.std())
    l -= lMeanTar
    a -= aMeanTar
    b -= bMeanTar
    # 按标准差缩放(scale_rate = 目标图像标准差/源图像标准差)
    l = (lStdTar / lStdSrc) * l
    a = (aStdTar / aStdSrc) * a
    b = (bStdTar / bStdSrc) * b
    # 加入源图像对应通道的均值
    l += lMeanSrc
    a += aMeanSrc
    b += bMeanSrc
    # 如果像素强度超出范围，则将像素强度剪裁为[0, 255]范围
    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)
    # 将通道合并在一起并转换回BGR颜色空间，确保确保使用 8 位无符号整数数据类型


    target = cv2.merge([l, a, b])

    del l,a,b
    print(gc.collect())

    cv2.imwrite(ele, target)

    del target
    print(gc.collect())
