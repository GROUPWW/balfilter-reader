import os

checkedDirList = ["Data20211129-yolo-added-neg/Data-yolo-txt/data/train2017",
                  "Data20211129-yolo-added-neg/Data-yolo-txt/data/val2017",
                  "Data20211129-yolo-added-neg/Data-yolo-txt/excluded-sus-img"]

checkedImgList = []
for aCheckedDir in checkedDirList:
    tmpCheckedImgList = os.listdir(aCheckedDir)
    checkedImgList += tmpCheckedImgList

print(len(checkedImgList))



deletedFold = "RRRRRRemainImg"
deletedImgList = os.listdir(deletedFold)


for ele in deletedImgList:
    if ele in checkedImgList:
        shouldDeleteDirImg = deletedFold + "/" + ele
        os.remove(shouldDeleteDirImg)