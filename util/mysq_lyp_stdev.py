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



def cntRatio2(imgName):
    db = pymysql.connect("localhost", "root", "123456", "balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    # sql = "with t_1 as (select STDDEV(CONFIDENCE) from %s where is_valid=0),t_no as (select STDDEV(CONFIDENCE) from %s where is_valid=-1),t0 as (select STDDEV(CONFIDENCE) from %s where CONFIDENCE =0 and is_valid=1),t_small as (select STDDEV(CONFIDENCE) from %s where CONFIDENCE >0 and CONFIDENCE<0.3),t1 as (select STDDEV(CONFIDENCE) from %s where CONFIDENCE >=0.3 and CONFIDENCE<0.6),t3 as (select STDDEV(CONFIDENCE)  from %s where CONFIDENCE>=0.6 and CONFIDENCE<0.9),t4 as (select STDDEV(CONFIDENCE)  from %s where CONFIDENCE>=0.9) select * from t_1,t_no,t0,t_small,t1,t3,t4"%(databaseName,databaseName,databaseName,databaseName,databaseName,databaseName,databaseName)
    sql = "with t1 as (select STDDEV(CONFIDENCE) from %s where CONFIDENCE >=0.3),t3 as (select STDDEV(CONFIDENCE)  from %s where CONFIDENCE>=0.6),t4 as (select STDDEV(CONFIDENCE)  from %s where CONFIDENCE>=0.9) select * from t1,t3,t4"%(databaseName,databaseName,databaseName)
    # print(sql)
    cursor.execute(sql)
    up = cursor.fetchall()
    # # print(up[0])
    # print(up[0])

    return up[0]
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

    l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg', '2_1004522.jpg','2_1004515.jpg',
             '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
             "3_1005250.jpg","3_1005251.jpg","3_1005253.jpg"]







    neg_list = []
    for ele in l_neg:
        if ele.split(".")[-1] == "jpg":
            tmpRes = cntRatio2(ele.split(".")[0])
            neg_list.append(tmpRes)

    # print(neg_list)
    # print(np.mean(neg_list,0))

    # neg_list.append(np.median(neg_list, 0))




    for j in range(len(neg_list[0])):
        for i in range(len(neg_list)):

            # print(str(round(neg_list[i][j]*100,2))+"%")
            print(neg_list[i][j])
        print("\n")


    pos_list = []
    for ele in l_pos:
        if ele.split(".")[-1] == "jpg":
            tmpRes = cntRatio2(ele.split(".")[0])
            pos_list.append(tmpRes)

    # print(pos_list)
    # print(np.mean(pos_list,0))

    # pos_list.append(np.median(pos_list, 0))




    for j in range(len(pos_list[0])):
        for i in range(len(pos_list)):

            # print(str(round(pos_list[i][j]*100,2))+"%")
            print(pos_list[i][j])
        print("\n")