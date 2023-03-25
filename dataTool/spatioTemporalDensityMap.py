# Ou Zheng
# 04/04/2022
import cv2
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def heatmap2d(arr: np.ndarray,xMax):
	fig = plt.figure(figsize=(8, 6))
	plt.xlabel('time gap:'+str(timeGap)+"s")
	plt.ylabel('time gap:'+str(distanceGap)+"feet")
	plt.xlim(0, xMax)
	plt.imshow(arr, cmap='viridis')
	plt.colorbar()
	plt.show()
# please put csv and video file in the same folder
#===============user input=================================
fileName="background.png"
rawData = pd.read_csv('FreewayB-01.csv')
# in second
timeGap=1
fps=30
# in feet
distanceGap=20
pix2meter=0.1565451082
meter2feet=3.2808399
font = cv2.FONT_HERSHEY_SIMPLEX
#===============user input=================================
frameGap=timeGap*fps
img = cv2.imread(fileName)
height, width, channels = img.shape
xMax=width
startCarID = rawData.loc[0, 'carId']
maxFramenum= rawData.loc[rawData.index[-1], 'frameNum']
maxCarID=rawData.loc[rawData.index[-1], 'carId']
yMax=int((xMax*pix2meter*meter2feet) /distanceGap)+1
xMax=int(maxFramenum/frameGap)+1
finalOutArray = np.zeros((yMax,xMax))

while True:
	print(startCarID,"|",maxCarID)
	if(startCarID>maxCarID):
		print(finalOutArray)
		heatmap2d(finalOutArray,xMax)
		break
	currentData=rawData[rawData['carId']==startCarID]
	for index, row in currentData.iterrows():
		#=======================upper flow===================
		if(int(row['laneId'])>2):
			continue
		currentTimeSlot=int(row['frameNum']/frameGap)
		currentDistance=int((int(row['carCenterX']))*pix2meter*meter2feet /distanceGap)
		finalOutArray[currentDistance,currentTimeSlot]+=1
		#=======================bottom flow===================
		# if(int(row['laneId'])<3):
		# 	continue
		# currentTimeSlot=int(row['frameNum']/frameGap)
		# currentDistance=int((xMax-int(row['carCenterX']))*pix2meter*meter2feet /distanceGap)
		# finalOutArray[currentDistance,currentTimeSlot]+=1
	startCarID+=1



