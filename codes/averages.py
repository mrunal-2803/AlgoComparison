from os import path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = '/home/mrunal/Documents/Python Scripts/REPORT/csv/'

files = ['AGAST_BF.csv','AGAST_FLANN.csv','AKAZE_BF.csv','AKAZE_FLANN.csv','BRISK_BF.csv','BRISK_FLANN.csv','FAST_BF.csv','FAST_FLANN.csv',
         'GFTT_BF.csv','GFTT_FLANN.csv','MSER_BF.csv','MSER_FLANN.csv','ORB_BF.csv','ORB_FLANN.csv','SIFT_BF.csv','SIFT_FLANN.csv']

fnames = ['agast_bf','agast_flann','akaze_bf','akaze_flann','brisk_bf','brisk_flann','fast_bf','fast_flann',
          'gftt_bf','gftt_flann','maser_bf','mser_flann','orb_bf','orb_flann','sift_bf','sift_flann']

d = []

for i in range(0,len(files)):
    data = pd.read_csv(path+files[i])
    data = np.array(data.iloc(1)[1])
    data = sum(data)/len(data)
    d.append(data)

fig = plt.figure(figsize = (10, 5))

plt.bar(fnames, d, color ='maroon',
        width = 0.4)

plt.xlabel("Feature Trackers")
plt.ylabel("Avg FPS")
plt.show()