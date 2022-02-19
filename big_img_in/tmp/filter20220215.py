import cv2
import numpy as np
import glob
import os

# img_list = glob.glob(r'*.jpg')  # 大小写无关
# print(len(img_list))
# print(img_list)


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result






def cntBluePurple(imgDir):
    img = cv2.imread(imgDir)
    # print(imgDir)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    area_mul_255=img.shape[0]*img.shape[1]*255

    # 饱和度从43改成30，含灰紫色
    lowerPurpl = np.array([100, 30, 46])
    upperPurpl = np.array([155,255,255])
    mask=cv2.inRange(HSV,lowerPurpl,upperPurpl)
    return  mask.sum() / area_mul_255


def cntRed(imgDir):
    img = cv2.imread(imgDir)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    area_mul_255=img.shape[0]*img.shape[1]*255

    # 饱和度从43改成30，含灰红色
    lower_red_1 = np.array([0, 30, 46])
    upper_red_1 = np.array([10, 255, 255])
    lower_red_2 = np.array([156, 30, 46])
    upper_red_2 = np.array([180, 255, 255])
    mask=cv2.inRange(HSV,lower_red_1,upper_red_1)
    cnt1 = mask.sum() / area_mul_255
    mask = cv2.inRange(HSV, lower_red_2, upper_red_2)
    cnt2 = mask.sum() / area_mul_255
    return cnt1 + cnt2


def cntBlack(imgDir):
    img = cv2.imread(imgDir)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    area_mul_255=img.shape[0]*img.shape[1]*255
    lowerBlack = np.array([0, 0, 0])
    upperBlack = np.array([180,255,46])
    mask=cv2.inRange(HSV,lowerBlack,upperBlack)
    return  mask.sum() / area_mul_255


def cntSobel(imgDir):
    img = cv2.imread(imgDir)
    img =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    s = 0
    sobel1 = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=3)
    sobel2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    dst = np.sqrt(sobel1*sobel1 + sobel2*sobel2)
    s += (dst>500).sum()
    return  s / multiplyList(img.shape)






def cntAll(dir):
    Dir_cntBluePurple,Dir_cntRed,Dir_cntBlack,Dir_cntSobel = [],[],[],[]
    for ele in dir:
        if ele.split(".")[-1] == "ini":
            continue
        Dir_cntBluePurple.append(cntBluePurple(ele))
        Dir_cntRed.append(cntRed(ele))
        Dir_cntBlack.append(cntBlack(ele))
        Dir_cntSobel.append(cntSobel(ele))
    Dir_cntBluePurple.sort()
    Dir_cntRed.sort()
    Dir_cntBlack.sort()
    Dir_cntSobel.sort()
    return [Dir_cntBluePurple,Dir_cntRed,Dir_cntBlack,Dir_cntSobel]


def findThres():
    blackDir = ["black/"+ele for ele in os.listdir("black")]
    blue_purpleDir = ["blue_purple/"+ele for ele in os.listdir("blue_purple")]
    focus_on_filterDir = ["focus_on_filter/"+ele for ele in os.listdir("focus_on_filter")]
    no_cellDir = ["no_cell/"+ele for ele in os.listdir("no_cell")]
    normalDir = ["normal/"+ele for ele in os.listdir("normal")]
    redDir = ["red/"+ele for ele in os.listdir("red")]

    result_blackDir = cntAll(blackDir)
    result_blue_purpleDir = cntAll(blue_purpleDir)
    result_focus_on_filterDir = cntAll(focus_on_filterDir)
    result_no_cellDir= cntAll(no_cellDir)
    result_normalDir = cntAll(normalDir )
    result_redDir= cntAll(redDir)

    print("正常图像的黑色占比")
    print([round(ele,4) for ele in result_normalDir[2]])
    print("异常黑色图像的黑色占比")
    print([round(ele,4) for ele in result_blackDir[2]])
    print("\n")

    print("无细胞图像的蓝紫色占比")
    print([round(ele,4) for ele in result_no_cellDir[0]])
    print("正常图像的蓝紫色占比")
    print([round(ele,4) for ele in result_normalDir[0]])
    print("异常蓝紫色图像的蓝紫色占比")
    print([round(ele,4) for ele in result_blue_purpleDir[0]])
    print("\n")

    print("无细胞图像的红色占比")
    print([round(ele,4) for ele in result_no_cellDir[1]])
    print("正常图像的红色占比")
    print([round(ele,4) for ele in result_normalDir[1]])
    print("异常红色图像的红色占比")
    print([round(ele,4) for ele in result_redDir[1]])
    print("\n")

    print("正常图像的高边缘信息占比")
    print([round(ele,4) for ele in result_normalDir[3]])
    print("对焦在滤膜上图像的高边缘信息占比")
    print([round(ele,4) for ele in result_focus_on_filterDir[3]])
    print("\n")


    from numpy import mean
    print("#################################################下方是平均数#################################################")
    print("正常图像的黑色占比")
    print(round(mean(result_normalDir[2]),4))
    print("异常黑色图像的黑色占比")
    print(round(mean(result_blackDir[2]),4))
    print("\n")

    print("无细胞图像的蓝紫色占比")
    print(round(mean(result_no_cellDir[0]),4))
    print("正常图像的蓝紫色占比")
    print(round(mean(result_normalDir[0]),4))
    print("异常蓝紫色图像的蓝紫色占比")
    print(round(mean(result_blue_purpleDir[0]),4))
    print("\n")

    print("无细胞图像的红色占比")
    print(round(mean(result_no_cellDir[1]),4))
    print("正常图像的红色占比")
    print(round(mean(result_normalDir[1]),4))
    print("异常红色图像的红色占比")
    print(round(mean(result_redDir[1]),4))
    print("\n")

    print("正常图像的高边缘信息占比")
    print(round(mean(result_normalDir[3]),4))
    print("对焦在滤膜上图像的高边缘信息占比")
    print(round(mean(result_focus_on_filterDir[3]),4))
    print("\n")

    import math
    thresBlack = round(math.sqrt(mean(result_normalDir[2]) * mean(result_blackDir[2])),4)

    thresMinBlue_purple = round(math.sqrt(mean(result_no_cellDir[0]) * mean(result_normalDir[0])),4)
    thresMaxBlue_purple = round(math.sqrt(mean(result_normalDir[0]) * mean(result_blue_purpleDir[0])),4)

    thresMinRed = round(math.sqrt(mean(result_no_cellDir[1]) * mean(result_normalDir[1])),4)
    thresMaxRed = round(math.sqrt(mean(result_normalDir[1]) * mean(result_redDir[1])),4)

    thresSobel = round(math.sqrt(mean(result_normalDir[3])* mean(result_focus_on_filterDir[3])),4)
    print(thresBlack,thresMinBlue_purple,thresMaxBlue_purple,thresMinRed,thresMaxRed,thresSobel)


findThres() #0.0295 0.0314 0.3095 0.0311 0.383 0.0084




# def doFilter:



    # print(img_name + "蓝紫色占比" + str(round(mask.sum() / area_mul_255, 4)))


    # if mask.sum() / area_mul_255 >  #待修改
    #
    #
    # # 饱和度从43改成30，含灰红色
    # lower_red_1 = np.array([0, 30, 46])
    # upper_red_1 = np.array([10, 255, 255])
    # lower_red_2 = np.array([156, 30, 46])
    # upper_red_2 = np.array([180, 255, 255])
    #
    # mask=cv2.inRange(HSV,lower_red_1,upper_red_1)
    # cnt1 = mask.sum() / area_mul_255
    #
    # mask = cv2.inRange(HSV, lower_red_2, upper_red_2)
    # cnt2 = mask.sum() / area_mul_255
    # # cv2.imshow('tmp',Cyan_mask)
    # # cv2.waitKey()
    #
    # print(img_name + "                  红色占比" + str(round(cnt1 + cnt2, 4)))
    #
    #
    # lowerBlack = np.array([0, 0, 0])
    # upperBlack = np.array([180,255,46])
    # mask=cv2.inRange(HSV,lowerBlack,upperBlack)
    # print(img_name + "                                      黑色占比" + str(round(mask.sum() / area_mul_255, 4)))


    # lower = np.array([0, 0, 221])
    # upper = np.array([180,30,255])
    # mask=cv2.inRange(HSV,lower,upper)
    # print(img_name + "                                                          白色占比" + str(round(mask.sum() / area_mul_255, 4)))




#图片越模糊，其边缘就越少,所以用拉普拉斯-方差的清晰度方法可能会和预期想的方法相反
    # # 处理空间不够,拆成四块统计
    # s = 0
    # img_t = img[:img.shape[0]//2,:img.shape[1]//2]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst * (dst <= 50)).sum() / (dst<=50).sum()
    #
    # img_t = img[:img.shape[0]//2,img.shape[1]//2:]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst * (dst <= 50)).sum() / (dst<=50).sum()
    #
    # img_t = img[img.shape[0]//2:,:img.shape[1]//2]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst * (dst <= 50)).sum() / (dst<=50).sum()
    #
    # img_t = img[img.shape[0]//2:,img.shape[1]//2:]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst * (dst <= 50)).sum() / (dst<=50).sum()

#     gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize = 3)
#     dst = cv2.convertScaleAbs(gray_lap)
#     cv2.imshow(img_name, dst)
#     cv2.imshow(img_name+" 1", dst*(dst>254))
#     cv2.imshow(img_name+" 2", dst*(dst<=254))
#     print(img_name + "的平均信息量为" ,(dst>254).sum() / (dst.shape[0]*dst.shape[1]*dst.shape[2]))
# cv2.waitKey(0)



#     sobel = cv2.Sobel(img,cv2.CV_64F, 1, 1, ksize=3)
#     dst = cv2.convertScaleAbs(sobel)
#     cv2.imshow(img_name, dst)
#     cv2.imshow(img_name+" 1", dst*(dst>150))
#     cv2.imshow(img_name+" 2", dst*(dst<=150))
#     print(img_name + "的平均信息量为" ,(dst>150).sum() / (dst.shape[0]*dst.shape[1]))
# cv2.waitKey(0)


    #
    # img =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s = 0
    # # img = img[img.shape[0]//4:img.shape[0]*3//4,img.shape[1]//4:img.shape[1]*3//4]
    #
    #
    #
    #
    # # sobel = cv2.Sobel(img,cv2.CV_64F, 1, 1, ksize=3)
    # # dst = cv2.convertScaleAbs(sobel)
    #
    # sobel1 = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=3)
    # sobel2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    # dst = np.sqrt(sobel1*sobel1 + sobel2*sobel2)
    #
    # s += (dst>500).sum()
    # print(img_name + "的平均信息量为", round(s / multiplyList(img.shape), 4))



    # img_t = img[:img.shape[0]//2,:img.shape[1]//2]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst>150).sum()
    #
    # img_t = img[:img.shape[0]//2,img.shape[1]//2:]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst>150).sum()
    #
    # img_t = img[img.shape[0]//2:,:img.shape[1]//2]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst>150).sum()
    #
    # img_t = img[img.shape[0]//2:,img.shape[1]//2:]
    # sobel = cv2.Sobel(img_t,cv2.CV_64F, 1, 1, ksize=3)
    # dst = cv2.convertScaleAbs(sobel)
    # s += (dst>150).sum()






    # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    # img = cv2.dilate(img, kernel, iterations=2)
    # HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #
    # lowerWhite = np.array([0, 0, 221])
    # upperWhite = np.array([180,30,255])
    # mask=cv2.inRange(HSV,lowerWhite,upperWhite)
    # maskInvDived255 = (255 - mask) // 255
    # # print(maskInvDived255)
    # maskInvDived255 = cv2.cvtColor(maskInvDived255, cv2.COLOR_GRAY2BGR)
    #
    # dst = dst * maskInvDived255

    # cv2.imwrite("res/3_" + img_name, maskInvDived255*255)
    #
    # #print(dst.shape)

    # mask = mask // 255
    # mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # dst = dst * mask

    # print(img_name + "的平均拉普拉斯边缘信息量为" + str(round(cnt.sum() / (img.shape[0]*img.shape[1]*3), 4)))

    # cv2.imwrite("res/4_"+img_name,dst)
    # cv2.imshow(img_name, dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


#     sobel1 = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=3)
#     sobel2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
#     sobel = np.sqrt(sobel1*sobel1 + sobel2*sobel2)
#     dst = sobel
#     # dst = cv2.convertScaleAbs(sobel)
#     dst = (dst > 500) * dst
#     print(img_name + "的sobel边缘信息量为" + str(round(dst.sum() / area_mul_255, 4)))
#
# #     cv2.imshow(img_name, dst)
# # cv2.waitKey(0)




#
# file = open('result.txt','w')
# file.write("\n\n\n")
# print("\n")
# for j in not_red_outlist:
#     print(j)
#     file.write(j+"\n")
#
# file.write("\n\n\n")
# print("\n")
# for j in lap:
#     print(j)
#     file.write(j+"\n")
#
# file.write("\n\n\n")
# print("\n")
# for j in sobel_list:
#     print(j)
#     file.write(j+"\n")
#
# file.close();