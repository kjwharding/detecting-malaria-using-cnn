from flask import Flask, render_template, redirect, url_for, request, session
import tensorflow as tf
from tensorflow.keras.models import load_model
import secrets
from tensorflow import keras
import numpy as np

app = Flask(__name__)

# model dir
MODEL = r"static\cnn.model"

# client key 
app.secret_key = secrets.token_urlsafe(32)

# config upload dir
UPLOAD_DIR = r"static"
app.config["UPLOAD_IMAGES_DEST"] = UPLOAD_DIR

# home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and "sample_img" in request.files:

        img = request.files['sample_img']
        img_name = img.filename
        img.save(app.config["UPLOAD_IMAGES_DEST"] + "/" + img_name)
        img_path = app.config["UPLOAD_IMAGES_DEST"] + "/" + img_name

        # predicting class using uploaded image 
        prediction = predict_class(img_path)
        # 0 = infected, 1 = healthy
        
        # initialise variables
        predict_string = ""
        predict_colour = ""

        # if class is parasitized
        if prediction == 0:
            predict_string = "infected with malaria"
            predict_colour = "#e80000" # red text colour

        # if class is healthy
        elif prediction == 1:
            predict_string = "healthy"
            predict_colour = "#00dd10" # green text colour
        
        else:
            predict_string = "[ERROR WITH CLASSIFICATION MODEL]"


        # adding information to session
        session["img_name"] = img_name
        session["prediction"] = predict_string
        session["predict_colour"] = predict_colour

        # redirect to classification page
        return redirect(url_for("classification"))

    # visit home page or return to home page if issue occurs
    return render_template("index.html")

# classification page
@app.route("/classification")
def classification():

    # try to classify image
    if "img_name" in session:
        return render_template("classification.html", uploaded_img=session["img_name"], predict_colour=session["predict_colour"])
    
    # if there's an issue return to the home page
    else:
        return redirect(url_for("index"))

# predict class of cell using pre-trained model
def predict_class(img_path):
    img = keras.preprocessing.image.load_img(
        img_path,

        # resize to required cnn input size
        target_size=(100, 100)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # load model and make prediction
    model = load_model(MODEL, compile=True)
    prediction = model.predict(img_array)
    return np.argmax(prediction)

if __name__ == "__main__":
    app.run(debug=True)