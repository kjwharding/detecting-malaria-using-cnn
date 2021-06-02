# How to use the application
This guide is specific to using the application on localhost with a Windows machine. This application will work on macOS or a Linux distribution but may require a few tweaks. Ideally, this application would be hosted on a custom domain, however, for demonstration purposes, this works perfectly.

### 1. Install the required libraries
Before installing the libraries above please ensure you have [Python 3.7.9]( https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe) installed. Furthermore, `python` (or `python3`) and `pip` (or `pip3`) should be on path.

If you are on Windows, you can install the required libraries almost instantly. Just download the batch file below and run it.

[required_lib.bat](../../web_app/docs/required_lib.bat)

Note: *Additionally, I have included some extra libraries that are commonly used in computer vision. This is because further additions to this application may require them.*

If you are using macOS or a Linux distribution, please use `pip` (or `pip3`) to install the following libraries.
* Numpy: `pip install numpy~=1.18.5`
* Matplotlib: `pip install matplotlib~=3.3.2`
* OpenCV: `pip install opencv-python~=4.4.0.46`
* Tensorflow: `pip install tensorflow~=2.3.1`
* Keras: `pip install keras~=2.4.3`
* Shutil: `pip install pytest-shutil~=1.7.0`
* Flask: `pip install flask~=1.1.2`
* Flask Forms: `pip install flask-wtf~=0.14.3`
* Flask Uploads: `pip install flask-uploads~=0.2.1`
* Werkzeug: `pip install werkzeug==0.16.1`
* Connexion: `pip install connexion==1.0.38`

### 2. Installing the application
Now that the relevant libraries are installed you can download the application itself. To do this please install the zip file below. 

[malaria_classifier_app.zip](../../web_app/docs/malaria_classifier_app.zip)

When the application is downloaded, make sure to unzip the folder in a sensible location on your computer.

### 3. Getting the application running
To run the application, open the Command Prompt and navigate to the `malaria_classifer_app` folder. 

Alternatively, you can manually visit the folder in the File Explorer and type `cmd` into the directory location bar. 

From here type the following command to start the application on localhost:

```
python app.py
```

*Note:* `python` *may need to be replaced with* `python3`.

### 4. Using the application
Now that the application is running on your local machine, open an internet browser such as Chrome, and type the following into the address bar:

```
localhost:5000
```
or
```
127.0.0.1:5000
```

Now you will have access to the application. Just select a red blood cell and **classify**!


[Return to 'README.md'](../../README.md)
