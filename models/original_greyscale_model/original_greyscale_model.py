import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import numpy as np
import matplotlib as plt

# reading in required training data - used personal dir as issue with relative dirs
# import features
features = pickle.load(open(r'C:\ce301_harding_kiernan_j_w\models\original_greyscale_model\features.pickle', 'rb'))
 # import labels
labels = pickle.load(open(r'C:\ce301_harding_kiernan_j_w\models\original_greyscale_model\labels.pickle', 'rb'))

# converting to numpy arrays
# normalising data (/255 as the max pixel value is 255)
features = np.array(features/255.0)
labels = np.array(labels)

# creating base model to add layers to
model = Sequential()

# -- first layer --
# 32 = no. of files the convolutional layers will learn from
# 3,3 = the convolution window (or kernal size)
model.add(Conv2D(32, (3,3), input_shape = features.shape[1:]))
# applying the rectified linear activation function
# in basic terms - return 0 if negative and x if positive
model.add(Activation('relu'))
# used to reduce the spatial size of the representation
model.add(MaxPooling2D(pool_size=(2,2)))

# -- second layer -- 
model.add(Conv2D(32, (3,3),))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# -- third layer -- 
# dense layer requires a 1D dataset
model.add(Flatten())
# deeply connected layers
model.add(Dense(32))

# -- output layer -- 
model.add(Dense(1))
# applying the sigmoid activation function
model.add(Activation('sigmoid'))

# -- output --
model.compile(loss='binary_crossentropy', 
            optimizer='adam',
            metrics=['accuracy'])

model_hist = model.fit(features, labels, 
        batch_size=32, 
        epochs=16,
        validation_split=0.1)

model.save("greyscale_model.model")