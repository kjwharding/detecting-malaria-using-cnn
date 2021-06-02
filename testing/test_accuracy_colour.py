import tensorflow as tf
import os
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model

# test images
DATADIR = r"C:\ce301_harding_kiernan_j_w\dataset\augmented\testing_set"
CATEGORIES = ["parasitized", "uninfected"]
IMG_DIMENSION = 100
MODEL = load_model(r"C:\ce301_harding_kiernan_j_w\models\final\final.model", compile=True)

# making prediction
def predict_class(img_path):
    img = keras.preprocessing.image.load_img(
        img_path,
        target_size=(IMG_DIMENSION, IMG_DIMENSION)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    prediction = MODEL.predict(img_array)
    #print(prediction)
    return np.argmax(prediction)

# test model accuracy
def test_accuracy():
    correct_predictions_p = 0
    correct_predictions_h = 0
    total_predictions_p = 0
    total_predictions_h = 0

    for category in CATEGORIES:

        # join category and path
        path = os.path.join(DATADIR, category)

        # 0 = parasitized, 1 = healthy
        class_no = CATEGORIES.index(category)

        # test all predictions
        for img in os.listdir(path):
            if category == "parasitized":
                try:
                    prediction = predict_class(os.path.join(path, img))

                    #print("\n=========================================\n")
                    #print(os.path.join(path, img))
                    #print(CATEGORIES[prediction] + "\n")
                    print(str(correct_predictions_p) + "/" + str(total_predictions_p) + "\n")
                    #print("=========================================\n")

                    if prediction == class_no:
                        correct_predictions_p += 1

                except:
                    pass

                total_predictions_p += 1

            else:
                try:
                    prediction = predict_class(os.path.join(path, img))

                    #print("\n=========================================")
                    #print("\n" + os.path.join(path, img))
                    #print(CATEGORIES[prediction] + "\n")
                    print(str(correct_predictions_p + correct_predictions_h) + "/" + str(total_predictions_p + total_predictions_h) + "\n")
                    #print("=========================================\n")

                    if prediction == class_no:
                        correct_predictions_h += 1

                except:
                    pass

                total_predictions_h += 1

    accuracy_percentage_p = (correct_predictions_p / total_predictions_p) * 100
    accuracy_percentage_h = (correct_predictions_h / total_predictions_h) * 100
    accuracy_percentage_total = (accuracy_percentage_p + accuracy_percentage_h) / 2

    print("\n\n\n\n\n\n")
    print("=========================================")
    print("=========================================")
    print("PARASITIZED ACCURACY")
    print(str(correct_predictions_p) + "/" + str(total_predictions_p))
    print(str(accuracy_percentage_p) + "%")
    print("-----------------------------------------")
    print("UNINFECTED ACCURACY")
    print(str(correct_predictions_h) + "/" + str(total_predictions_h))
    print(str(accuracy_percentage_h) + "%")
    print("-----------------------------------------")
    print("*** TOTAL ACCURACY ***")
    print(str(correct_predictions_p + correct_predictions_h) + "/" + str(total_predictions_p + total_predictions_h))
    print(str(accuracy_percentage_total) + "%")
    print("=========================================")
    print("=========================================")

MODEL.summary()
test_accuracy()