import numpy as np
import matplotlib.pyplot as plt

fnames = ['agast_bf','agast_flann','akaze_bf','akaze_flann','brisk_bf','brisk_flann','fast_bf','fast_flann',
          'gftt_bf','gftt_flann','maser_bf','mser_flann','orb_bf','orb_flann','sift_bf','sift_flann']

x = np.arange(16)

#y1 = [5191, 5191, 1887, 1887, 4212, 4212, 5138, 5138, 930, 930, 925, 925, 500, 500, 2041, 2041]
#y2 = [4950, 4950, 3060, 3060, 2740, 2740, 4902, 4902, 980, 980, 649, 649, 457, 457, 2676, 2676]
#y3 = [898, 5190, 1111, 1849, 1283, 4054, 921, 921, 227, 929, 52, 836, 163, 492, 971, 2041]

#y4 = [0.2893, 0.5009, 0.6232, 0.6468, 0.3053, 0.3422, 0.2742, 0.2770, 0.2604, 0.5162, 0.6945, 0.6411, 0.1774, 0.2047, 1.1199, 1.1107]

y5 = [152.6569, 115.6615, 184.4245, 169.8938, 107.8760, 100.4251, 147.6750, 147.3192, 49.6115, 55.1180, 147.8725, 151.4844, 32.9179, 35.3568, 379.5142, 245.7158]

#width = 0.2


#plt.bar(x-0.2, y1, width, color='cyan')
#plt.bar(x, y2, width, color='orange')
#plt.bar(x+0.2, y3, width, color='green')

#plt.bar(x, y4, color='brown')

plt.bar(x, y5, color='blue')



plt.xticks(x, fnames)
plt.xlabel("Features")
plt.ylabel("Values")
#plt.legend(["Tinitial"])
plt.show()