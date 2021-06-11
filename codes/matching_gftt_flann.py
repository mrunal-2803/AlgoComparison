import cv2
import numpy as np
import time

start_time = time.time()
t = []
kp_list = []
fkp_list = []
matches_list = []
fps_list = []
prev_frame_time = 0
new_frame_time = 0

cap = cv2.VideoCapture('/home/mrunal/Documents/Python Scripts/REPORT/sample.mov')
#create a Brute Force matcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#create an orb object
gftt = cv2.GFTTDetector_create()
orb = cv2.ORB_create()

#import all the required images
img = cv2.imread('/home/mrunal/Documents/Python Scripts/REPORT/book.jpg')


#convert them to grayscale
#this is required for future processes
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#get keypoints for each image using detect method using grayscale images
kp = gftt.detect(gray,None)
kp,des = orb.compute(gray,kp)

FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params,search_params)

while True:
    _,frame = cap.read()
    if frame is not None:
        frame = cv2.resize(frame,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)
        fgray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fkp = gftt.detect(fgray,None)
        fkp,fdes = orb.compute(fgray,fkp)
        matches = flann.match(des,fdes)
        matches = sorted(matches, key=lambda x:x.distance)
        fin = cv2.drawMatches(img, kp, frame, fkp, matches, frame, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        kp_list.append(len(kp))
        fkp_list.append(len(fkp))
        matches_list.append(len(matches))
        t.append(time.time() - start_time)
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        fps_list.append([time.time() - start_time,fps])
        cv2.imshow('WEBCAM', fin)
    else:
        break
    c = cv2.waitKey(1)
    if c == 27:
        break

""" print("Tinitial: %s"%t[0])    
print("Tfinal: %s"%(time.time() - start_time))
print('Average Train Image Keypoints: %d'%int(sum(kp_list)/len(kp_list)))
print('Average Test Image Keypoints: %d'%int(sum(fkp_list)/len(fkp_list)))
print('Average Matches: %d'%int(sum(matches_list)/len(matches_list)))
np.savetxt("GFTT_FLANN.csv", 
           fps_list,
           delimiter =", ", 
           fmt ='% s') """