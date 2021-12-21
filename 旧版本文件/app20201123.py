import csv
from flask import Flask, render_template, request, redirect, url_for
import requests
from pager import Pager
import os

pic_name_dic = {ele.split('-')[1]: ele.split('-')[0] for ele in os.listdir('./example/images')}
def to_nxn_list(nxn,max_l,pad):
    r,c = int(nxn.split('x')[0]),int(nxn.split('x')[1])
    center_int_row = min(max_l - pad - 1, max(pad, r))
    center_int_col = min(max_l - pad - 1, max(pad, c))
    nxn_res = []
    for i in range(center_int_row - pad, center_int_row + pad + 1):
        for j in range(center_int_col - pad, center_int_col + pad+ 1):
            nxn_res.append(pic_name_dic[str(i)+"x"+str(j)+".png"]+'-'+str(i)+"x"+str(j))
    return nxn_res



def read_table(url):
    """Return a list of dict"""
    # r = requests.get(url)
    # 加encoding = 'utf-8' 解决编码问题？
    # name前竟然出现了\ufeff字符，改为'utf-8-sig'
    with open(url,encoding='utf-8-sig') as f:
        return [row for row in csv.DictReader(f.readlines())]




APPNAME = "GROUPWW_CELL"
STATIC_FOLDER = 'example'
TABLE_FILE = "example/fakecatalog.csv"

#table = read_table(TABLE_FILE)
table = out_mysql('000000')



print(table[0])

pager = Pager(len(table))


app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config.update(
    APPNAME=APPNAME,
    )


@app.route('/')
def index():
    return redirect('/0')


@app.route('/<int:ind>/')
def image_view(ind=None):
    if ind >= pager.count:
        return render_template("404.html"), 404
    else:
        pager.current = ind
        #print(table[ind])
        # for key in table[ind]:
        #     print(key)
        # table[ind]['图像块在原图的位置'] = table[ind]['图像块在原图的位置'].replace("x", "行 ")+'列'
        table[ind]['3x3_list'] =to_nxn_list(table[ind]['name'].split('-')[1],int(table[ind]['病例编号']),1)
        table[ind]['5x5_list'] =to_nxn_list(table[ind]['name'].split('-')[1],int(table[ind]['病例编号']),2)
        return render_template(
            'imageview.html',
            index=ind,
            pager=pager,
            data=table[ind])


@app.route('/goto', methods=['POST', 'GET'])    
def goto():
    return redirect('/' + request.form['index'])


if __name__ == '__main__':
    #debug应该开吗，对于部署
    #好像得用一个叫uwsgi的部署,uwsgi只支持linux
    app.run(host='0.0.0.0', port=8080,threaded=True)
