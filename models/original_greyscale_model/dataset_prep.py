import numpy
import matplotlib.pyplot as plt
import os
from cv2 import cv2
import random
import pickle

# change path address
DATADIR = r"C:\ce301_harding_kiernan_j_w\dataset\training_set"
CATEGORIES = ["parasitized", "uninfected"]
IMG_DIMENSION = 50

training_data = []
def create_training_data():
    for category in CATEGORIES:
        
        print("<<< Started " + category + " >>>")

        # path to parasitized and uninfected cell imgs
        path = os.path.join(DATADIR, category)

        # setting each class to either 0 or 1
        class_no = CATEGORIES.index(category)

        
        for img in os.listdir(path):
            try:
                # print current image 
                print(category + " - " + img)

                # setting the images as greyscale and resizing
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_img_array = cv2.resize(img_array, (IMG_DIMENSION, IMG_DIMENSION))
                training_data.append([new_img_array, class_no])

                # for testing purposes only
                # plt.imshow(new_img_array, cmap="gray")
                # plt.show()
                # print(img_array)

            except:
                pass

# run the above method
create_training_data()

# finished preparing images
print("<<< Prepared images >>>")

# shuffling the data to remove future bias
random.shuffle(training_data)

# looking at the size of the working training set
print("Training set size: " + str(len(training_data)))

# feature and label arrays
features = []
labels = [] 

# adding the features and labels to the arrays
for ft, lb in training_data:
    features.append(ft)
    labels.append(lb)

# converting to a numpy array 
features = numpy.array(features).reshape(-1, IMG_DIMENSION, IMG_DIMENSION, 1)

# using pickle to output data
output = open("C:/ce301_harding_kiernan_j_w/malaria_cnn/features.pickle", "wb")
pickle.dump(features, output)
output.close()

output = open("C:/ce301_harding_kiernan_j_w/malaria_cnn/labels.pickle", "wb")
pickle.dump(labels, output)
output.close()

print("<<< Complete >>>")
