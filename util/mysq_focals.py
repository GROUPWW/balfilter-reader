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
    l_neg = []

    l_pos = ['2_1004521.jpg']


    l = l_pos + l_neg

    # l = ["1008906.jpg"]

    import cv2
    neg_list = []
    for ele in l:
        if ele.split(".")[-1] == "jpg":
            tmpRes = cntRatio(ele.split(".")[0])
            print(tmpRes)



            # tmpRes = cv2.resize(tmpRes,(tmpRes.shape[0]*64,tmpRes.shape[1]*64),interpolation=cv2.INTER_NEAREST)
            tmpResBig = np.ones((tmpRes.shape[0]*64,tmpRes.shape[1]*64))
            for i in range(tmpResBig.shape[0]):
                for j in range(tmpResBig.shape[1]):
                    # print(i,j,i//64,j//64)
                    tmpResBig[i][j] = tmpRes[i//64][j//64]
            tmpRes = tmpResBig

            # print(tmpRes)
            a = tmpRes >= 0.9

            # print(a)

            row = cv2.imread("../big_img_in/"+ele)
            row1 = row[0:tmpRes.shape[0]*4,0:tmpRes.shape[1]*4]
            row2 = cv2.resize(row1, (tmpRes.shape[0], tmpRes.shape[1]))

            a = np.stack((a,) * 3, axis=-1)

            print(tmpRes.shape[0],tmpRes.shape[1])
            for i in range(tmpRes.shape[0]):
                for j in range(tmpRes.shape[1]):
                        if a[i][j][0] == True:
                            row2[i][j][0] = 0
                            row2[i][j][1] = 0
                            row2[i][j][2] = 255
            print(row2)
            cv2.imwrite("res_" + ele, row2)





