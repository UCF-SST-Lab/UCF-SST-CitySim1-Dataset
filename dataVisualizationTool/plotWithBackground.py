# # Ou Zheng
# # 04/04/2022
import cv2
import sys
import numpy as np
import pandas as pd
# please put csv and video file in the same folder
#===============user input=================================
rawData = pd.read_csv('ExpresswayA-01.csv')
carID=13
#========================================================
currentData=rawData[rawData['carId']==carID]
img = cv2.imread(cv2.samples.findFile("backgound.png"))
if img is None:
	sys.exit("Could not read the image.")
for index, row in currentData.iterrows():
  #plot bounding box 4 point
  cv2.circle(img,(int(row['boundingBox1X']),int(row['boundingBox1Y'])), 2, (0,0,255), 2)
  cv2.circle(img,(int(row['boundingBox2X']),int(row['boundingBox2Y'])), 2, (0,0,255), 2)
  cv2.circle(img,(int(row['boundingBox3X']),int(row['boundingBox3Y'])), 2, (0,0,255), 2)
  #plot car center
  cv2.circle(img,(int(row['boundingBox4X']),int(row['boundingBox4Y'])), 2, (0,0,255), 2)
  cv2.circle(img,(int(row['carCenterX']),int(row['carCenterY'])), 2, (0,255,0), 2)

cv2.imshow("Display window", img)
k = cv2.waitKey(0)
if k == ord("s"):
	cv2.imwrite("backgoundWihtPlot.png", img)