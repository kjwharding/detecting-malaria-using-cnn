@ECHO OFF

ECHO ======================================================================
ECHO NOTE: PLEASE INSTALL PYTHON 3.7 AND ADD PIP TO PATH BEFORE CONTINUING.
ECHO ======================================================================
PAUSE
ECHO ======================================================================
ECHO INSTALLING PYTHON LIBRARIES TO CREATE AND RUN THE MODEL...
ECHO ======================================================================

pip install numpy~=1.18.5
pip install matplotlib~=3.3.2
pip install opencv-python~=4.4.0.46
pip install pickle-mixin~=1.0.2
pip install tensorflow~=2.3.1
pip install keras~=2.4.3
pip install pillow~=8.0.1
pip install pytest-shutil~=1.7.0
pip install flask~=1.1.2
pip install flask-wtf~=0.14.3
pip install flask-uploads~=0.2.1
pip install werkzeug==0.16.1
pip install connexion==1.0.38
pip install pytest-shutil==1.7.0

ECHO ======================================================================
ECHO ALL LOCALLY INSTALLED LIBRARIES.
ECHO ======================================================================

pip freeze

ECHO ======================================================================
ECHO PLEASE HAVE A GOOD DAY. GOODBYE.
ECHO ======================================================================
PAUSE

