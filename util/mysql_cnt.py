from turtle import color
from unicodedata import category
import pymysql
import numpy as np
from sklearn.metrics import confusion_matrix, f1_score, auc, roc_curve
import matplotlib.pyplot as plt
import pathlib
import pandas as pd

auc_dir = './auc'

def cntAvg(imgName):
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t1 as (select AVG(CONFIDENCE) from %s where CONFIDENCE >=0.3),t3 as (select AVG(CONFIDENCE)  from %s where CONFIDENCE>=0.6),t4 as (select AVG(CONFIDENCE)  from %s where CONFIDENCE>=0.9) select * from t1,t3,t4" % (databaseName, databaseName, databaseName)
    cursor.execute(sql)
    up = cursor.fetchall()
    return [(x if x != None else 0) for x in up[0]]


def cntNum(imgName):
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t2 as (select count(*)  from %s where CONFIDENCE>=0.3),t3 as (select count(*)  from %s where CONFIDENCE>=0.6),t4 as (select count(*)  from %s where CONFIDENCE>=0.9) select * from  t2,t3,t4" % (databaseName, databaseName, databaseName)
    cursor.execute(sql)
    up = cursor.fetchall()
    return [(x if x != None else 0) for x in up[0]]


def cntSum(imgName):
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t1 as (select SUM(CONFIDENCE) from %s where CONFIDENCE >=0.3),t3 as (select SUM(CONFIDENCE)  from %s where CONFIDENCE>=0.6),t4 as (select SUM(CONFIDENCE)  from %s where CONFIDENCE>=0.9) select * from t1,t3,t4" % (databaseName, databaseName, databaseName)
    cursor.execute(sql)
    up = cursor.fetchall()
    return [(x if x != None else 0) for x in up[0]]


LINE_WIDTH = 0.25

def draw_auc(tag, l, t):
    pathlib.Path(auc_dir).mkdir(parents=True, exist_ok=True) 
    params = {
        'axes.labelsize': 6,
        'axes.titlesize': 6,
        'axes.linewidth': LINE_WIDTH,
        'xtick.labelsize': 6,
        'ytick.labelsize': 6,
        'axes.titlepad': 1,
        'axes.labelpad': 1,
        'font.size': 12,
        'lines.linewidth': LINE_WIDTH,
        'legend.fontsize': 6,
        'legend.frameon': False,
        'lines.markersize': 2.0,
        'xtick.major.width': LINE_WIDTH,
        'ytick.major.width': LINE_WIDTH,
    }
    plt.rcParams.update(params)

    fpr, tpr, thresholds = roc_curve(
        t, l, pos_label=1, drop_intermediate=False)
    # print(np.array([tpr, fpr]).T)
    area = auc(fpr, tpr)
    plt.figure(dpi=300, figsize=(3, 2))
    # plt.title(tag)

    best_sum = 0
    best_i = 0
    for i in range(len(fpr)):
        sum_i = tpr[i] + 1 - fpr[i]
        if sum_i > best_sum:
            best_sum = sum_i
            best_i = i

    category = tag.split('_')[1]
    plt.plot(fpr, tpr, label='cut-off (%s) =%0.3f' %
             (category, thresholds[best_i]), color='black', marker='.')
    plt.plot(fpr[best_i], tpr[best_i], 'b.', markersize=4)
    plt.legend(loc="lower right")
    # plt.text(fpr[best_i], tpr[best_i], 'threshold=%0.2f' % (thresholds[best_i]))
    # plt.annotate(text='threshold=%0.2f' % (thresholds[best_i]), xy=(fpr[best_i], tpr[best_i]))

    # plt.show()
    # exit()
    out_pic = auc_dir + '/' + tag + '.tiff'
    print('saving to', out_pic)
    plt.savefig(out_pic, dpi=1200)
    plt.close()

    # print('roc=%0.1f threshold=%0.1f tpr=%0.1f fpr=%0.1f' % (area, thresholds[best_i], tpr[best_i], fpr[best_i]))
    return [area, thresholds[best_i], tpr[best_i], fpr[best_i]]


def print_val_and_draw_auc(tag, point_neg, point_pos):
    print(tag, '###############')
    point_all = np.concatenate((point_neg, point_pos))
    # for ele in point_all:
    #     print(ele)
    return draw_auc(tag, point_all, [0]*len(point_neg)+[1]*len(point_pos))


def compComplex(tag, neg_list, pos_list):
    result = []
    result.append(print_val_and_draw_auc(
        tag + '_0.3', neg_list[:, 0], pos_list[:, 0]))
    result.append(print_val_and_draw_auc(
        tag + '_0.6', neg_list[:, 1], pos_list[:, 1]))
    result.append(print_val_and_draw_auc(
        tag + '_0.9', neg_list[:, 2], pos_list[:, 2]))
    result = np.around(result, decimals=3)

    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    print('roc    ', result[:, 0])
    print('cut-off', result[:, 1])
    print('tpr    ', result[:, 2])
    print('fpr    ', result[:, 3])
    data = pd.DataFrame(result.T, index=['roc', 'cut-off', 'tpr', 'fpr'], columns=['0.3', '0.6', '0.9'])
    with pd.ExcelWriter(auc_dir + '/data.xlsx', mode='a') as writer:
        data.to_excel(writer, tag, float_format='%.3f')


def run_f_on_pics(tag, f, neg_pics, pos_pics):
    neg_list = []
    for ele in neg_pics:
        if ele.split(".")[-1] == "jpg":
            fname = ele.split(".")[0]
            fname = fname.split("/")[-1]
            tmpRes = f(fname)
            print(fname, tmpRes)
            neg_list.append(tmpRes)

    pos_list = []
    for ele in pos_pics:
        if ele.split(".")[-1] == "jpg":
            fname = ele.split(".")[0]
            fname = fname.split("/")[-1]
            tmpRes = f(fname)
            print(fname, tmpRes)
            pos_list.append(tmpRes)

    compComplex(tag, np.array(neg_list), np.array(pos_list))


def run_on_pics(tag, neg_pics, pos_pics):
    run_f_on_pics(tag + '_Num', cntNum, neg_pics, pos_pics)
    run_f_on_pics(tag + '_Avg.', cntAvg, neg_pics, pos_pics)
    run_f_on_pics(tag + '_Sum', cntSum, neg_pics, pos_pics)


def test1():
    neg_pics_A = ['001.jpg',
                  '031.jpg'
                  ]
    pos_pics_A = ['005.jpg',
                  '006.jpg',
                  '009.jpg',
                  '010.jpg',
                  '014.jpg',
                  '018.jpg',
                  ]

    neg_pics_B = ['002.jpg',
                  '004.jpg'
                  ]
    pos_pics_B = ['011.jpg',
                  '013.jpg',
                  '015.jpg',
                  '016.jpg',
                  '017.jpg',
                  '022.jpg',
                  ]

    neg_pics_C = ['003.jpg',
                  '023.jpg'
                  ]
    pos_pics_C = ['007.jpg',
                  '008.jpg',
                  '012.jpg',
                  '021.jpg',
                  '024.jpg',
                  '027.jpg',
                  ]

    run_on_pics('AB', neg_pics_A + neg_pics_B, pos_pics_A + pos_pics_B)
    run_on_pics('BC', neg_pics_B + neg_pics_C, pos_pics_B + pos_pics_C)
    run_on_pics('AC', neg_pics_A + neg_pics_C, pos_pics_A + pos_pics_C)


def test2():
    neg_pics_A = ['001.jpg',
                  '031.jpg',
                  ]
    pos_pics_A = ['006.jpg',
                  '011.jpg',
                  '015.jpg',
                  '022.jpg',
                  ]

    neg_pics_B = ['002.jpg',
                  ]
    pos_pics_B = ['005.jpg',
                  '009.jpg',
                  '013.jpg',
                  '016.jpg',
                  '024.jpg',
                  ]

    neg_pics_C = ['003.jpg',
                  ]
    pos_pics_C = ['007.jpg',
                  '010.jpg',
                  '014.jpg',
                  '017.jpg',
                  '018.jpg',
                  ]

    neg_pics_D = ['004.jpg',
                  '023.jpg',
                  ]
    pos_pics_D = ['008.jpg',
                  '012.jpg',
                  '021.jpg',
                  '027.jpg',
                  ]

    run_on_pics('ABC', neg_pics_A + neg_pics_B + neg_pics_C,
                pos_pics_A + pos_pics_B + pos_pics_C)
    run_on_pics('BCD', neg_pics_B + neg_pics_C + neg_pics_D,
                pos_pics_B + pos_pics_C + pos_pics_D)
    run_on_pics('ACD', neg_pics_A + neg_pics_C + neg_pics_D,
                pos_pics_A + pos_pics_C + pos_pics_D)
    run_on_pics('ABD', neg_pics_A + neg_pics_B + neg_pics_D,
                pos_pics_A + pos_pics_B + pos_pics_D)


if __name__ == "__main__":
    test1()
    # test2()
