import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import numpy as np
import skimage.transform as sktr
from scipy import ndimage
import skimage
# from scipy.ndimage.filters import gaussian_filter, uniform_filter
import sys

im = plt.imread('./images/buildings.jpg')/255.
# get 2 points
# plt.imshow(im)
# pts = plt.ginput(2)
# plt.close()
# pts = [x[::-1] for x in pts]

    
for thresh in range(25, 500, 15):
    # blur image
    imblur = skimage.filters.gaussian_filter(im, sigma = 1.0)

    # unblur if distance from line is < thresh
    rr, cc = np.meshgrid(np.arange(im.shape[0]), np.arange(im.shape[1]))
    rr = rr.flatten().astype(int)
    cc = cc.flatten().astype(int)
    vector = np.ones([2, len(rr)]).astype(int)
    vector[0] = rr
    vector[1] = cc
    valid = abs(vector[0]-250) < thresh
    valid = np.array(valid).reshape(-1)
    rr = rr[valid]
    cc = cc[valid]
    vector = vector[:, valid]
    imblur[rr, cc] = im[vector[0], vector[1]]
    print thresh 
    im = imblur

plt.imshow(im)
plt.show()
