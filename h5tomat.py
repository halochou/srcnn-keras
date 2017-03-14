import h5py
import numpy as np
import scipy.io as sio

hf = h5py.File('model.h5')
weights_conv1 = np.array(hf.get('model_weights/convolution2d_1/convolution2d_1_W:0'))
biases_conv1 = np.array(hf.get('model_weights/convolution2d_1/convolution2d_1_b:0'))
weights_conv2 = np.array(hf.get('model_weights/convolution2d_2/convolution2d_2_W:0'))
biases_conv2 = np.array(hf.get('model_weights/convolution2d_2/convolution2d_2_b:0'))
weights_conv3 = np.array(hf.get('model_weights/convolution2d_3/convolution2d_3_W:0'))
biases_conv3 = np.array(hf.get('model_weights/convolution2d_3/convolution2d_3_b:0'))

res = dict()
res['weights_conv1'] = weights_conv1.reshape(81, 64)
res['weights_conv2'] = weights_conv2.reshape(64, 1, 32)
res['weights_conv3'] = weights_conv3.reshape(32, 25)
res['biases_conv1'] = biases_conv1.reshape(64, 1)
res['biases_conv2'] = biases_conv2.reshape(32, 1)
res['biases_conv3'] = biases_conv3.reshape(1)

sio.savemat('res.mat', res)
