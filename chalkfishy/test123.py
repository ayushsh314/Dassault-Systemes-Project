# Python
# import libraries
import datetime
from picamera import PiCamera

import time
import os
# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.


import cv2
import numpy as np
thres = 0.45  # Threshold to detect object
nms_threshold = 0.2
cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,150)

classNames = []
#classFile = 'coco.names'
classFile = 'classes.names'
# with open(classFile,'rt') as f:
#     classNames = f.read().rstrip('n').split('n')
with open(classFile, 'rt') as f:
    classNames = [line.rstrip() for line in f]


# print(classNames)
configPath = 'yolov3_custom.cfg'
weightsPath = 'yolov3_custom_2000.weights'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)




prev = ''
while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    # print(classIds," ",confs," ",bbox)
    bbox = list(bbox)
    # print(bbox)
    confs = list(np.array(confs).reshape(1, -1)[0])
    confs = list(map(float, confs))
    # print(type(confs[0]))
    # print(" ss ",confs)
    # if(confs[0]<0.6):
    #     continue

    indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)
    # print(objectsss[indices[0][0]])
    # print(objectsss[indices])

    text = ''
    for i in indices:
        # print(objectsss[i])
        i= 1*(i == 0) + i*(i != 0 )
        # print(objectsss[i]," " ,confs[0])

   

        box = bbox[i-1]
        # print(box)
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x+w, h+y), color=(0, 255, 0), thickness=2)
        cv2.putText(img, classNames[classIds[i-1]-1].upper(), (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        # print(classNames[classIds[i][0]-1].upper())

        # converting text sample to audio

        text += 'There is a ' + classNames[classIds[i-1]-1].upper()+' '
        print(text)
        # text+=classNames[classIds[i][0]-1].upper()+' '

  


    cv2.imshow("Output", img)
    cv2.waitKey(1)


