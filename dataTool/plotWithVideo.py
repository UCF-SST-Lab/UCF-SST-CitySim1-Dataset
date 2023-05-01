# Ou Zheng
# 04/04/2022
import cv2
import numpy as np
import pandas as pd
# please put csv and video file in the same folder

#===============user input=================================
fileName="ExpresswayA3.mp4"
carID=2249
#========================================================
rawData = pd.read_csv("fix_"+fileName[:-4]+'withGPS.csv')
cap = cv2.VideoCapture(fileName)
currentData=rawData[rawData['carID']==carID]
print(currentData.head())
counter=1
ret, frame = cap.read()
displayFrame=frame
for index, row in currentData.iterrows():
  # bounding box
  cv2.circle(displayFrame,(int(row['boundingBox1X']),int(row['boundingBox1Y'])), 2, (0,0,255), 2)
  cv2.circle(displayFrame,(int(row['boundingBox2X']),int(row['boundingBox2Y'])), 2, (0,0,255), 2)
  cv2.circle(displayFrame,(int(row['boundingBox3X']),int(row['boundingBox3Y'])), 2, (0,0,255), 2)
  #car center
  cv2.circle(displayFrame,(int(row['boundingBox4X']),int(row['boundingBox4Y'])), 2, (0,0,255), 2)
  cv2.circle(displayFrame,(int(row['carCenterX']),int(row['carCenterY'])), 2, (0,255,0), 2)
cv2.imshow('displayFrame',displayFrame)
cv2.waitKey(0) 
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
