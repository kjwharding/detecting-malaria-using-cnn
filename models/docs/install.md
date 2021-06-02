# Training Custom Models
To design and implement custom Convolutional Neural Network models you will need to install the required environment. The following guide will help you to install my code and the essential python libraries to create working image classifiers. It should be noted that not all CNN models require the libraries mentioned, some may take a completely different approach.
### 1. Download the dataset you will use to train your model
* If you wish to use the genuine NIH Malaria dataset, please download it [here]( https://lhncbc.nlm.nih.gov/LHC-publications/pubs/MalariaDatasets.html).
* If you would like to use my dataset which is already augmented and split download it [here](../../dataset/augmented).
* Alternatively, obtain your own dataset for training, validating, and testing.

### 2. Install the required libraries
Prior to installing the libraries below please ensure you have [Python 3.7.9]( https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe) installed. Furthermore, `python` (or `python3`) and `pip` (or `pip3`) should be on path.
If you are on Windows, you can install the required libraries almost instantly. Just download the batch file below and run it.

[required_lib.bat](required_lib.bat)

Note: *Additionally, I have included some extra libraries that are commonly used in computer vision. This is because further investigations may require them.*

If you are using macOS or a Linux distribution, please use `pip` (or `pip3`) to install the following libraries.
* Numpy: `pip install numpy~=1.18.5`
* Matplotlib: `pip install matplotlib~=3.3.2`
* OpenCV: `pip install opencv-python~=4.4.0.46`
* TensorFlow: `pip install tensorflow~=2.3.1`
* Keras: `pip install keras~=2.4.3`

### 3. Download my script to train a CNN model
If you wish to train a Convolutional Neural Network to classify images, you are permitted to use my most recent Python script which can be downloaded [here](../final/final_model.py). Please note that this script will need to be modified depending on the type of data you want to classify. Convolutional Neural Networks always require tweaking to find an optimal model. 


[Return to 'README.md'](../../README.md)
