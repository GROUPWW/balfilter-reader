def cnt(TP,TN,FP,FN):
    tyd = round(TN/(FP+TN),3)
    lmd = round(TP/(TP+FN),3)
    ACC = round((TP+TN)/(TP+TN+FP+FN),3)
    yang= round(TP / (TP + FP),3)
    yin = round(TN / (TN + FN),3)
    print(tyd,lmd,ACC,yang,yin)

cnt(TP=9,TN=3,FP=1,FN=5)

cnt(8,4,0,6)
cnt(9,1,3,5)

