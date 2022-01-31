import cv2
import numpy as np
import glob

img_list = glob.glob(r'*.jpg')  # 大小写无关
print(len(img_list))
print(img_list)


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

for img_name in img_list:
    img = cv2.imread(img_name)


    #)
    area_mul_255=img.shape[0]*img.shape[1]*255


    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # print(img.shape[:2])



    # 饱和度从43改成30，含灰紫色
    lowerPurpl = np.array([100, 30, 46])
    upperPurpl = np.array([155,255,255])
    mask=cv2.inRange(HSV,lowerPurpl,upperPurpl)
    print(img_name + "蓝紫色占比" + str(round(mask.sum() / area_mul_255, 4)))
    # if mask.sum() / area_mul_255 >  #待修改


    # 饱和度从43改成30，含灰红色
    lower_red_1 = np.array([0, 30, 46])
    upper_red_1 = np.array([10, 255, 255])
    lower_red_2 = np.array([156, 30, 46])
    upper_red_2 = np.array([180, 255, 255])

    mask=cv2.inRange(HSV,lower_red_1,upper_red_1)
    cnt1 = mask.sum() / area_mul_255

    mask = cv2.inRange(HSV, lower_red_2, upper_red_2)
    cnt2 = mask.sum() / area_mul_255
    # cv2.imshow('tmp',Cyan_mask)
    # cv2.waitKey()

    print(img_name + "                  红色占比" + str(round(cnt1 + cnt2, 4)))


    lowerBlack = np.array([0, 0, 0])
    upperBlack = np.array([180,255,46])
    mask=cv2.inRange(HSV,lowerBlack,upperBlack)
    print(img_name + "                                      黑色占比" + str(round(mask.sum() / area_mul_255, 4)))


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



    img =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    s = 0
    img = img[img.shape[0]//4:img.shape[0]*3//4,img.shape[1]//4:img.shape[1]*3//4]
    sobel = cv2.Sobel(img,cv2.CV_64F, 1, 1, ksize=3)
    dst = cv2.convertScaleAbs(sobel)
    s += (dst>150).sum()
    print(img_name + "的平均信息量为", round(s / multiplyList(img.shape), 4))



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


#     sobel = cv2.Sobel(img,cv2.CV_64F, 1, 1, ksize=5)
#     dst = cv2.convertScaleAbs(sobel)
#     print(img_name + "的sobel边缘信息量为" + str(round(dst.sum() / area_mul_255, 4)))
#     # cv2.imshow(img_name, dst)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()




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