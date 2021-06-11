from os import path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = '/home/mrunal/Documents/Python Scripts/REPORT/csv/'

#files = ['AGAST_BF.csv','AGAST_FLANN.csv','AKAZE_BF.csv','AKAZE_FLANN.csv','BRISK_BF.csv','BRISK_FLANN.csv','FAST_BF.csv','FAST_FLANN.csv',
#         'GFTT_BF.csv','GFTT_FLANN.csv','MSER_BF.csv','MSER_FLANN.csv','ORB_BF.csv','ORB_FLANN.csv','SIFT_BF.csv','SIFT_FLANN.csv']

#files = ['AGAST_BF.csv','AKAZE_BF.csv','BRISK_BF.csv','FAST_BF.csv',
#         'GFTT_BF.csv','MSER_BF.csv','ORB_BF.csv','SIFT_BF.csv']

#files = ['AGAST_FLANN.csv','AKAZE_FLANN.csv','BRISK_FLANN.csv','FAST_FLANN.csv',
#         'GFTT_FLANN.csv','MSER_FLANN.csv','ORB_FLANN.csv','SIFT_FLANN.csv']

files = ['SIFT_BF.csv','SIFT_FLANN.csv']

#fnames = ['agast_bf','agast_flann','akaze_bf','akaze_flann','brisk_bf','brisk_flann','fast_bf','fast_flann',
#          'gftt_bf','gftt_flann','maser_bf','mser_flann','orb_bf','orb_flann','sift_bf','sift_flann']

#fnames = ['agast_bf','akaze_bf','brisk_bf','fast_bf',
#          'gftt_bf','maser_bf','orb_bf','sift_bf']

#fnames = ['agast_flann','akaze_flann','brisk_flann','fast_flann',
#          'gftt_flann','mser_flann','orb_flann','sift_flann']

fnames = ['sift_bf','sift_flann']

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

for i in range(0,len(fnames)):
    data = pd.read_csv(path+files[i])
    x = np.array(data.iloc(1)[0])
    y = np.array(data.iloc(1)[1])
    plt.plot(x,y,label=fnames[i])

plt.xlabel("Execution Time")
plt.ylabel("FPS")
plt.legend()
plt.show()


