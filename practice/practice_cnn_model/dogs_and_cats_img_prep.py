"""
Please find the tutorial that I followed linked:
- https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/
- https://www.youtube.com/watch?v=j-3vuBynnOE&ab_channel=sentdex
"""

import numpy
import matplotlib.pyplot as plt
import os
from cv2 import cv2
import random
import pickle

DATADIR = "cnn_test_code\kagglecatsanddogs_3367a\PetImages"
CATEGORIES = ["Dog", "Cat"]
IMG_SIZE = 50

training_data = []
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #path to cats/dogs directory
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except:
                pass

create_training_data()
random.shuffle(training_data)

X = [] 
y = [] 

for features, label in training_data:
    X.append(features)
    y.append(label)

X = numpy.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out = open("cnn_test_code/X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("cnn_test_code/y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()