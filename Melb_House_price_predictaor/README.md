## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Project Directory Structure](#directory-structure)
* [Features](#features)
* [Sources](#sources)

## General info
This project is predicting Melboure House price based on suburb selection.
	
## Technologies
Project is created with:
* Flask version: 1.1.2
* Ajax Javascript version: 3.4.1
* dash library version: 1.19
	
## Setup
To run this project, install flask in your local machine:

```
$ pip install pickle
$ pip install flask
$ cd ../Melb_house_price_predictor/server
$ python server.py
```

## Directory Structure
![Project Directory Structure] (https://github.com/nipune/Project-2/blob/main/Melb_House_price_predictaor/dir_structure.PNG)

## Features
* This simple web interface calcuates house price based on RandomForestregressor algorithm
* CSV File data downloaded from Kaggle -Melbourne_full_House.csv
* cleaned the data using following criteria:
    * Remove the rows with null values
    * Remove the rows landsize or building area which has 0 value
    * Remove the rows where building area is greatre than landsize
    * Suburub with one property grouped as 'Other'
* Remove Price and bedroom outliers
* Create distribution plot to see the price trend
* Split the data and use linearregression algorithm to fit the model and find out the score
* Use GridSearchCV model to compare LinearRegression, RandomForestRegressor and Decisiontree model to find out the best scoring model
* RandomForest gave best score of .75
* Use this model to predict home price value
* store that model into pickle file and colums into json file
* Use HTML, Javascript and FLask to develop UI interface

## Output

![House Price Image](HousePrice.gif)
## Sources
This Webinterface application development is inspired by Machine Learning & Data Science youtube video Tutorial by codebasics
