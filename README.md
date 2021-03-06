## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Project Directory Structure](#directory-structure)
* [Features](#features)
* [Sentiment Analysis](#Sentiment-Analysis)
* [Sources](#sources)

## General info
This project is predicting the median Melbourne House prices based on suburb selection. By using various machine learning teachniques we were able to determine which models gave the closest predicition to the actual prices. 

The team used three notebook types: Jupyter Notebook (on local machines), [Google Colab](https://colab.research.google.com/drive/1FOjqVT7H5lRAP_aNokAh4r-T0mFHop19) & Amazon SageMaker. Please note that SageMaker notebook instances have been stopped and deleted, artefacts are available in the presentation.

For this project the team crunched both large and smaller datasets, this tested both our patience and Google Colab/AWS SageMakers computational (free/unpaid for) limits. Given the demand on our local machines, the team decided to eacn run separate notebooks to both clean data and verify/crunch different models, with a view to see which model would best fit. 

We have included in the supplementary material folder these alternative notebooks should you want to see the code itself. This has been summarised in our [presentation](https://github.com/nipune/Project-2/blob/main/Project%202_%20House%20Price%20Predictor%20v2.0.pptx).
	
## Technologies
Project is created with:
* Sci-Kit library
* Flask version: 1.1.2
* Ajax Javascript version: 3.4.1
* Dash library version: 1.19
	
## Setup
To run this project, install flask in your local machine:

```
$ pip install pickle
$ pip install flask
$ cd Melb_house_price_predictor/server
$ python server.py
```

## Directory Structure
![image](https://github.com/nipune/Project-2/blob/main/Images/dir_structure.gif)

## Features
* This entire project is comparing multiple features which are very important as part of Real Estate data analysis. By filtering for valid data then integrating the dataset using a simple web interface. The output is a prediction of house prices in Victorian suburbs based on the Random Forest Regressor Algorithm.
* There were two datasets used as part of this project from Kaggle: 
	* 1. Melbourne_houseing_full.csv which has data from 2016 till 2018 (5MB)
	* 2. Aus-property-sales-sep2018-april2020.csv (37MB)
* During our Analysis, Team used following machine learning models to conclude which algorithm works best to predict house prices
	* Linear regression
	* Balanced Random Forest
	* Random Forest Regressor
	* Gradient Boosting Regressor
	* Easy Ensemble Classifier
	* Decision Tree Regressor

* Dimensionality reduction technique was applied to the data to reduce the input features from 21 to 10 in order to perform sanity checks on Melbourne Housing data. For example, the following columns that were not as important to predict house prices: longitude, latititude, loc_pid, lat_pid etc..

* Team also used estimators like Mean_absolute_error, root_mean_squared_error and R-square value to detemine the relationship between the model and the dependent variable for predicting house price.
* Team also performed feature engineering to generate new feature named price_per_sqm to train the model* 
* For the data cleaning process the following data cleansing techniques were applied:
    * Remove the rows with null values.
    * Remove the rows where landsize or building area has a 0 value.
    * Remove the rows where building area is greater than landsize.
    * Suburbs with 10 or less properties grouped as 'Other'
* After cleaning the data, we removed price and bedroom outliers from the data.
* To build confidence around the clean data a distribution plot. This was created to visualise the price trend and it was clearly showing less outliners.
* As part of features selection the team used the ChiSquare Test to determine which features are more important. The result supported the decision making in what variables would be most suitable to use in building the price prediction model. The output below is the result from the ChiSquare Test. 
* ![image](https://github.com/nipune/Project-2/blob/main/Images/Senitment.png)
* Fit and Train the data using test and train model. Linear-regression algorithm was used to fit the model and find out the score. 
* ![image](https://github.com/nipune/Project-2/blob/main/Images/model_score.jpg)
* Use GridSearchCV model to compare LinearRegression, RandomForestRegressor and Decisiontree model to find out the best scoring model
* RandomForestRegressor gave best score of .75
* _Evaluate the trained model(s) using testing data. Include any calculations, metrics, or visualizations needed to evaluate the performance._ -Need to add more details here
* The plot below is of the linear regression model looking at the Australian house price data. With a 80% fit to the data and mean absolute error of $114,352
* ![image](https://github.com/nipune/Project-2/blob/main/Images/comparisonpred.png)
## Sentiment Analysis
* Team uses sentiment analysis technique to decide on our parameter model for real estate dataset, we used the Word Cloud to support our analysis and generate the output.
* The word cloud used news articles that were pulled using the NewsApi searching for the key words 'House Prices Australia'. 
![image](https://github.com/nipune/Project-2/blob/main/Images/word%20cloud%20.PNG)
* Use this model to predict home price value
* store that model into pickle file and colums into json file


## Output
![Image](https://github.com/nipune/Project-2/blob/main/Images/House%20Predictor.GIF)
* To develop the user interface the following were used: Use HTML, Javascript and FLask. This interface gives the end user an easy way to determine what the median house price is for a chosen suburb based on the selection criteria.  
## Sources
This Webinterface application development is inspired by Machine Learning & Data Science youtube video Tutorial by codebasics
