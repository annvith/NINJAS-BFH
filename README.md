# Project Name:
NINJAS
We have tried to built an image classifier that takes an image as input from the user and then predict whether the image is that of mamootty or mohanlal.

#TEAM MEMBERS:
1.Ameya Lizbeth James(https://github.com/ameyalizbeth)
2.Hira Fathima (https://github.com/Hirafathima)
3.Ann Vithayathil(https://github.com/annvith/)

#Team ID:
BFH/recEqPYJVOIIxS6gc/2021

#Link to Product walkthrough:
https://drive.google.com/file/d/1xf9DS20_KrAeBhJRwlYSxljwcNggF3BC/view?usp=sharing

#How it Works?
Step1:
Creation of Dataset:
We created the dataset on our own.We used selenium inorder to do web scraping and download the images of mammootty and mohanlal.The code for this resides in main.py.This file has to be run twice.One for mohanlal and other for mamootty.
Dataset Link :https://www.kaggle.com/ameyajames/mamooty-vs-mohanlal
Step2:
We used pytorch  generate the main ML model.The test accuracy that we got was 73%.We ran a total of 15 epochs and saved the best one from that as the best checkpoint model.You can view this in the bestcheckpoint.model file.
The code for the model can be found inside modelbuilding.py.
Step3:
The flask application(web interface)  takes the image input,loads the saved model and then gives the prediction results.
The final link of our complete project can be found @ :
https://mamooka-lal.herokuapp.com/

#Libraries Used:
Flask==2.0.0
Pillow==8.2.0
urllib3==1.26.4
Werkzeug==2.0.0
torch==1.8.1 
torchvision==0.9.1
numpy==1.19.5
opencv-python==4.5.2.52
glob2==0.7
pathlib2==2.3.5
selenium==3.141.0
Jupyter==1.0.0
Notebook==6.4.0
chrome driver according to your browser version
Link to download:https://chromedriver.chromium.org/downloads

#How to configure:
install conda
create a virtual environment
install the necessary packages
git clone https://github.com/annvith/NINJAS-BFH

#How to run
1.dataset creation

make a folder training_images
create two sub folders mohanlal and mamooty
and add sufficient photos.

make a folder testing_images
create two sub folders mohanlal and mamooty
and add sufficient photos.

Create a file named "chromedriver" for the downloaded version of chrome driver in the same directory as that of main.py
to create the dataset run the file main.py by "python main.py"
here is the kaggle link
training_images :https://www.kaggle.com/fillerink/mohanlal-mammooty-images
testing_images :https://www.kaggle.com/ameyajames/mamooty-vs-mohanlal

2. model building

in the file newmodel.ipynb ,
correct the train_path to the path where training_images are present
correct the test_path to the path where tesing_images are present
now run the file newmodel.ipynb in jupyter notebook
this saves the model as best_checkpoint.model


3.prediction

create a folder predicting_images with images you want to predict
in the file newmodelprdiction.ipynb correct the pred_path and train_path
according to the path they are present on yur computer.
run the file newmodelprdiction.ipynb in jupyter notebook


RUNNING THE FLASK APP
git clone the repo https://github.com/ameyalizbeth/classifier
install the packages as shown in the reqirements.txt in a virtual env
run the file app.py by using "python app.py"




