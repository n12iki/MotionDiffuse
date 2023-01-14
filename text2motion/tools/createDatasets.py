import os
import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter,OrderedDict
import re
import stanza
# assign directory
directory = "/home/n12i/Desktop/french/annotations/csv/translation/clean"

nlp=stanza.Pipeline('fr')
# iterate over files in
# that directory
maxTime=0
differece=[]
files = [f for f in os.listdir(directory) if f[-4:]==".csv"]
words=[]
wordsR=[]
wordsL=[]
count=0
for filename in files:
    #print(filename)
    table=pd.read_csv(directory+"/"+filename,delimiter=",",)
    #print(table["gloss"])
    diff=(table["end"]-table["start"])*50/1000
    diffInd=np.where(diff>500)
    tableR=pd.read_csv("/home/n12i/Desktop/french/annotations/csv/right/clean/"+filename,delimiter=",",)
    tableL=pd.read_csv("/home/n12i/Desktop/french/annotations/csv/left/clean/"+filename,delimiter=",",)
    for index, row in table.iterrows():
        if not(pd.isna(row["gloss"])):
            s=row["gloss"]
            count+=1
            s=re.sub(r'[^\w\s]','',s)
            s=(s.lower()).split(" ")
            s=list(filter(('').__ne__, s))
            words.append(s)
    for index, row in tableR.iterrows():
        if not(pd.isna(row["gloss"])):
            wordsR.append((row["gloss"].lower()).split(" "))
    for index, row in tableL.iterrows():
        if not(pd.isna(row["gloss"])):
            wordsL.append((row["gloss"].lower()).split(" "))

plt.figure(0)    
words=[item for sublist in words for item in sublist]
wordStat=Counter(words)
simpleWordStat=Counter({k: c for k, c in wordStat.items() if c >= 100})
#print(simpleWordStat)

simpleWordStat = OrderedDict(simpleWordStat.most_common())

plt.bar(simpleWordStat.keys(), simpleWordStat.values())
plt.xticks(rotation=90)

plt.figure(1)
wordsR=[item for sublist in wordsR for item in sublist]
wordStatR=Counter(wordsR)
simpleWordStatR=Counter({k: c for k, c in wordStatR.items() if c >= 100})
#print(simpleWordStatR)

simpleWordStatR = OrderedDict(simpleWordStatR.most_common())

plt.bar(simpleWordStatR.keys(), simpleWordStatR.values())
plt.xticks(rotation=90)

plt.figure(2)
wordsL=[item for sublist in wordsL for item in sublist]
wordStatL=Counter(wordsL)
simpleWordStatL=Counter({k: c for k, c in wordStatL.items() if c >= 100})
#print(simpleWordStatL)

simpleWordStatL = OrderedDict(simpleWordStatL.most_common())

plt.bar(simpleWordStatL.keys(), simpleWordStatL.values())
plt.xticks(rotation=90)

plt.show()

directory = "/home/n12i/Desktop/french/annotations/csv/translation/clean"
 
# iterate over files in
# that directory
sentenceMatch=[]
uniqueSentence=[]
wordLowerLimit=Counter({k: c for k, c in wordStat.items() if c >= 10})
files = [f for f in os.listdir(directory) if f[-4:]==".csv"]
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
testTable=pd.DataFrame(columns=["sentence","RIGHT_WRIST_X","RIGHT_WRIST_Y","RIGHT_THUMB_TIP_X","RIGHT_THUMB_TIP_Y",
                      "RIGHT_INDEX_FINGER_TIP_X","RIGHT_INDEX_FINGER_TIP_Y","RIGHT_MIDDLE_FINGER_TIP_X",
                      "RIGHT_MIDDLE_FINGER_TIP_Y","RIGHT_RING_FINGER_TIP_X","RIGHT_RING_FINGER_TIP_Y",
                      "RIGHT_PINKY_TIP_X","RIGHT_PINKY_TIP_Y","LEFT_WRIST_X","LEFT_WRIST_Y",
                      "LEFT_THUMB_TIP_X","LEFT_THUMB_TIP_Y","LEFT_INDEX_FINGER_TIP_X","LEFT_INDEX_FINGER_TIP_Y",
                      "LEFT_MIDDLE_FINGER_TIP_X","LEFT_MIDDLE_FINGER_TIP_Y","LEFT_RING_FINGER_TIP_X",
                      "LEFT_RING_FINGER_TIP_Y","LEFT_PINKY_TIP_X","LEFT_PINKY_TIP_Y","NOSE_X","NOSE_Y","LEFT_EAR_X",
                      "LEFT_EAR_Y","RIGHT_EAR_X","RIGHT_EAR_Y","MOUTH_LEFT_X","MOUTH_LEFT_Y","MOUTH_RIGHT_X","MOUTH_RIGHT_Y",
                      "LEFT_SHOULDER_X","LEFT_SHOULDER_Y","RIGHT_SHOULDER_X","RIGHT_SHOULDER_Y","LEFT_ELBOW_X","LEFT_ELBOW_Y",
                      "RIGHT_ELBOW_X","RIGHT_ELBOW_Y"
                      ])
trainTable=pd.DataFrame(columns=["sentence","RIGHT_WRIST_X","RIGHT_WRIST_Y","RIGHT_THUMB_TIP_X","RIGHT_THUMB_TIP_Y",
                      "RIGHT_INDEX_FINGER_TIP_X","RIGHT_INDEX_FINGER_TIP_Y","RIGHT_MIDDLE_FINGER_TIP_X",
                      "RIGHT_MIDDLE_FINGER_TIP_Y","RIGHT_RING_FINGER_TIP_X","RIGHT_RING_FINGER_TIP_Y",
                      "RIGHT_PINKY_TIP_X","RIGHT_PINKY_TIP_Y","LEFT_WRIST_X","LEFT_WRIST_Y",
                      "LEFT_THUMB_TIP_X","LEFT_THUMB_TIP_Y","LEFT_INDEX_FINGER_TIP_X","LEFT_INDEX_FINGER_TIP_Y",
                      "LEFT_MIDDLE_FINGER_TIP_X","LEFT_MIDDLE_FINGER_TIP_Y","LEFT_RING_FINGER_TIP_X",
                      "LEFT_RING_FINGER_TIP_Y","LEFT_PINKY_TIP_X","LEFT_PINKY_TIP_Y","NOSE_X","NOSE_Y","LEFT_EAR_X",
                      "LEFT_EAR_Y","RIGHT_EAR_X","RIGHT_EAR_Y","MOUTH_LEFT_X","MOUTH_LEFT_Y","MOUTH_RIGHT_X","MOUTH_RIGHT_Y",
                      "LEFT_SHOULDER_X","LEFT_SHOULDER_Y","RIGHT_SHOULDER_X","RIGHT_SHOULDER_Y","LEFT_ELBOW_X","LEFT_ELBOW_Y",
                      "RIGHT_ELBOW_X","RIGHT_ELBOW_Y"
                      ])

valTable=pd.DataFrame(columns=["sentence","RIGHT_WRIST_X","RIGHT_WRIST_Y","RIGHT_THUMB_TIP_X","RIGHT_THUMB_TIP_Y",
                      "RIGHT_INDEX_FINGER_TIP_X","RIGHT_INDEX_FINGER_TIP_Y","RIGHT_MIDDLE_FINGER_TIP_X",
                      "RIGHT_MIDDLE_FINGER_TIP_Y","RIGHT_RING_FINGER_TIP_X","RIGHT_RING_FINGER_TIP_Y",
                      "RIGHT_PINKY_TIP_X","RIGHT_PINKY_TIP_Y","LEFT_WRIST_X","LEFT_WRIST_Y",
                      "LEFT_THUMB_TIP_X","LEFT_THUMB_TIP_Y","LEFT_INDEX_FINGER_TIP_X","LEFT_INDEX_FINGER_TIP_Y",
                      "LEFT_MIDDLE_FINGER_TIP_X","LEFT_MIDDLE_FINGER_TIP_Y","LEFT_RING_FINGER_TIP_X",
                      "LEFT_RING_FINGER_TIP_Y","LEFT_PINKY_TIP_X","LEFT_PINKY_TIP_Y","NOSE_X","NOSE_Y","LEFT_EAR_X",
                      "LEFT_EAR_Y","RIGHT_EAR_X","RIGHT_EAR_Y","MOUTH_LEFT_X","MOUTH_LEFT_Y","MOUTH_RIGHT_X","MOUTH_RIGHT_Y",
                      "LEFT_SHOULDER_X","LEFT_SHOULDER_Y","RIGHT_SHOULDER_X","RIGHT_SHOULDER_Y","LEFT_ELBOW_X","LEFT_ELBOW_Y",
                      "RIGHT_ELBOW_X","RIGHT_ELBOW_Y"
                      ])

for filename in files:
    print(filename)
    tableLand=pd.read_csv("/home/n12i/Desktop/french/features/landmarks/clean/"+filename,delimiter=",",)
    table=pd.read_csv(directory+"/"+filename,delimiter=",",)
    #print(table["gloss"])
    diff=(table["end"]-table["start"])*50/1000
    diffInd=np.where(diff>500)
    for index, row in table.iterrows():
        if not(pd.isna(row["gloss"])):
            flag=0
            for i in columns:
                if any(np.isnan(np.array(tableLand[i]))):
                    flag=1
            if flag==0:
                s=row["gloss"]
                s=re.sub(r'[^\w\s]','',s)
                s=(s.lower()).split(" ")
                sentenceList=list(filter(('').__ne__, s))
                sentence=" ".join(list(filter(('').__ne__, s)))
                doc = nlp(sentence)
                sentence=  sentence+"#"
                for phrase in doc.sentences:
                    for word in phrase.words:
                        sentence= sentence+str(word.lemma)+"/"+str(word.pos)+" "
                sentence=sentence[:-1]+"#0.0#0.0"
                skip=0
                start=int(row["start"]*50/1000)
                if start==0:
                    start=1
                end=int(row["end"]*50/1000)
                inRow=[sentence,np.array(tableLand["RIGHT_WRIST_X"][start-1:end]),np.array(tableLand["RIGHT_WRIST_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_THUMB_TIP_X"][start-1:end]),np.array(tableLand["RIGHT_THUMB_TIP_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_INDEX_FINGER_TIP_X"][start-1:end]),np.array(tableLand["RIGHT_INDEX_FINGER_TIP_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_MIDDLE_FINGER_TIP_X"][start-1:end]),np.array(tableLand["RIGHT_MIDDLE_FINGER_TIP_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_RING_FINGER_TIP_X"][start-1:end]),np.array(tableLand["RIGHT_RING_FINGER_TIP_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_PINKY_TIP_X"][start-1:end]),np.array(tableLand["RIGHT_PINKY_TIP_Y"][start-1:end]),
                       np.array(tableLand["LEFT_WRIST_X"][start-1:end]),np.array(tableLand["LEFT_WRIST_Y"][start-1:end]),
                       np.array(tableLand["LEFT_THUMB_TIP_X"][start-1:end]),np.array(tableLand["LEFT_THUMB_TIP_Y"][start-1:end]),
                       np.array(tableLand["LEFT_INDEX_FINGER_TIP_X"][start-1:end]),np.array(tableLand["LEFT_INDEX_FINGER_TIP_Y"][start-1:end]),
                       np.array(tableLand["LEFT_MIDDLE_FINGER_TIP_X"][start-1:end]),np.array(tableLand["LEFT_MIDDLE_FINGER_TIP_Y"][start-1:end]),
                       np.array(tableLand["LEFT_RING_FINGER_TIP_X"][start-1:end]),np.array(tableLand["LEFT_RING_FINGER_TIP_Y"][start-1:end]),
                       np.array(tableLand["LEFT_PINKY_TIP_X"][start-1:end]),np.array(tableLand["LEFT_PINKY_TIP_Y"][start-1:end]),
                       np.array(tableLand["NOSE_X"][start-1:end]),np.array(tableLand["NOSE_Y"][start-1:end]),
                       np.array(tableLand["LEFT_EAR_X"][start-1:end]),np.array(tableLand["LEFT_EAR_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_EAR_X"][start-1:end]),np.array(tableLand["RIGHT_EAR_Y"][start-1:end]),
                       np.array(tableLand["MOUTH_LEFT_X"][start-1:end]),np.array(tableLand["MOUTH_LEFT_Y"][start-1:end]),
                       np.array(tableLand["MOUTH_RIGHT_X"][start-1:end]),np.array(tableLand["MOUTH_RIGHT_Y"][start-1:end]),
                       np.array(tableLand["LEFT_SHOULDER_X"][start-1:end]),np.array(tableLand["LEFT_SHOULDER_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_SHOULDER_X"][start-1:end]),np.array(tableLand["RIGHT_SHOULDER_Y"][start-1:end]),
                       np.array(tableLand["LEFT_ELBOW_X"][start-1:end]),np.array(tableLand["LEFT_ELBOW_Y"][start-1:end]),
                       np.array(tableLand["RIGHT_ELBOW_X"][start-1:end]),np.array(tableLand["RIGHT_ELBOW_Y"][start-1:end])]

                if all(elem in wordLowerLimit  for elem in sentenceList):
                    skip=1
                    if not(sentence in sentenceMatch):
                        if(len(testTable)<=150):
                            testTable.loc[len(testTable.index)] = inRow
                        else:
                            valTable.loc[len(valTable.index)] = inRow
                        sentenceMatch.append(sentence)
                if skip==0:
                    trainTable.loc[len(trainTable.index)] = inRow
try:
    os.mkdir("/home/n12i/Desktop/french/final")
except:
    pass
trainTable.to_csv("/home/n12i/Desktop/french/final/train.csv",index=False)                    
testTable.to_csv("/home/n12i/Desktop/french/final/test.csv",index=False)
valTable.to_csv("/home/n12i/Desktop/french/final/val.csv",index=False)


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