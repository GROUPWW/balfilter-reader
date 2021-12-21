import os

from xml.dom.minidom import parse
import xml.dom.minidom
import cv2

Annotations = os.listdir("Annotations")
for Annotation in Annotations:

    # 使用minidom解析器打开 XML 文档
    print("Annotations/"+Annotation)
    DOMTree = xml.dom.minidom.parse("Annotations/"+Annotation)
    collection = DOMTree.documentElement
    path = collection.getElementsByTagName('path')

    print(DOMTree)
    print(collection)
    print(path[0].childNodes[0].data)
    path[0].childNodes[0].data = "".join(path[0].childNodes[0].data.split(".")[:-1]) + ".jpg"
    print(path[0].childNodes[0].data)

    fileName = collection.getElementsByTagName('filename')
    print(fileName[0].childNodes[0].data)
    fileName[0].childNodes[0].data += ".jpg"
    print(fileName[0].childNodes[0].data)

    try:
        with open('res/Annotations/'+Annotation,'w',encoding='UTF-8') as fh:
            # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
            # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
            collection.writexml(fh,indent='',addindent='\t')
            print('OK')
    except Exception as err:
        print('错误：{err}'.format(err=err))


JPEGImages = os.listdir("JPEGImages")
for JPEGImage in JPEGImages:

    print("JPEGImages/"+JPEGImage)
    img = cv2.imread("JPEGImages/"+JPEGImage)
    cv2.imwrite("res/JPEGImages/"+"".join(JPEGImage.split(".")[:-1]) + ".jpg",img)