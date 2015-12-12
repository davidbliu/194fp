import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import numpy as np
import skimage.transform as sktr
from scipy import ndimage
import skimage
# from scipy.ndimage.filters import gaussian_filter, uniform_filter
import sys

IMNAME = 'mall'
im = plt.imread('./images/' + IMNAME + '.jpg')/255.


mallDists = range(25, 500, 3)
mallThresh = 275

buildingDists = range(50, 500, 10)
buildingThresh = 500

DISTS = mallDists
THRESH = mallThresh

for thresh in DISTS:
    # blur image
    imblur = skimage.filters.gaussian_filter(im, sigma = 0.5)

    # unblur if distance from line is < thresh
    rr, cc = np.meshgrid(np.arange(im.shape[0]), np.arange(im.shape[1]))
    rr = rr.flatten().astype(int)
    cc = cc.flatten().astype(int)
    vector = np.ones([2, len(rr)]).astype(int)
    vector[0] = rr
    vector[1] = cc
    valid = abs(vector[0]-THRESH) < thresh
    valid = np.array(valid).reshape(-1)
    rr = rr[valid]
    cc = cc[valid]
    vector = vector[:, valid]
    imblur[rr, cc] = im[vector[0], vector[1]]
    print thresh 
    im = imblur

plt.imsave('./results/'+IMNAME+'.png', im)
plt.imshow(im)
plt.show()
