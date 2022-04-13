import pymysql


from sklearn.metrics import confusion_matrix,f1_score,auc,roc_curve
import matplotlib.pyplot as plt
from fast_detect import fast_detect_cnt
import numpy as np


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

    def zhongzhi(data):
        data_s = sorted(data)
        return data_s[len(data_s)//2] if len(data_s) % 2 == 1 else (data_s[len(data_s)//2-1] + data_s[len(data_s)//2]) / 2

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



    #
    # neg_list_num,pos_list_num = inputAFunC(cntNum)
    # neg_list_avg,pos_list_avg = inputAFunC(cntAvg)

    neg_list_num, pos_list_num, neg_list_avg, pos_list_avg = fast_detect_cnt()

    print(neg_list_num)


    # print(neg_list_ratio,pos_list_ratio,sep="\n")

    neg_list = neg_list_num*neg_list_avg
    pos_list = pos_list_num*pos_list_avg
    # print(neg_list,pos_list,sep="\n")




    compComplexAll(neg_list_num, pos_list_num, neg_list_avg, pos_list_avg, neg_list, pos_list)