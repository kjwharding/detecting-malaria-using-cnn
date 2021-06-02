# Setting up the Environment
After researching the theory behind Convolutional Neural Networks, I needed to understand how they could be implemented. Initially, I researched numerous tutorials (some through YouTube) which explained how to utilise different libraries to create a CNN. I found that ‘[Python Programming Tutorials]( https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/)’ provided a simple tutorial that would get me started. The libraries that I used are very popular for deep learning, but the majority of them required installation using PIP. The external libraries (with installation commands) that I utilised were:

* TensorFlow `pip install tensorflow`
* Keras `pip install keras`
* OpenCV `pip install opencv-python`
* Pickle `pip install pickle-mixin`
* Numpy `pip install numpy`
* Matplotlib `pip install maplotlib`
* Random
* OS

To ensure that the libraries were installed correctly I used the command `pip freeze`. Furthermore, I imported all the libraries into Python and run the program to check that there were no unexpected errors. Initially, I found an issue when importing one of the most important libraries, TensorFlow (see below).
``` 
>>> import tensorflow
2020-10-08 22:20:33.261414: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2020-10-08 22:20:33.261569: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
```
It is clearly stated in the example above that the error should be ignored if you do not have a GPU. However, I still decided to carry out some research as I had a NVIDIA® GeForce® GTX 1060 6GB installed in my local system. I found that there should be no compatibility issues as I have not set-up TensorFlow GPU. Any other library or environment issues I face will be discussed later when found.


[Return to 'README.md'](../../README.md)
