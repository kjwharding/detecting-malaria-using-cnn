# Implementation
Please find the application code [here](../../web_app). 
The application is implemented using Flask, which is a light-weight server-side framework that aids the development of web applications in Python. Using Flask, other Python libraries can be used within a web application. This allows a CNN model (loaded from Keras) to interact with a web application and classify images, such as parasitized and healthy red blood cells. Like any web application, it could be hosted on a server or accessed via localhost. Therefore, it does not require an internet connection.

### Main Functions
There are 3 main functions within the Python application, ‘[app.py](../app.py)’. Two of these functions are linked to app routes, which map a specific URL to a Python function.

* Firstly, there is a function called `predict_class(img_path)`, which takes the image path as a parameter. It loads & resizes the image using `keras.preprocessing.image.load_img()` and then proceeds to classify the image using the pre-trained CNN model. The CNN model is loaded using Keras’ `load_model()` function.

* Secondly, function `index()` is an app route for the application home page (see figure 1). This function renders the template web page, ‘[index.html](../templates/index.html)’, using Flask’s `render_template()` function. Alternatively, if an image is uploaded, the image is classified using the function mentioned above, `predict_class()`. When the class is predicted, some variables are added to the session. For example, a string to indicate whether the sample is parasitized or healthy and another string containing the hex colour code for either red (parasitized), or green (healthy). Now that the image is classified and all the data is prepared, the user would be redirected to the classification page using the `redirect()` function.

*Figure 1: Home page (index) function.*

```
@app.route("/", methods=["GET", "POST"])
def index():
```

* Last of all, function `classification()` is an app route for the classification page (see figure 2). If the image name is in session, the classification template is rendered alongside the relevant data (e.g. the prediction). This data is passed to the classification web page via the current session. If any issues occur, you are redirected straight back to the home page (index).

*Figure 2: Classification page function.*

```
@app.route("/classification")
def classification():
```

### Web Pages (Templates)
Below is a link to the relevant web pages that are rendered using the Flask web application. Any of the styling and layout is discussed in a different section of the technical documentation, which can be found [here](styling.md). In both web pages, Python code is used to access the relevant data. This is done by surrounding the statements in double braces, which can be seen in figure 3, where an image is retrieved.

* Home page (input): [index.html](../templates/index.html)

* Classification output page: [classification.html]( ../templates/classification.html)

*Figure 3: Python code used in a `html` document.*

```
<img src="{{url_for('static', filename='logo.png')}}" class="logo"/>
```

### File Layout
The directory layout for a Flask web application is required to be very specific to locate files. For instance, images and stylesheets should be located in the ‘static’ directory and web pages should be located in the ‘templates’ directory. Please find an example in figure 4. 

*Figure 4: Directory layout for a Python web application.*

* static
    * image.png
    * styles.css
* templates
    * index.html
* app.py

[Return to 'README.md'](../../README.md)
