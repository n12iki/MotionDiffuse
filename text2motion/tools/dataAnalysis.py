import os
import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter,OrderedDict
import re
# assign directory
directory = "/home/n12i/Desktop/french/annotations/csv/translation/clean"
 
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
            words.append(s.split(" "))
    for index, row in tableR.iterrows():
        if not(pd.isna(row["gloss"])):
            wordsR.append(row["gloss"].split(" "))
    for index, row in tableL.iterrows():
        if not(pd.isna(row["gloss"])):
            wordsL.append(row["gloss"].split(" "))

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
simpleWordStatL=Counter({k: c for k, c in wordStatL.items() if c >= 50})
#print(simpleWordStatL)

simpleWordStatL = OrderedDict(simpleWordStatL.most_common())

plt.bar(simpleWordStatL.keys(), simpleWordStatL.values())
plt.xticks(rotation=90)

plt.show()

directory = "/home/n12i/Desktop/french/annotations/csv/translation/clean"
 
# iterate over files in
# that directory
sentences=[]
uniqueSentence=[]
wordLowerLimit=Counter({k: c for k, c in wordStat.items() if c >= 10})
files = [f for f in os.listdir(directory) if f[-4:]==".csv"]
for filename in files:
    #print(filename)
    table=pd.read_csv(directory+"/"+filename,delimiter=",",)
    #print(table["gloss"])
    diff=(table["end"]-table["start"])*50/1000
    diffInd=np.where(diff>500)
    for index, row in table.iterrows():
        if not(pd.isna(row["gloss"])):
            s=row["gloss"]
            s=re.sub(r'[^\w\s]','',s)
            sentence=s.split(" ")
            if all(elem in wordLowerLimit  for elem in sentence):
                sentences.append(sentence)
print(len(sentences))
print(len(set(tuple(row) for row in sentences)))
print(count)