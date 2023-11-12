
import csv
import pandas as pd
import numpy as np


df = pd.read_csv("CNNStreetNames.csv")



def listOfCNN(start, on, end):
    if start == '' or on == '' or end =='':
        return [1]
    CNNs = [[]]
    startCNN = df[df.streetname == on]
    startCNN = startCNN[startCNN.from_st == start]
    startCNN2 = df[df.streetname == start]
    startCNN2 = startCNN2[startCNN2.from_st == on]
    startCNN = pd.concat([startCNN,startCNN2], axis=0, ignore_index=True)
    #startCNN = startCNN[startCNN.CNN > 10000000]
    
    endCNN = df[df.streetname == on]
    endCNN = endCNN[endCNN.from_st == end]
    endCNN2 = df[df.streetname == end]
    endCNN2= endCNN2[endCNN2.from_st == on]
    endCNN = pd.concat([endCNN,endCNN2], axis=0, ignore_index=True)
    #endCNN = endCNN[endCNN.CNN > 10000000]
    CNNs=[[float(startCNN[startCNN.CNN > 10000000].iloc[0]["CNN"])]]
    endCNN=int(endCNN[endCNN.CNN > 10000000].iloc[0]["CNN"])
    endCNN=CNNs[0][0]+2000
    notdone = True
    while notdone:
        newCNNS=[]
      
        for i in CNNs:
            intersection = i[-1]
            fromm = df[df.FROM_CNN == intersection]
            hope = fromm[fromm.TO_CNN == endCNN]
            if hope.empty:
                fromm = fromm[~fromm.TO_CNN.isin(i)]
                for index,row in fromm.iterrows():
                    newCNNS.append(i+[row["CNN"],row["TO_CNN"]])
            else:
               
                a = i
                a.append(hope.iloc[0]["CNN"])
                a.append(endCNN)
                newCNNS = a
                notdone = False
                break
            too = df[df.TO_CNN == intersection]
            hope = too[too.FROM_CNN == endCNN]
            if hope.empty:
                too = too[~too.FROM_CNN.isin(i)]
                for index,row in too.iterrows():
                    newCNNS.append(i+[row["CNN"],row["FROM_CNN"]])
            else:
               
                a = i
                a.append(hope.iloc[0]["CNN"])
                a.append(endCNN)
                newCNNS = a
                notdone = False
                break
        CNNs = newCNNS
    for i in range(len(CNNs)):
        CNNs[i]=int(CNNs[i])
    return CNNs
            
inter = pd.concat([pd.read_csv("intersectonValue.csv"),pd.read_csv("segmentValue.csv")], axis=0, ignore_index=True)

def saftey(a):
    safteys = []
    for i in a:
        e = inter[inter.cnn_intrsctn_fkey == i]
        if e.empty:
            safteys.append(1)
        else:
            safteys.append(e.iloc[0]["ped_action"])
    return safteys

def SafteyOfBLocks(start, on, end):
    while len(on) != 0 and on not in df['streetname'].unique():
        on = on[:-1]
    if len(on) == 0:
        return [1]
    
    test = df[df.streetname == on]
    
    starttest = test[test.from_st == start]
    while len(start)>0 and starttest.empty:
        start = start[:-1]
        starttest = test[test.from_st == start] 
    if len(start) == 0:
        return [1]
    
    endtest = test[test.from_st == end]
    while len(end)>0 and endtest.empty:
        end = end[:-1]
        endtest = test[test.from_st == end] 
    if len(end) == 0:
        return [1]
    
    return saftey(listOfCNN(start, on, end))
    

b = SafteyOfBLocks("HAIGHT ST","CENTRAL AVE", "BUENA VISTA AVE")

print(b)