import pymysql

def cntRatio(imgName):
    db = pymysql.connect("localhost", "root", "123456", "balf")
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
    result = [(ele/down[0][0]) for ele in up[0]]
    # print(imgName,"的总有效图像块数量为",down[0][0])
    return result
    # print(result)


def cntAvg(imgName):
    db = pymysql.connect("localhost", "root", "123456", "balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t1 as (select AVG(CONFIDENCE) from %s where CONFIDENCE >=0.3),t3 as (select AVG(CONFIDENCE)  from %s where CONFIDENCE>=0.6),t4 as (select AVG(CONFIDENCE)  from %s where CONFIDENCE>=0.9) select * from t1,t3,t4"%(databaseName,databaseName,databaseName)
    # print(sql)
    cursor.execute(sql)
    up = cursor.fetchall()
    # # print(up[0])
    # print(up[0])

    return up[0]
    # print(result)



def cntNum(imgName):
    db = pymysql.connect("localhost", "root", "123456", "balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t2 as (select count(*)  from %s where CONFIDENCE>=0.3),t3 as (select count(*)  from %s where CONFIDENCE>=0.6),t4 as (select count(*)  from %s where CONFIDENCE>=0.9) select * from  t2,t3,t4"%(databaseName,databaseName,databaseName)
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

from sklearn.metrics import confusion_matrix,f1_score,auc,roc_curve
import matplotlib.pyplot as plt
def cnt(TP,TN,FP,FN,l,t,m=0):
    # print(TP,TN,FP,FN)
    # print(t)
    # print(m)
    tyd = round(TN/(FP+TN),3)
    lmd = round(TP/(TP+FN),3)
    ACC = round((TP+TN)/(TP+TN+FP+FN),3)
    yang= round(TP / (TP + FP),3)
    yin = round(TN / (TN + FN),3)

    fpr, tpr, thresholds = roc_curve(t, l,pos_label=1,drop_intermediate = False)

    # print(thresholds)

    area = auc(fpr, tpr)
    # #
    # # # 画图
    plt.figure()

    plt.plot(fpr, tpr, label='ROC curve (AUC = %0.3f)' % area)
    # plt.scatter(fpr, tpr, c="r")
    # for i in range(len(fpr)):
    #     # plt.text(fpr[i], tpr[i], str(round(1-fpr[i],3))+","+str(round(tpr[i],3)), ha='center', va='bottom')
    #     plt.text(fpr[i], tpr[i], str(round(thresholds[i], 3)), ha='center', va='bottom')
    plt.legend(loc="lower right")
    plt.show()
    #
    #
    print(tyd,lmd,ACC,yang,yin,sep="\n")
    print(round(area ,3))
    print("\n\n")








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

    # l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg','2_1004522.jpg','2_1004515.jpg',
    #          '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
    #          "3_1005250.jpg","3_1005251.jpg","3_1005253.jpg"]

    l_pos = ['2_1004518.jpg', '2_1004519.jpg', '2_1004521.jpg','2_1004522.jpg','2_1004515.jpg',
             '1003989.jpg', '1003993.jpg', '1003994.jpg', '1003995.jpg', '1003997.jpg', '1003998.jpg',
             "3_1005250.jpg","3_1005251.jpg","3_1005253.jpg"]



    def resList(f):
    ####################################################################
        neg_list = []
        for ele in l_neg:
            if ele.split(".")[-1] == "jpg":
                tmpRes = f(ele.split(".")[0])
                neg_list.append(tmpRes)


        for j in range(len(neg_list[0])):

            col = []
            for i in range(len(neg_list)):
                col.append(neg_list[i][j])





        pos_list = []
        for ele in l_pos:
            if ele.split(".")[-1] == "jpg":
                tmpRes = f(ele.split(".")[0])
                pos_list.append(tmpRes)



        for j in range(len(pos_list[0])):

            col = []
            for i in range(len(pos_list)):
                col.append(pos_list[i][j])



        for j in range(len(pos_list[0])):
            for i in range(len(pos_list)):

                # print(str(round(pos_list[i][j]*100,2))+"%")
            # print("\n")
                pass

    ###################################################################################################################
        # print(neg_list)
        return neg_list,pos_list

    from sklearn import preprocessing
    import numpy as np
    def norm(l):
        ma = max(l)
        mi = min(l)
        return [(ele - mi)/(ma-mi) for ele in l]


    def inputAFunC(f):
        # neg_list1,pos_list1 = resList(f)
        # list1 = np.array(neg_list1 + pos_list1)
        #
        # t = [norm(list1[:,0]),norm(list1[:,1]),norm(list1[:,2])]
        #
        # t = np.array(t).transpose()
        # list1 = t.copy()
        #
        # neg_list,pos_list = list1[:4],list1[4:]
        # return neg_list,pos_list


        neg_list1,pos_list1 = resList(f)
        return np.array(neg_list1),np.array(pos_list1)

    def compComplex(neg_list,pos_list):

        # print(np.array(neg_list[-1]))
        #
        # print("################################")
        # print(np.array(pos_list[-1]))
        #
        #
        # print("################################")

        m_zhongzhi_n = [zhongzhi(neg_list[:,0]),zhongzhi(neg_list[:,1]),zhongzhi(neg_list[:,2])]
        m_zhongzhi_p = [zhongzhi(pos_list[:,0]), zhongzhi(pos_list[:,1]), zhongzhi(pos_list[:,2])]


        m_zhongzhi = [(m_zhongzhi_n[i]+m_zhongzhi_p[i])/2 for i in range(3)]
        # print(m_zhongzhi_n )
        # print()
        # print(m_zhongzhi_p)
        # print(m_zhongzhi)

        # neg_list = np.array(neg_list[:-1])
        # pos_list = np.array(pos_list[:-1])

        point3_neg = neg_list[:,0]
        point6_neg = neg_list[:,1]
        point9_neg = neg_list[:,2]
        point3_pos = pos_list[:,0]
        point6_pos = pos_list[:,1]
        point9_pos = pos_list[:,2]
        # print(point9_pos)


        print("\n\n\n\n")
        for ele in np.concatenate((point3_neg,point3_pos)):
            print(ele)

        print("###############################")

        for ele in np.concatenate((point6_neg,point6_pos)):
            print(ele)

        print("###############################")

        for ele in np.concatenate((point9_neg,point9_pos)):
            print(ele)

        print("###############################")



        m_zhongzhi3,m_zhongzhi6,m_zhongzhi9 = m_zhongzhi[:]


        p = point3_pos
        n = point3_neg

        TP,TN,FP,FN = 0,0,0,0
        for ele in p:
            if ele >= m_zhongzhi3:
                TP += 1
            else:

                FN += 1

        for ele in n:
            if ele >= m_zhongzhi3:
                FP += 1
            else:
                TN += 1

        cnt(TP,TN,FP,FN,np.concatenate((n,p)),[0]*len(n)+[1]*len(p),m=m_zhongzhi3)



        p = point6_pos
        n = point6_neg

        TP,TN,FP,FN = 0,0,0,0
        for ele in p:
            if ele >= m_zhongzhi6:
                TP += 1
            else:
                FN += 1

        for ele in n:
            if ele >= m_zhongzhi6:
                FP += 1
            else:
                TN += 1

        cnt(TP,TN,FP,FN,np.concatenate((n,p)),[0]*len(n)+[1]*len(p),m=m_zhongzhi6)



        p = point9_pos
        n = point9_neg

        TP,TN,FP,FN = 0,0,0,0
        for i in range(len(p)):
            if p[i] >= m_zhongzhi9:
                TP += 1
            else:
                # print(i)
                FN += 1

        for ele in n:
            if ele >= m_zhongzhi9:
                FP += 1
            else:
                TN += 1

        cnt(TP,TN,FP,FN,np.concatenate((n,p)),[0]*len(n)+[1]*len(p),m=m_zhongzhi9)


    def compComplexAll(neg_list_num, pos_list_num, neg_list_avg, pos_list_avg, neg_list, pos_list):
        compComplex(neg_list_num, pos_list_num)
        compComplex(neg_list_avg, pos_list_avg)
        compComplex(neg_list, pos_list)




    # neg_list_num,pos_list_num = inputAFunC(cntNum)
    # neg_list_avg,pos_list_avg = inputAFunC(cntAvg)
    #
    # # print(neg_list_ratio,pos_list_ratio,sep="\n")
    #
    # neg_list = neg_list_num*neg_list_avg
    # pos_list = pos_list_num*pos_list_avg
    # # print(neg_list,pos_list,sep="\n")
    # compComplexAll(neg_list_num, pos_list_num, neg_list_avg, pos_list_avg, neg_list, pos_list)


    neg_list,pos_list = inputAFunC(cntRatio)
    compComplex(neg_list, pos_list)



