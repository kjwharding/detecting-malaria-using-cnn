from cv2 import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

MODEL = load_model(r"path", compile=True)

# test image from "random_test_imgs" dir
DATADIR = r"C:\ce301_harding_kiernan_j_w\dataset\augmented\testing_set"
CATEGORIES = ["parasitized", "uninfected"]
IMG_DIMENSION = 50


# preparing image for cnn
def prepare_input_img(img_path):
    IMG_DIMENSION = 50
    original_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    new_img = cv2.resize(original_img, (IMG_DIMENSION, IMG_DIMENSION))
    return new_img.reshape(-1, IMG_DIMENSION, IMG_DIMENSION, 1)

# making prediction
def predict_class(img):
    predict_malaria = MODEL.predict(prepare_input_img(img))
    return int(predict_malaria[0][0])

def test_accuracy():
    correct_predictions = 0
    total_predictions = 0

    for category in CATEGORIES:
        # join category and path
        path = os.path.join(DATADIR, category)

        # 0 = parasitized, 1 = healthy
        class_no = CATEGORIES.index(category)

        # test all predictions
        for img in os.listdir(path):
            try:
                prediction = predict_class(os.path.join(path, img))
                print("\n" + os.path.join(path, img))
                print(str(total_predictions) + "\n")

                if prediction == class_no:
                    correct_predictions+=1

            except:
                pass

            total_predictions+=1

    accuracy_percentage = (correct_predictions/total_predictions)*100
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    print(str(correct_predictions) + "/" + str(total_predictions))
    print(str(accuracy_percentage) + "%")
    print("---------------------------------------------------")
    print("---------------------------------------------------")

    
test_accuracy()