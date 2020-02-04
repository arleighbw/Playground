#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd
import numpy as np

from scipy import fftpack
from pathlib import Path

groundTruthPath = Path('feed_Data_Mining_Assign1Data\Data_Mining_Assign1Data\groundTruth')
myODataPath = Path('feed_Data_Mining_Assign1Data\Data_Mining_Assign1Data\MyoData')

gtDataPath= groundTruthPath / 'user10' / 'fork'
dataPath = myODataPath / 'user10'/ 'fork'

gtFiles = list(gtDataPath.glob("*.txt"))
dataFiles = list(dataPath.glob("*EMG.txt"))

gtData = np.genfromtxt(gtFiles[0], dtype=None, delimiter=',', usecols=(0,1))
myOData = np.genfromtxt(dataFiles[0], dtype=None, delimiter=',')


# In[116]:


myODataEatingIntervals = []
eatingDfs = []

for gTruth in data:
    #sampleRate conversion for EMG data
    startIndex = int(gTruth[0] * 100 / 30)
    endIndex = int(gTruth[1] * 100 / 30)
    
    #print("GroundTruth=" + str(gTruth[0]) + ":" + str(gTruth[1]) + " Start/End Index=" + str(startIndex) + ": " +str(endIndex))
    #save in list, start and end indices
    myODataEatingIntervals.append([startIndex, endIndex])
    
    #save eating data intervals
    eatingDfs.append(pd.DataFrame(myOData[startIndex:endIndex]))

#make pretty and plot in respect to TimeStamp
eatingDF = pd.concat(eatingDfs)
eatingDF.columns=['TimeStamp','EMG1','EMG2','EMG3','EMG4','EMG5','EMG6','EMG7','EMG8']
eatingDF.plot(x='TimeStamp')


# In[117]:


notEatingStart = 0
notEatingDfs = []

for interval in myODataEatingIntervals:
    notEatingEnd = interval[0]-1
    
    #print(str(notEatingStart) + " : " + str(notEatingEnd))
    
    notEatingDfs.append(pd.DataFrame(myOData[notEatingStart:notEatingEnd]))
    
    notEatingStart = interval[1]+1
    
## last interval, to end of myOData
notEatingDfs.append(pd.DataFrame(myOData[notEatingStart:]))    

#make pretty and plot in respect to TimeStamp
notEatingDF = pd.concat(notEatingDfs)
notEatingDF.columns=['TimeStamp','EMG1','EMG2','EMG3','EMG4','EMG5','EMG6','EMG7','EMG8']
notEatingDF.plot(x='TimeStamp')


# In[161]:


#stdDev = eatingDF.std()
#print(type(stdDev))

stdDeviations = [eatingDF.std()]
stdDeviations.append(notEatingDF.std())

print(type(stdDeviations[0][1:]))
print(stdDeviations[0])
print(stdDeviations[1])

pd.concat(stdDeviations, axis=1)[1:].plot()


# In[133]:


mean = eatingDF.mean()

print(mean)
mean[1:].plot()


# In[111]:


fft = fftpack.fft(eatingDF)
print(type(fft))
print(fft)

pd.DataFrame(fft)[1:].plot()


# In[ ]:




