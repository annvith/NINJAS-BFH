# NINJAS-BFH

We have tried to built an image classifier that takes an image as input from the user and then predict whether the image is that of mamootty or mohanlal.

Creation of Dataset:
We created the dataset on our own.We used selenium inorder to do web scraping and download the images of mammootty and mohanlal.The code for this resides in main.py.This file has to be run twice.One for mohanlal and other for mamootty.The dataset used for training has been obtained from kaggle while we used our own dataset for test data.
dataset link:https://www.kaggle.com/ameyajames/mamooty-vs-mohanlal

We used pytorch  generate the main ML model.The test accuracy that we got was 73%.We saved that as the best checkpoint model.
The code for the model can be found inside modelbuilding.py.
The flask application(web interface)  takes the image input,loads the saved model and then gives the prediction results.

The final link of our complete project can be found @ :
https://mamooka-lal.herokuapp.com/

Team ID:
BFH/recEqPYJVOIIxS6gc/2021

Team Name:NINJAS
Members:Ameya Lizbeth James
        Hira Fathima
        Ann Vithayathil


