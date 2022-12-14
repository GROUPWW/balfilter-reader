import pymysql

class in_mysql():
    def __init__(self,case_id_and_model):
        self.case_id_and_model = case_id_and_model
        # print(type(case_id_and_model))
        self.db  = pymysql.connect(host="localhost", user="root", password="123456", db="balf")
        self.cursor = self.db.cursor()
        self.sql = "DROP TABLE IF EXISTS DATABASE_%s" % (self.case_id_and_model)
        self.cursor.execute(self.sql)
        self.sql = "CREATE TABLE DATABASE_%s (`id` INT PRIMARY KEY AUTO_INCREMENT,IMG_NAME  CHAR(20) NOT NULL,CONFIDENCE FLOAT,MODEL CHAR(20),IS_VALID INT,IS_ACCEPTED INT,IS_POSITIVE INT,COMMENT  VARCHAR (5000))" % (case_id_and_model)
        self.cursor.execute(self.sql)
        print('Database ',case_id_and_model,' created successfully')


    def write_in_database(self,nxn_img_name,conf,used_model,isValid):
        self.sql =  "INSERT INTO DATABASE_%s(IMG_NAME,CONFIDENCE,MODEL,IS_VALID,IS_ACCEPTED,IS_POSITIVE) VALUES ('%s', %s,'%s','%d',0,-1)" %(self.case_id_and_model,nxn_img_name,conf,used_model,isValid)
        self.cursor.execute(self.sql)



def out_mysql(case_id_and_model):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="balf")
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
    db = pymysql.connect(host="localhost", user="root", password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t2 as (select count(*)  from %s where CONFIDENCE>=0.3),t3 as (select count(*)  from %s where CONFIDENCE>=0.6),t4 as (select count(*)  from %s where CONFIDENCE>=0.9) select * from  t2,t3,t4"%(databaseName,databaseName,databaseName)
    # print(sql)
    cursor.execute(sql)
    up = cursor.fetchall()
    # print(up[0])

    sql = "select count(*) from %s where is_Valid=1"%(databaseName)
    cursor.execute(sql)
    down = cursor.fetchall()
    # print(down[0][0])

    # result = [str(round(ele/down[0][0]*100,2))+"%" for ele in up[0]]
    result = [round(ele/down[0][0],4) for ele in up[0]]
    print(imgName,"的总有效图像块数量为",down[0][0])
    return result
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
            tmpRes = cntRatio(ele.split(".")[0])
            neg_list.append(tmpRes)

    # print(neg_list)
    # print(np.mean(neg_list,0))

    # neg_list.append(np.median(neg_list, 0))

    zhongzhimean = []
    col_jige_means = []
    for j in range(len(neg_list[0])):

        col = []
        for i in range(len(neg_list)):
            col.append(neg_list[i][j])
        zhongzhimean.append(zhongzhi(col))
        col_jige_means.append(geometric_mean(col))
    neg_list.append(np.mean(neg_list, 0))
    neg_list.append(zhongzhimean)
    neg_list.append(col_jige_means)


    for j in range(len(neg_list[0])):
        for i in range(len(neg_list)):

            print(str(round(neg_list[i][j]*100,2)),end=",")
        print("\n")


    pos_list = []
    for ele in l_pos:
        if ele.split(".")[-1] == "jpg":
            tmpRes = cntRatio(ele.split(".")[0])
            pos_list.append(tmpRes)

    # print(pos_list)
    # print(np.mean(pos_list,0))

    # pos_list.append(np.median(pos_list, 0))
    
    col_jige_means = []
    zhongzhimean = []
    for j in range(len(pos_list[0])):

        col = []
        for i in range(len(pos_list)):
            col.append(pos_list[i][j])
        zhongzhimean.append(zhongzhi(col))
        col_jige_means.append(geometric_mean(col))
    pos_list.append(np.mean(pos_list, 0))
    pos_list.append(zhongzhimean)
    pos_list.append(col_jige_means)


    for j in range(len(pos_list[0])):
        for i in range(len(pos_list)):

            print(str(round(pos_list[i][j]*100,2)),end=",")
        print("\n")