from cv2 import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# test image from "random_test_imgs" dir
TEST_IMG_ADDRESS = r"C:\ce301_harding_kiernan_j_w\dataset\testing_set\uninfected\C158P119ThinF_IMG_20151115_181859_cell_100.png"

# preparing image for cnn
def prepare_input_img(img_path):
    IMG_DIMENSION = 50
    original_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    new_img = cv2.resize(original_img, (IMG_DIMENSION, IMG_DIMENSION))
    #plt.imshow(new_img, cmap="gray")
    #plt.show()
    return new_img.reshape(-1, IMG_DIMENSION, IMG_DIMENSION, 1)

# making prediction
def predict_class(img):
    model = load_model(r"malaria_classifier.model", compile=True)
    predict_malaria = model.predict(prepare_input_img(img))
    return int(predict_malaria[0][0])

# making the prediction
prediction = predict_class(TEST_IMG_ADDRESS)

print("\n\n-----------------------------------------\n")

if prediction == 0:
    print("Sample is infected with Malaria")

elif prediction == 1:
    print("Sample is healthy")

else:
    print("Error")

print("\n-----------------------------------------\n\n")
