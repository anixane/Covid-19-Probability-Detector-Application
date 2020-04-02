# Covid-19 (Corona) Probability Detector Application

![Alt text](/screenshots/landingpage.png "Optional Title")

## Features
- You can detect the probablity of a patient having Corona Virus based on the early stage symptoms.
- A machine learning model is trained on the sample data generated in data.csv file. Currently it uses Logistic Regression.
- API for interaction is developed on Flask.
- Don't like a feature? Change it! Raise a Pull Request.

## Result Screenshot when submit is clicked after entering early stage symptoms.
![Alt text](/screenshots/resultpage.png "Optional Title")


## Installation
- You need Python
- Install dependencies by running
```bash
pip install Jupyter
pip install pandas
pip install numpy
pip install sklearn
pip install tensorflow  #only supports python 3.6.x versions
pip install pickle
```
- Clone this repo and create auth.py
```bash
git clone git@github.com:anixane/COVID-19-Probability-Detection.git
```
- Run the flask server
