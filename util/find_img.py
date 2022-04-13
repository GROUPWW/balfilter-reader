import pymysql








def cntRatio(imgName):
    db = pymysql.connect("localhost", "root", "123456", "balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "select IMG_NAME  from %s where CONFIDENCE>0 and CONFIDENCE<0.3"%(databaseName)
    # print(sql)
    cursor.execute(sql)
    up = cursor.fetchall()

    return up
    # print(result)

bigInSS = ['2_1004518',  '2_1004522',
         '1003989',  '1003998',
         "3_1005253"]

for bigIn in bigInSS:

    l1 = cntRatio(bigIn)

    l2 = [ele[0] for ele in l1]

    print(l2)

    l3 = ["../image_output/"+bigIn+"/"+ele+".jpg" for ele in l2]

    print(l3)

    import os

    # os.makedirs("resImg")

    import shutil
    for ele in l2:
        shutil.copy("../image_output/"+bigIn+"/"+ele+".jpg", "resImg"+"/"+bigIn+"_"+ele+".jpg")


