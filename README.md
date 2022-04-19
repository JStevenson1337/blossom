README.md
[]: # Language: Python3
[]: # Path: setup.py
setup.py
[]: # Language: Python3
[]: # Path: tests/test_*.py
tests/test_*.py
[]: # Language: Python3
[]: # Path: tests/test_*.py


#------FOR LINUX/MAC---------#
#installing venv 
sudo apt-get install python3.6-venv
#creating virtual env
python3 -m venv env
#activating virtual env
source env/bin/activate


#-------FOR WINDOWS----------#
#installing venv
py -m pip install --user virtualenv
#creating virtual env
py -m venv env
#activating virtual env
.\env\Scripts\activate



#------------RUN----------#
export FLASK_APP=app
flask run
