# Udacity Data Science Nanodegree Capstone Project
Weightlifting Potential Predictor Web App
 
### Table of Contents

0. [Project Definition](#summary)
1. [Installation](#installation)
2. [File Descriptions](#files)
3. [How to Use](#use)
4. [Analysis](#analysis)
5. [Conclusion](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Project Definition <a name="summary"></a>

One of my passions in life is weight lifting for strength and fitness.
I believe that a lot of people have a difficult time getting into consistent weight lifting because they don't know what their end goals may look like.
It's one thing to say "I want to get stronger," but it's more impactful and sets more accountability to say "I have a realistic long term goal of doing a 200 kg bench press."
To solve this problem of people lacking clear goals and/or motivational targets for their personal health in weightlifting I decided to use the powerlifting-database from Kaggle to do the following:

1. Perform high level data cleaning + analysis for lift weight capability vs. other information about the people included in the dataset.
2. Build machine learning models to predict what a maximum lift weight could be for a user based on their characteristics. The model will be trained on a subset of the data and then tested for accuracy on a test set of the data.
3. Build a plotly web app that can be easily hosted on a local machine to act as a GUI for the saved machine learning models. A user of the web app can enter in their characteristics and receive a predicted maximum lift weight that they could set as a future achievable goal.

## Installation <a name="installation"></a>

Necessary libraries to run the streamlit web app include: streamlit, pandas, numpy, PIL, and pickle.  
Necessary libraries to run the analysis + ML Model creation in jupyter notebook include: pandas, numpy, scipy, sklearn, matplotlib, seaborn, plotly, pickle
All code has been run on Python 3.8.

## File Descriptions <a name="files"></a>

1) .ipynb file weightlifting_analysis_and_modelling_060123.ipynb that is used to open the openpowerlifting.csv dataset, clean and analyze the code, then create and save the ML models from the data.
2) .py file lift_webApp.py includes the code that is used to host the streamlit web app for a direct user interface that uses the ML models (.pkl) to estimate lift capability.
3) .csv file openpowerlifting.csv includes the powerlifting dataset (obtained from Kaggle under free use - https://www.kaggle.com/datasets/dansbecker/powerlifting-database)
4) .jpg file victor-freitas-WvDYdXDzkhs-unsplash.jpq is a free licensed image obtained from Unsplash (https://unsplash.com/photos/WvDYdXDzkhs)
5) .pkl files bench_model.pkl, deadlift_model.pkl, squat_model.pkl that are the exported ML models of the openpowerlifting.csv created in weightlifting_analysis_and_modelling_060123.ipynb and hosted in lift_webApp.py


## How to Use <a name="use"></a>

In a Conda command terminal run the following:
1) Activate your conda environment that contains the above libraries mentioned for the streamlit web app
    'conda activate <your_environment_here>'
2) Save all the .pkl files and the lift_webApp.py to a location on your machine, then navigate to the directory that they're saved in.
     'cd <your_directory_location_here>'
3) Enter the command into the Conda terminal to run the web app and it should appear in your browser. (Or copy and paste the host url info from the command terminal that appears into a browser)
    'streamlit run lift_webApp.py'.

## Analysis<a name="analysis"></a>

The key analysis and graphs can be found in the jupyter notebook weightlifting_analysis_and_modelling_060123.ipynb. However, some summaries of the analysis..
1) Cleaning data - Some values for lift weights and body weights were accidentally entered in as negative numbers. I opted to remove these entirely, but a possible alternate approach was to assume that they should be converted to positive numbers and left in the dataset.  I also opted to remove rows of data that were missing any of the three key lift weights. An alternate method here would have been to do some extrapolation of missing lift weights based on existing ones. For example, if person A lifted 300 kg squat, 350 kg deadlift, but had a missing bench value, it could have been an option to extrapolate an estimated bench value of 200kg to allow that data row to be complete.
2) High level analysis - The data showed fairly normal distributions for max lift weights between male and female competitors. The lifts for the males had higher mean values than the lifts for the females. I added a "commitment level" column and the goal is to see if somebody who is more "committed" ( attends more events = more name entries) will have heavier max lifts (and subsequently to use that as a potential predictor in the ML models). It is difficult to tell due to less data in the higher commitment range, but the results of squats seemed to have some increase in mean lift kg vs. commitment level. Additionally, a 3d scatterplot was created to give an understanding of body weight and age's impact on max squats for male participants. As would be expected, the highest squat values clustered around a 20-30 age range with 100-150kg body weight. Lifts definitely saw a decline with additional age.


## Conclusion<a name="results"></a>

The key modelling results of the project can be found in the application and jupyter notebook, however there are a few things to note:
1) Modelling Results - Two optimized models were created via Pipeline and CVGridSearch. build_model() = standard scaler and an ElasticNet classifier, and build_model_2() = MinMax scaler and a PLS (Partial Least Squares) regression classifier. The models were trained and then tested, with results compared in a table via negative mean squared error. Ultimately they were very similar but Model 2 had slightly less error and was chosen as the set of lift models to export for the web app.
2) Justification - Looking at some of the results, the value of ~1696 mean sq error for squats means that, on average, the predicted lift is off from the test lift value by about 41 kg. This is not perfect, of course, but it starts getting us into the ballpark when squat lifts can go all the way up to 500 kg! It is interesting to note that our mean squared error was lower for Bench than the other two. Does that mean that the model was predicting bench better? Or was bench simply a lower average value to begin with, so that the mean squared error would naturally drop. The linear regression model chosen for use is fitted well as it correctly gives higher lifts to heavier body weight, higher commitment, and male. However, the model biases that younger age will lift more, 9 year old ends up lifting more than 35 year old. This would need to be improved in future with a polynomial regression model to account for a decrease in lifts on the lower side of ~20-30 years old. (There would be a peak at 20-30 years old and then downward slopes on each side)
3) Web App Results - The web app functions perfectly well for its purpose. Upon entering their age, body weight, perceived commitment level, sex, and equipment type, anybody can receive their predicted maximum potential lifts that they can aspire to reach in the long term. The app interface is very straightforward, with some drop down boxes for string selection choices so users don't have to type specific items (and risk incorrect entries that cause errors). A workout themed graphic + fun balloons popping up when a user activates the model prediction set a nice touch for the app.

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

The Udacity Data Science Course provided some examples throughout the course that helped with my project development. Please consider checking out the course if you found this project interesting. [here](https://www.udacity.com/courses/all?utm_source=gsem_brand&utm_medium=ads_r&utm_campaign=747168232_c_individuals&utm_term=126315200811&utm_keyword=udacity_e&gclid=CjwKCAjw586hBhBrEiwAQYEnHVqnxwSRVfaDb53lwF5Fa3Jx1xeR7nfh3ZokP82uTh0IFPzLBeHE0RoC5RsQAvD_BwE).

Kaggle's powerlifting-database dataset can be found [here](https://www.kaggle.com/datasets/dansbecker/powerlifting-database)

The image for the web app was freely licensed at Unsplash and can be found [here](https://unsplash.com/photos/WvDYdXDzkhs)
As for my personal code, you can use it to your heart's content!