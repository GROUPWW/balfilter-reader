import pymysql

class in_mysql():
    def __init__(self,case_id_and_model):
        self.case_id_and_model = case_id_and_model
        print(type(case_id_and_model))
        self.db  = pymysql.connect("localhost", "root", "123456", "balf")
        self.cursor = self.db.cursor()
        self.sql = "DROP TABLE IF EXISTS DATABASE_%s" % (self.case_id_and_model)
        self.cursor.execute(self.sql)
        self.sql = "CREATE TABLE DATABASE_%s (IMG_NAME  CHAR(20) NOT NULL,CONFIDENCE FLOAT,MODEL CHAR(20),IS_VALID INT,IS_ACCEPTED INT,COMMENT  VARCHAR (5000))" % (case_id_and_model)
        self.cursor.execute(self.sql)
        print('创建数据库',case_id_and_model,'成功')


    def write_in_database(self,nxn_img_name,conf,used_model,isValid):
        self.sql =  "INSERT INTO DATABASE_%s(IMG_NAME,CONFIDENCE,MODEL,IS_VALID,IS_ACCEPTED) VALUES ('%s', %s,'%s','%d',0)" %(self.case_id_and_model,nxn_img_name,conf,used_model,isValid)
        self.cursor.execute(self.sql)



def out_mysql(case_id_and_model):
    db = pymysql.connect("localhost", "root", "123456", "balf")
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor) #变成字典形式的输出
    sql = "SELECT CONFIDENCE '图像块可疑度',IMG_NAME 'nxn' ,MODEL '使用的目标检测模型' FROM DATABASE_%s ORDER BY CONFIDENCE DESC" % (case_id_and_model)
    cursor.execute(sql)
    results = cursor.fetchall()
    sql = "SELECT count(*) count_star FROM DATABASE_%s" % (case_id_and_model)
    cursor.execute(sql)
    count_star = cursor.fetchall()
    # print(results)
    # print(count_star)
    return results,count_star



def cntRatio(imgName):
    db = pymysql.connect("localhost", "root", "123456", "balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "select count(*) from %s"%(databaseName)
    # print(sql)
    cursor.execute(sql)
    up = cursor.fetchall()
    # print(up[0])
    import math
    length = math.sqrt(up[0][0])
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


            resArray[i][j] = tableDic[str(i)+"x"+str(j)]

    # print(down[0][0])

    # # result = [str(round(ele/down[0][0]*100,2))+"%" for ele in up[0]]
    # result = [round(ele/down[0][0],4) for ele in up[0]]
    # print(imgName,"的总有效图像块数量为",down[0][0])
    return resArray
    # print(result)

if __name__=="__main__":

    def geometric_mean(data):  # 计算几何平均数
        total = 1
        for i in data:
            total *= i  # 等同于total=total*i
        return pow(total, 1 / len(data))

    def zhongzhi(data):
        data_s = sorted(data)
        return data_s[len(data_s)//2] if len(data_s) % 2 == 1 else (data_s[len(data_s)//2-1] + data_s[len(data_s)//2]) / 2

    import os
    import numpy as np
    # l = os.listdir("../big_img_in")
    l_neg = [ '2_1004509.jpg', '2_1004510.jpg', '2_1004516.jpg',
             "3_1005256.jpg"]

    # l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg','2_1004515.jpg',
    #          '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg']

    l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg', '2_1004515.jpg',
             '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
             "3_1005250.jpg", "3_1005251.jpg", "3_1005253.jpg"]


    l = l_pos + l_neg

    # l = ["3_1005251.jpg"]

    import cv2
    neg_list = []
    for ele in l:
        if ele.split(".")[-1] == "jpg":
            tmpRes = cntRatio(ele.split(".")[0])
            print(tmpRes)

###########################################################################
            tmpRes = 1 - tmpRes
            tmpRes *= 255
            tmpRes = tmpRes.astype(np.uint8)
            tmpRes = cv2.applyColorMap(tmpRes,cv2.COLORMAP_HOT)
###########################################################################
###########################################################################
            # tmpRes = np.stack((tmpRes,) * 3, axis=-1)
            # for i in range(tmpRes.shape[0]):
            #     for j in range(tmpRes.shape[1]):
            #             if tmpRes[i][j][0] == 0:
            #                 tmpRes[i][j][0] = 255
            #                 tmpRes[i][j][1] = 255
            #                 tmpRes[i][j][2] = 255
            #             elif 0<tmpRes[i][j][0] <= 0.75:
            #                 tmpRes[i][j][0] = -256 * tmpRes[i][j][0] + 192
            #                 tmpRes[i][j][1] = -256 * tmpRes[i][j][1] + 192
            #                 tmpRes[i][j][2] = 255
            #             else:
            #                 tmpRes[i][j][0] = 0
            #                 tmpRes[i][j][1] = 0
            #                 tmpRes[i][j][2] = -600*tmpRes[i][j][1] + 705
#################################################################################

            #
            # [0-0.75] -> （255，192，192）-(255,0,0)
            # y = ax + b
            # 192 = b
            # y = ax + 192
            # 0 = -256 * 0.75 + 192
            # [0.75-0.95] ->(255,0,0) - (135,0,0)
            # y = ax + b
            # y = -600x + b
            # 255 = -450 + b







            tmpRes = cv2.resize(tmpRes,(tmpRes.shape[0]*16,tmpRes[1].shape[0]*16),interpolation=cv2.INTER_NEAREST)
            cv2.imwrite("res_"+ele,tmpRes)

