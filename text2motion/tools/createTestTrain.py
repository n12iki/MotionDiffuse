import numpy as np
import pandas as pd
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

random.seed(1)
columns=["RIGHT_WRIST_X","RIGHT_WRIST_Y","RIGHT_THUMB_TIP_X","RIGHT_THUMB_TIP_Y",
                      "RIGHT_INDEX_FINGER_TIP_X","RIGHT_INDEX_FINGER_TIP_Y","RIGHT_MIDDLE_FINGER_TIP_X",
                      "RIGHT_MIDDLE_FINGER_TIP_Y","RIGHT_RING_FINGER_TIP_X","RIGHT_RING_FINGER_TIP_Y",
                      "RIGHT_PINKY_TIP_X","RIGHT_PINKY_TIP_Y","LEFT_WRIST_X","LEFT_WRIST_Y",
                      "LEFT_THUMB_TIP_X","LEFT_THUMB_TIP_Y","LEFT_INDEX_FINGER_TIP_X","LEFT_INDEX_FINGER_TIP_Y",
                      "LEFT_MIDDLE_FINGER_TIP_X","LEFT_MIDDLE_FINGER_TIP_Y","LEFT_RING_FINGER_TIP_X",
                      "LEFT_RING_FINGER_TIP_Y","LEFT_PINKY_TIP_X","LEFT_PINKY_TIP_Y","NOSE_X","NOSE_Y","LEFT_EAR_X",
                      "LEFT_EAR_Y","RIGHT_EAR_X","RIGHT_EAR_Y","MOUTH_LEFT_X","MOUTH_LEFT_Y","MOUTH_RIGHT_X","MOUTH_RIGHT_Y",
                      "LEFT_SHOULDER_X","LEFT_SHOULDER_Y","RIGHT_SHOULDER_X","RIGHT_SHOULDER_Y","LEFT_ELBOW_X","LEFT_ELBOW_Y",
                      "RIGHT_ELBOW_X","RIGHT_ELBOW_Y"
                      ]

trainTable=pd.read_csv("/home/n12i/Desktop/french/final/train.csv")
testTable=pd.read_csv("/home/n12i/Desktop/french/final/test.csv")
valTable=pd.read_csv("/home/n12i/Desktop/french/final/val.csv")

for index, row in trainTable.iterrows():
    name=get_random_string(20)
    #print(row[columns])
    result=np.array([])
    length=row["RIGHT_WRIST_X"][1:-1].replace("\n", "").replace("  "," ").split(" ")
    length=len(list(filter(("").__ne__, length)))
    for j in range(length):
        frame=[]
        for i in row[columns]:
            i=i[1:-1].replace("\n", "").replace("  "," ").split(" ")
            i=list(filter(("").__ne__, i))
            frame.append(float(i[j]))
        if len(result)!=0:
            result=np.vstack((result, frame))
        else:
            result=np.array(frame)
    with open("./landmarks/"+str(index)+name+'.npy', 'wb') as f:
        np.save(f, result)
    with open("./text/"+str(index)+name+".txt",'w') as f:
        print(row["sentence"])
        f.write(row["sentence"])
    if index==0:
        with open("train.txt","w") as f:
            f.write(str(index)+name+"\n")
    else:
        with open("train.txt","a") as f:
            f.write(str(index)+name+"\n")


for index, row in testTable.iterrows():
    name=get_random_string(20)
    #print(row[columns])
    result=np.array([])
    length=row["RIGHT_WRIST_X"][1:-1].replace("\n", "").replace("  "," ").split(" ")
    length=len(list(filter(("").__ne__, length)))
    for j in range(length):
        frame=[]
        for i in row[columns]:
            i=i[1:-1].replace("\n", "").replace("  "," ").split(" ")
            i=list(filter(("").__ne__, i))
            frame.append(float(i[j]))
        if len(result)!=0:
            result=np.vstack((result, frame))
        else:
            result=np.array(frame)
    with open("./landmarks/"+str(index)+name+'.npy', 'wb') as f:
        np.save(f, result)
    with open("./text/"+str(index)+name+".txt",'w') as f:
        print(row["sentence"])
        f.write(row["sentence"])
    if index==0:
        with open("test.txt","w") as f:
            f.write(str(index)+name+"\n")
    else:
        with open("test.txt","a") as f:
            f.write(str(index)+name+"\n")


for index, row in valTable.iterrows():
    name=get_random_string(20)
    #print(row[columns])
    result=np.array([])
    length=row["RIGHT_WRIST_X"][1:-1].replace("\n", "").replace("  "," ").split(" ")
    length=len(list(filter(("").__ne__, length)))
    for j in range(length):
        frame=[]
        for i in row[columns]:
            i=i[1:-1].replace("\n", "").replace("  "," ").split(" ")
            i=list(filter(("").__ne__, i))
            frame.append(float(i[j]))
        if len(result)!=0:
            result=np.vstack((result, frame))
        else:
            result=np.array(frame)
    with open("./landmarks/"+str(index)+name+'.npy', 'wb') as f:
        np.save(f, result)
    with open("./text/"+str(index)+name+".txt",'w') as f:
        print(row["sentence"])
        f.write(row["sentence"])
    if index==0:
        with open("val.txt","w") as f:
            f.write(str(index)+name+"\n")
    else:
        with open("val.txt","a") as f:
            f.write(str(index)+name+"\n")

