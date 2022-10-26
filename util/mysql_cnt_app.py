import pymysql




def cntAvg(imgName):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t0 as (select AVG(CONFIDENCE) from %s where CONFIDENCE =0 and is_valid=1), t1 as (select AVG(CONFIDENCE) from %s where CONFIDENCE >0),t2 as (select AVG(CONFIDENCE) from %s where CONFIDENCE >=0.3),t3 as (select AVG(CONFIDENCE)  from %s where CONFIDENCE>=0.6),t4 as (select AVG(CONFIDENCE)  from %s where CONFIDENCE>=0.9) select * from t0,t1,t2,t3,t4"%(databaseName,databaseName,databaseName,databaseName,databaseName)
    # print(sql)
    cursor.execute(sql)
    up = cursor.fetchall()
    # # print(up[0])
    # print(up[0])

    return up[0]
    # print(result)



def cntNum(imgName):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t0 as (select count(*) from %s where CONFIDENCE =0 and is_valid=1), t1 as (select count(*) from %s where CONFIDENCE >0),t2 as (select count(*)  from %s where CONFIDENCE>=0.3),t3 as (select count(*)  from %s where CONFIDENCE>=0.6),t4 as (select count(*)  from %s where CONFIDENCE>=0.9) select * from t0,t1,t2,t3,t4"%(databaseName,databaseName,databaseName,databaseName,databaseName)
    # print(sql)
    cursor.execute(sql)
    up = cursor.fetchall()
    # print(up[0])
    #
    # sql = "select count(*) from %s where is_Valid=1"%(databaseName)
    # cursor.execute(sql)
    # down = cursor.fetchall()
    # # print(down[0][0])
    #
    # # result = [str(round(ele/down[0][0]*100,2))+"%" for ele in up[0]]
    # result = [(ele/down[0][0]) for ele in up[0]]
    # print(imgName,"的总有效图像块数量为",down[0][0])
    # return result
    # print(result)

    return up[0]