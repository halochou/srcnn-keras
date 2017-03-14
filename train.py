import h5py
import numpy as np

hf = h5py.File('official.h5')
data = hf.get('data')
label = hf.get('label')
n = data.shape[0]
data = np.array(data).dot(255).reshape(n, 33, 33, 1)
label = np.array(label).dot(255).reshape(n, 21, 21, 1)

from keras.models import Sequential
from keras.models import Model
from keras.layers import Input, Convolution2D
from keras.optimizers import Adam


def srcnn(input_shape=(33,33,1)):
    model = Sequential()
    model.add(Convolution2D(64, 9, 9, border_mode='valid', input_shape=input_shape, activation='relu'))
    model.add(Convolution2D(32, 1, 1, activation='relu'))
    model.add(Convolution2D(1, 5, 5, ))
    model.compile(Adam(lr=0.001), 'mse')
    return model

model = srcnn()
from keras.models import load_model
resume = 1
#model = load_model("models/%05d.h5" % resume)

for i in range(resume,10,1000):
    model.fit(data, label, batch_size=128, nb_epoch=10, shuffle='batch')
    model.save("models/%05d.h5" % i)
