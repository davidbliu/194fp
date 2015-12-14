import numpy as np
import sys

from skimage import filters
from matplotlib import pyplot as plt
from matplotlib import colors

def main(imname, maskname=None):
    im = plt.imread("./images/%s.jpg" % imname)/255.
    plt.imshow(im)
    print("Select DOF top and bottom")
    pts = np.array(plt.ginput(2))
    plt.close()
    pts = pts[:,1].astype(int)

    mid = (pts[0]+pts[1])/2
    tail = abs(pts[0]-pts[1])/2

    if maskname:
        mask = plt.imread("./images/%s.jpg" % maskname)/255.
        over = im*mask

    for thresh in range(tail, max(mid, im.shape[0]-mid), 5):
        # blur image
        imblur = filters.gaussian_filter(im, sigma=1)

        # unblur if distance from line is < thresh
        rr, cc = np.meshgrid(np.arange(im.shape[0]), np.arange(im.shape[1]))
        rr = rr.flatten()
        cc = cc.flatten()
        vector = np.ones([2, len(rr)]).astype(int)
        vector[0] = rr
        vector[1] = cc
        dof = abs(vector[0]-mid) < thresh
        dof = np.array(dof).reshape(-1)
        rr = rr[dof]
        cc = cc[dof]
        vector = vector[:, dof]
        imblur[rr, cc] = im[vector[0], vector[1]]
        im = imblur

    if maskname:
        im *= (1 - mask)
        im += over

    im = colors.rgb_to_hsv(im)
    im[...,1] *= 1.7
    im[...,1][im[...,1] > 1] = 1
    im = colors.hsv_to_rgb(im)

    plt.imsave("./results/toy_%s.jpg" % imname, im)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print README
