#ou zheng
#04062022
#This is for expressway

import pandas as pd
import csv

import numpy as np
import cv2
#====================================user input===================
inputName='./ExpresswayA.csv'
zones=np.load("./ExpresswayALane.npy",allow_pickle=True)
#====================================user input===================
outputNme=inputName[:-4]+"withLane.csv"
df = pd.read_csv(inputName)
rawData = pd.read_csv(inputName)

with open(outputNme, 'w', newline='') as csvfile2:
	spamwriter = csv.writer(csvfile2)
	with open(inputName, newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		counter=0
		for row in spamreader:
			print(counter)
			if counter ==0:
				row.append("laneNumber")
				counter+=1
				spamwriter.writerow(row)
				continue;
			laneNumber=-1
			print(row)
			for i in range(len(zones)):
				print(row[10])
				print(row[11])
				result = cv2.pointPolygonTest(zones[i], (int(row[10]),int(row[11])), False)
				if result==1 :
					laneNumber=i
					print(str(result)+"|"+str(i))
		
			row.append(str(laneNumber))   
			counter+=1
			spamwriter.writerow(row)
