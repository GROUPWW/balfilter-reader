import pymysql
import os
import numpy as np
import cv2



def cntRatio(imgName):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    # sql = "select count(*) from %s"%(databaseName)
    # # print(sql)
    # cursor.execute(sql)
    # up = cursor.fetchall()
    # print(up[0])

    up = len(os.listdir("./image_output/"+imgName))

    import math
    length = math.sqrt(up)
    print(length)
    length = int(length)

    sql = "select IMG_NAME,CONFIDENCE from %s"%(databaseName)
    # print(sql)
    cursor.execute(sql)
    table = cursor.fetchall()
    tableDic = {t[0]:t[1] for t in table}
    print(tableDic)

    resArray = np.ones((length,length))
    for i in range(length):
        for j in range(length):
            resArray[i][j] = tableDic.get(str(i)+"x"+str(j),0.0)

    return resArray
    # print(result)

def createHeatmap(imgName):
    l = [imgName]

    neg_list = []
    for ele in l:
        if ele.split(".")[-1] == "jpg":
            tmpRes = cntRatio(ele.split(".")[0])
            # print(tmpRes)

            ###########################################################################
            # tmpRes = 1 - tmpRes
            # tmpRes *= 255
            # tmpRes = tmpRes.astype(np.uint8)
            # tmpRes = cv2.applyColorMap(tmpRes,cv2.COLORMAP_HOT)
            ###########################################################################
            tmpRes = np.stack((tmpRes,) * 3, axis=-1)
            for i in range(tmpRes.shape[0]):
                for j in range(tmpRes.shape[1]):
                    if tmpRes[i][j][0] == 0:
                        tmpRes[i][j][0] = 255
                        tmpRes[i][j][1] = 255
                        tmpRes[i][j][2] = 255
                    elif 0 < tmpRes[i][j][0] <= 0.75:
                        tmpRes[i][j][0] = -256 * tmpRes[i][j][0] + 192
                        tmpRes[i][j][1] = -256 * tmpRes[i][j][1] + 192
                        tmpRes[i][j][2] = 255
                    else:
                        tmpRes[i][j][0] = 0
                        tmpRes[i][j][1] = 0
                        tmpRes[i][j][2] = -600 * tmpRes[i][j][1] + 705
            #################################################################################
            tmpRes = cv2.resize(tmpRes, (tmpRes.shape[0] * 16, tmpRes[0].shape[0] * 16),
                                interpolation=cv2.INTER_NEAREST)
            
            cv2.imwrite("./image_output/res_" + ele, tmpRes)


if __name__=="__main__":
    pass

    # # l = os.listdir("../big_img_in")
    # l_neg = [ '2_1004509.jpg', '2_1004510.jpg', '2_1004516.jpg',
    #          "3_1005256.jpg"]
    #
    # l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg', '2_1004515.jpg',
    #          '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
    #          "3_1005250.jpg", "3_1005251.jpg", "3_1005253.jpg"]
    #
    # l = l_pos + l_neg



