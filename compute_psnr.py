from scipy.misc import imread,imsave
import numpy as np

def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(np.float)
    rgb[:,:,[1,2]] -= 128
    return rgb.dot(xform.T)

gt = imread('butterfly_GT.bmp')
gt = ycbcr2rgb(gt)
gt = gt[:,:,0]
gt = gt[6:231,6:231,:]
imsave('ground_true_Y.png', gt)

test = imread('sr.bmp')
test = ycbcr2rgb(test)
test = test[:,:,0]
#imsave('test.png', test)

