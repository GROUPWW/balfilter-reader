# coding:utf-8
import csv
from flask import Flask, render_template, request, redirect, url_for
import requests
from flask_helper.pager import Pager
import os
from util.mysql import out_mysql
import math
from util.mysql_cnt_app import cntAvg,cntNum

# pic_name_dic = {ele.split('-')[1]: ele.split('-')[0] for ele in os.listdir('./example/images')}
def to_nxn_list(nxn,max_l,pad):
    r,c = int(nxn.split('x')[0]),int(nxn.split('x')[1])
    center_int_row = min(max_l - pad - 1, max(pad, r))
    center_int_col = min(max_l - pad - 1, max(pad, c))
    nxn_res = []
    for i in range(center_int_row - pad, center_int_row + pad + 1):
        for j in range(center_int_col - pad, center_int_col + pad+ 1):
            nxn_res.append(str(i)+"x"+str(j))
    return nxn_res



# def read_table(url):
#     """Return a list of dict"""
#     # r = requests.get(url)
#     # 加encoding = 'utf-8' 解决编码问题？
#     # name前竟然出现了\ufeff字符，改为'utf-8-sig'
#     with open(url,encoding='utf-8-sig') as f:
#         return [row for row in csv.DictReader(f.readlines())]

# 暂时设定的病例号
case_id = '3_1005251'


APPNAME = "BALFilter Reader"
STATIC_FOLDER = 'image_output' #图片只能放这里面


# TABLE_FILE = "flask_helper/example/fakecatalog.csv"
#table = read_table(TABLE_FILE)

# ！！！！！！！！！！！！！！！！最终记得把数据库替换回来

table,count_star = out_mysql(case_id)
# 如果前面写入了数据库，请用上面那行替代
# print(table)
table = [{"图像块可疑度":ele["图像块可疑度"], "nxn":ele["nxn"],"Network used":"YOLOv5"} for ele in table]

#总共多少乘以多少块图像
count_star = int(math.sqrt(count_star[0]['count_star']))

print("len(table)",len(table))
pager = Pager(len(table))


app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config.update(APPNAME=APPNAME,)


@app.route('/')
def index():
    return redirect('/0')


@app.route('/<int:ind>/')
def image_view(ind=None):
    if ind >= pager.count:
        return render_template("404.html"), 404
    else:



        # imN = case_id
        # c1 = cntAvg(imN)
        # c2 = cntNum(imN)
        #
        # # s1 = sum(c1[2:])
        # c1 = [str(round(ele,3)) for ele in c1]
        # print(c1)# ['63.7%', '31.8%', '1.8%', '1.4%', '1.3%']
        #
        # c2 = [str(ele) for ele in c2]
        # print(c2) #['0%', '4%', '43%', '78%', '93%']

        sts = []
        # for i in range(5):
        #     sts.append("Ave.:"+c1[i]+" & Num:"+c2[i])

        sts.append("Ave.:" + "0.682" + " & Num:" + "101")
        sts.append("Ave.:" + "0.857" + " & Num:" + "59")
        sts.append("Ave.:"+"0.929"+" & Num:"+"29")



        pager.current = ind
        # for key in table[ind]:
        #     print(key)
        table[ind]['3x3_list'] =to_nxn_list(table[ind]['nxn'],count_star,1)
        table[ind]['5x5_list'] =to_nxn_list(table[ind]['nxn'],count_star,2)
        table[ind]['Location'] = table[ind]['nxn'].replace("x", " Row  ") + ' Col'
        table[ind]['find_img'] =case_id+'/'
        table[ind]['Case ID'] =case_id
        table[ind]['sts'] = sts

        # print(table[ind])

        # 这些参数其实就是在传键值对
        return render_template(
            'imageview.html',
            index=ind,
            pager=pager,
            data=table[ind])


# @app.route('/goto', methods=['POST', 'GET'])
# def goto():
#     return redirect('/' + request.form['index'])


if __name__ == '__main__':
    #debug应该开吗，对于部署；当然是不能开啊。。。。

    #这一套也很慢
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)

    app.run(host='0.0.0.0', port=8080,threaded=True)
