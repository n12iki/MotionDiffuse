import os
import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# assign directory
directory = "/home/n12i/Desktop/french/annotations/csv/translation"
 
# iterate over files in
# that directory
maxTime=0
differece=[]
files = [f for f in os.listdir(directory) if f[-4:]==".csv"]
for filename in files:
    #print(filename)
    table=pd.read_csv(directory+"/"+filename,delimiter=",",)
    #print(table["gloss"])
    diff=(table["end"]-table["start"])*50/1000
    diffInd=np.where(diff>500)
    for i in diffInd[0]:
        start=table.iloc[i]["start"]
        end=table.iloc[i]["end"]
        tableR=pd.read_csv("/home/n12i/Desktop/french/annotations/csv/right/"+filename,delimiter=",",)
        tableL=pd.read_csv("/home/n12i/Desktop/french/annotations/csv/left/"+filename,delimiter=",",)
        filter1R=tableR["start"]>=start 
        filter2R=tableR["end"]<=end
        filter1L=tableL["start"]>=start 
        filter2L=tableL["end"]<=end
        tableR.drop(tableR.index[filter1R & filter2R].tolist(), axis=0, inplace=True)
        tableL.drop(tableL.index[filter1L & filter2L].tolist(), axis=0, inplace=True)
    if len(diffInd[0])>0: 
        tableH=pd.read_csv("/home/n12i/Desktop/french/features/landmarks/hands/"+filename,delimiter=",",)
        tableP=pd.read_csv("/home/n12i/Desktop/french/features/landmarks/pose/"+filename,delimiter=",",)
        tableH=tableH[["RIGHT_WRIST_X","RIGHT_WRIST_Y","RIGHT_THUMB_TIP_X","RIGHT_THUMB_TIP_Y",
                      "RIGHT_INDEX_FINGER_TIP_X","RIGHT_INDEX_FINGER_TIP_Y","RIGHT_MIDDLE_FINGER_TIP_X",
                      "RIGHT_MIDDLE_FINGER_TIP_Y","RIGHT_RING_FINGER_TIP_X","RIGHT_RING_FINGER_TIP_Y",
                      "RIGHT_PINKY_TIP_X","RIGHT_PINKY_TIP_Y","LEFT_WRIST_X","LEFT_WRIST_Y",
                      "LEFT_THUMB_TIP_X","LEFT_THUMB_TIP_Y","LEFT_INDEX_FINGER_TIP_X","LEFT_INDEX_FINGER_TIP_Y",
                      "LEFT_MIDDLE_FINGER_TIP_X","LEFT_MIDDLE_FINGER_TIP_Y","LEFT_RING_FINGER_TIP_X",
                      "LEFT_RING_FINGER_TIP_Y","LEFT_PINKY_TIP_X","LEFT_PINKY_TIP_Y"]]
        tableP=tableP[["NOSE_X","NOSE_Y","LEFT_EAR_X","LEFT_EAR_Y","RIGHT_EAR_X","RIGHT_EAR_Y","MOUTH_LEFT_X",
                       "MOUTH_LEFT_Y","MOUTH_RIGHT_X","MOUTH_RIGHT_Y","LEFT_SHOULDER_X","LEFT_SHOULDER_Y",
                       "RIGHT_SHOULDER_X","RIGHT_SHOULDER_Y","LEFT_ELBOW_X","LEFT_ELBOW_Y",
                       "RIGHT_ELBOW_X","RIGHT_ELBOW_Y"]]
        final= pd.concat([tableP, tableH], axis=1)
        table.drop(diffInd[0],inplace=True)
        try:
            os.mkdir("/home/n12i/Desktop/french/features/landmarks/clean/")
            os.mkdir("/home/n12i/Desktop/french/annotations/csv/right/clean/")
            os.mkdir("/home/n12i/Desktop/french/annotations/csv/left/clean/")
            os.mkdir("/home/n12i/Desktop/french/annotations/csv/translation/clean/")
        except:
            pass
        final.to_csv("/home/n12i/Desktop/french/features/landmarks/clean/"+filename,index=False)
        tableR.to_csv("/home/n12i/Desktop/french/annotations/csv/right/clean/"+filename,index=False)
        tableL.to_csv("/home/n12i/Desktop/french/annotations/csv/left/clean/"+filename,index=False)
        table.to_csv("/home/n12i/Desktop/french/annotations/csv/translation/clean/"+filename,index=False)

    #with open(directory+"/"+filename, newline='') as csvfile:
    #    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #    for row in spamreader:
    #        if(len(row)>0):
    #            if(row[0].isdigit()):
    #                differece.append(int(row[1])-int(row[0]))
    #                if maxTime<int(row[1])-int(row[0]):
    #                    maxTime=int(row[1])-int(row[0])
#print(maxTime/50)

#differece=np.array(differece)*50.0/1000

# Creating histogram
#fig, ax = plt.subplots(figsize =(10, 7))
#ax.hist(differece, bins = np.arange(0, 3500, 200, dtype=None))
 
# Show plot
plt.show()