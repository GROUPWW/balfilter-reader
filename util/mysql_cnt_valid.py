import pymysql
import numpy as np
from sklearn.metrics import confusion_matrix, f1_score, auc, roc_curve
import matplotlib.pyplot as plt


def cntValid(imgName):
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="balf")
    cursor = db.cursor()
    databaseName = "database_" + imgName
    sql = "with t2 as (select count(*)  from %s where IS_VALID=1) select * from  t2" % (databaseName)
    cursor.execute(sql)
    up = cursor.fetchall()
    return [(x if x != None else 0) for x in up[0]][0]


def run_f_on_pics(f, neg_pics, pos_pics):
    for ele in neg_pics:
        if ele.split(".")[-1] == "jpg":
            fname = ele.split(".")[0]
            fname = fname.split("/")[-1]
            tmpRes = f(fname)
            print(fname, tmpRes)

    for ele in pos_pics:
        if ele.split(".")[-1] == "jpg":
            fname = ele.split(".")[0]
            fname = fname.split("/")[-1]
            tmpRes = f(fname)
            print(fname, tmpRes)


if __name__ == "__main__":

    neg_pics_A = ['001.jpg',
                '031.jpg'
                ]
    pos_pics_A = ['005.jpg',
                '006.jpg',
                '009.jpg',
                '010.jpg',
                '018.jpg',
                '021.jpg',
                ]

    neg_pics_B = ['002.jpg',
                '004.jpg'
                ]
    pos_pics_B = ['011.jpg',
                '013.jpg',
                '015.jpg',
                '016.jpg',
                '017.jpg',
                '024.jpg',
                ]

    neg_pics_C = ['003.jpg',
                '032.jpg'
                ]
    pos_pics_C = ['007.jpg',
                '008.jpg',
                '012.jpg',
                '014.jpg',
                '022.jpg',
                '027.jpg',
                ]

    run_f_on_pics(cntValid, neg_pics_A + neg_pics_B + neg_pics_C, pos_pics_A + pos_pics_B + pos_pics_C)