import numpy as np
import pandas as  pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as mplcm
import matplotlib.colors as colors
import numpy as np
from math import hypot,atan2
from celluloid import Camera


NUM_COLORS = 19

cm = plt.get_cmap('gist_rainbow')
color=[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]


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

#data=np.load("/home/n12i/Downloads/test_sample.npy")
data=np.load("./landmarks/0tgdbdervllmhwpvxpgtn.npy")
df = pd.DataFrame(data, columns = columns)
df=(df-1)*-1
print(df)

bodyDic={}
bodyDic["RIGHT_THUMB"]={"start":[df["RIGHT_THUMB_TIP_X"],df["RIGHT_THUMB_TIP_Y"]],"end":[df["RIGHT_WRIST_X"],df["RIGHT_WRIST_Y"]]}
bodyDic["RIGHT_INDEX"]={"start":[df["RIGHT_INDEX_FINGER_TIP_X"],df["RIGHT_INDEX_FINGER_TIP_Y"]],"end":[df["RIGHT_WRIST_X"],df["RIGHT_WRIST_Y"]]}
bodyDic["RIGHT_MIDDLE"]={"start":[df["RIGHT_MIDDLE_FINGER_TIP_X"],df["RIGHT_MIDDLE_FINGER_TIP_Y"]],"end":[df["RIGHT_WRIST_X"],df["RIGHT_WRIST_Y"]]}
bodyDic["RIGHT_RING"]={"start":[df["RIGHT_RING_FINGER_TIP_X"],df["RIGHT_RING_FINGER_TIP_Y"]],"end":[df["RIGHT_WRIST_X"],df["RIGHT_WRIST_Y"]]}
bodyDic["RIGHT_PINKY"]={"start":[df["RIGHT_PINKY_TIP_X"],df["RIGHT_PINKY_TIP_Y"]],"end":[df["RIGHT_WRIST_X"],df["RIGHT_WRIST_Y"]]}
bodyDic["LEFT_THUMB"]={"start":[df["LEFT_THUMB_TIP_X"],df["LEFT_THUMB_TIP_Y"]],"end":[df["LEFT_WRIST_X"],df["LEFT_WRIST_Y"]]}
bodyDic["LEFT_INDEX"]={"start":[df["LEFT_INDEX_FINGER_TIP_X"],df["LEFT_INDEX_FINGER_TIP_Y"]],"end":[df["LEFT_WRIST_X"],df["LEFT_WRIST_Y"]]}
bodyDic["LEFT_MIDDLE"]={"start":[df["LEFT_MIDDLE_FINGER_TIP_X"],df["LEFT_MIDDLE_FINGER_TIP_Y"]],"end":[df["LEFT_WRIST_X"],df["LEFT_WRIST_Y"]]}
bodyDic["LEFT_RING"]={"start":[df["LEFT_RING_FINGER_TIP_X"],df["LEFT_RING_FINGER_TIP_Y"]],"end":[df["LEFT_WRIST_X"],df["LEFT_WRIST_Y"]]}
bodyDic["LEFT_PINKY"]={"start":[df["LEFT_PINKY_TIP_X"],df["LEFT_PINKY_TIP_Y"]],"end":[df["LEFT_WRIST_X"],df["LEFT_WRIST_Y"]]}
bodyDic["RIGHT_FOREARM"]={"start":[df["RIGHT_WRIST_X"],df["RIGHT_WRIST_Y"]],"end":[df["RIGHT_ELBOW_X"],df["RIGHT_ELBOW_Y"]]}
bodyDic["LEFT_FOREARM"]={"start":[df["LEFT_WRIST_X"],df["LEFT_WRIST_Y"]],"end":[df["LEFT_ELBOW_X"],df["LEFT_ELBOW_Y"]]}
bodyDic["RIGHT_UPPERARM"]={"start":[df["RIGHT_ELBOW_X"],df["RIGHT_ELBOW_Y"]],"end":[df["RIGHT_SHOULDER_X"],df["RIGHT_SHOULDER_Y"]]}
bodyDic["LEFT_UPPERARM"]={"start":[df["LEFT_ELBOW_X"],df["LEFT_ELBOW_Y"]],"end":[df["LEFT_SHOULDER_X"],df["LEFT_SHOULDER_Y"]]}
bodyDic["CHEST"]={"start":[df["LEFT_SHOULDER_X"],df["LEFT_SHOULDER_Y"]],"end":[df["RIGHT_SHOULDER_X"],df["RIGHT_SHOULDER_Y"]]}
bodyDic["NOSE"]={"start":[df["NOSE_X"],df["NOSE_Y"]],"end":[df["NOSE_X"],df["NOSE_Y"]+.01]}
bodyDic["RIGHT_EAR"]={"start":[df["RIGHT_EAR_X"],df["RIGHT_EAR_Y"]],"end":[df["RIGHT_EAR_X"],df["RIGHT_EAR_Y"]+.01]}
bodyDic["LEFT_EAR"]={"start":[df["LEFT_EAR_X"],df["LEFT_EAR_Y"]],"end":[df["LEFT_EAR_X"],df["LEFT_EAR_Y"]+.01]}
bodyDic["MOUTH"]={"start":[df["MOUTH_RIGHT_X"],df["MOUTH_RIGHT_Y"]],"end":[df["MOUTH_LEFT_X"],df["MOUTH_LEFT_Y"]+.01]}

for part in bodyDic:
    lengths=[]
    angles=[]
    for i in range(len(bodyDic[part]["start"][0])):
        lengths.append(hypot(bodyDic[part]["start"][0][i]-bodyDic[part]["end"][0][i],bodyDic[part]["start"][1][i]-bodyDic[part]["end"][1][i]))
        angles.append(atan2(bodyDic[part]["start"][1][i]-bodyDic[part]["end"][1][i], bodyDic[part]["start"][0][i]-bodyDic[part]["end"][0][i]))
    bodyDic[part]["length"]=lengths
    bodyDic[part]["angle"]=angles

fig=plt.figure()
camera=Camera(fig)
for i in range(len(bodyDic["MOUTH"]["start"][0])):
    count=0
    for part in bodyDic:
        plt.plot([bodyDic[part]["start"][0][i],bodyDic[part]["end"][0][i]],
                 [bodyDic[part]["start"][1][i],bodyDic[part]["end"][1][i]],
                 color=color[count])
        plt.xlim(0,1)
        plt.ylim(0,1)
        count+=1
    camera.snap()
animation = camera.animate(interval=200,blit=True)
animation.save(
    'simpleActual.mp4',
    dpi=100
)