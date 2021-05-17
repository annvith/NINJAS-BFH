from skimage.transform import resize
from scipy import misc
import imageio
import numpy as np
import os
import pandas as pd

from keras.utils import np_utils
label = os.listdir("./dataset_image")

X=[]
y=[]
for image_label in label:
        images = os.listdir("dataset_image/"+image_label)
        for image in images:
            img = imageio.imread("dataset_image/"+image_label+"/"+image)
            img = resize(img, (64, 64))
            X.append(img)
            y.append(label.index(image_label))
 
X=np.array(X)
y=np.array(y)

X=X.astype('float32')
X = X / 255.0
print(X)
y = np_utils.to_categorical(y)
num_classes = y.shape[1]
print(y)
np.save("X_value",X)
np.save("y_value",y)

