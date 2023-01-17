import json
import numpy as np
with open("/home/n12i/Output/non_weighted_MSE_Motion.json") as json_file:
  testSet=json.load(json_file)

for i in testSet:
  input=i.split("#")[0]
  length=testSet[i]["length"]
  filePath=testSet[i]["file"]
  predicted=np.array(testSet[i]["output"])
  output=np.load("/home/n12i/Desktop/french/PositionalData/landmarks/"+filePath+".npy")
  print(predicted.shape)
  print(output.shape)

  print("\n")


print(input)
print(length)
print(filePath)
print(predicted.shape)
