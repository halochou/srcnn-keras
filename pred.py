import numpy as np
from scipy import misc
from keras.models import load_model

input_size = 33
label_size = 21
pad = (33 - 21) / 2
gt = misc.imread('gnd_Y.png')


low = misc.imresize(gt, 1.0/3.0, 'bicubic')
low = misc.imresize(low, 3.0, 'bicubic')

for model_id in range(3150,14001,50):
    model = load_model("models/%05d.h5" % model_id)
    high = np.zeros(low.shape)

    for i in range(0, 211, 21):
        for j in range(0, 211, 21):
            sub_img = low[i:i+33, j:j+33].reshape(1,33,33,1)
            pred = model.predict(sub_img).reshape(21,21)
            high[i+pad:i+pad+21, j+pad:j+pad+21] = pred

    misc.imsave("outputs/%05d.png" % model_id, high)
