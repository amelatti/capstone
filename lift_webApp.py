import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import _pickle as pickle

#Lay out web app frameowkr using streamlit st tags (title, write, image)

st.title('Weightlifting Max Potential Lift Calculator - Use this to motivate you to work for what is possible!')
st.write('Enter your information below to receive an estimate of what your max potential lifts could be, with the right time and hard work of course!')
# Image obtained from https://unsplash.com/photos/WvDYdXDzkhs free to use under the unsplash license.
image = Image.open('./victor-freitas-WvDYdXDzkhs-unsplash.jpg')
st.image(image, use_column_width=True)

# Import the pickle model for each lift that has been saved from weightlifting_analysis_and_modelling_060123.ipynb
with open('./squat_model.pkl','rb') as file:
  squat_model = pickle.load(file)

with open('./deadlift_model.pkl','rb') as file:
  deadlift_model = pickle.load(file)

with open('./bench_model.pkl','rb') as file:
  bench_model = pickle.load(file)

# Function to estimate lift weights after users provide their information

def liftEstimate(user_inputs_df):
  '''
  Function to estimate lift weights for squat, deadlift, and bench after users provide their information in the web app
  Inputs:
  user_inputs - all of the user inputs combined in one row of a pandas dataframe; consisting of:
    user_age - (int) in years
    user_weight - (float) in lb
    user_commitment - (int) value between 1 and 10 for user's self-evaluated commitment to lifting
    user_equip - vector of 0s and 1s reflecting the type of equipment the user selected.
  Outputs:
  Estimated max lift weights for squat, deadlift, and bench (int)
  
  '''

  # create test vector from user's inputs to run the model on for a prediction
  # test_vec = np.array([[user_age, user_weight, user_commitment, user_equip]])

  # get estimated lift weight from the model
  squat_est = squat_model.predict(user_inputs_df)
  deadlift_est = deadlift_model.predict(user_inputs_df)
  bench_est = bench_model.predict(user_inputs_df)

  return int(round(squat_est[0][0] * 2.205 ,0)), int(round(deadlift_est[0][0] * 2.205 ,0)), int(round(bench_est[0][0] * 2.205,0))

# ------------------------------------------------------------------------

# Getting the user inputs via streamlit web app number_input() and selectbox():
user_age = st.number_input("Enter your age", value=0)
user_weight = (st.number_input("Enter your body weight (in lbs)", value=0)) / 2.205 # Converting back to kg for model, start with lbs assuming our users will be in the US
user_commitment = st.number_input("Enter your commitment level (1 being lowest, 10 being highest!)", value=0)
user_sex = st.selectbox("Choose your sex from the dropdown box", ("Male","Female"))
user_equip = st.selectbox("Choose your typical workout equipment from the dropdown box", ("None","Wraps","Single-Ply Lifting Suit", "Multi-Ply Lifting Suit"))

# Massaging user inputs to the right format to use in the model
# User equipment depends on what key word is selected, then split into the values that we created dummies for!
if user_equip == 'None':
  equip_raw = 1
  equip_single = 0
  equip_wraps = 0
elif user_equip == 'Wraps':
  equip_raw = 0
  equip_single = 0
  equip_wraps = 1
elif user_equip == 'Single-Ply Lifting Suit':
  equip_raw = 0
  equip_single = 1
  equip_wraps = 0
else:
  equip_raw = 0
  equip_single = 0
  equip_wraps = 0

# User sex is also key word based
if user_sex == 'Male':
  user_sex = 1
else: 
  user_sex = 0


# Push to start the lift calculation
button = st.button("Click to estimate your potential max lifts!")

# Run the following when the calculate button is pressed
if button:
  with st.spinner ('Calculating your max potential lifts...'):
    # With the calculation started, we will join the user inputs to a vector and then append it to our df_user_input dataframe to run in the estimator
    user_vec = np.array([user_age, user_weight, user_commitment, user_sex, equip_raw, equip_single, equip_wraps])

    # Creating the df to handle user inputs
    df_cols = ['Age','BodyweightKg','Commitment','Sex_M','Equipment_Raw','Equipment_Single-ply','Equipment_Wraps']
    df_user_input = pd.DataFrame(columns=df_cols)

    # Add single row to the df with all the inputs.
    df_user_input.loc[len(df_user_input)] = user_vec

    # Run estimate function with model to get our three lift estimates
    squat_est, deadlift_est, bench_est = liftEstimate(df_user_input)

    st.success("Max Potential Lifts Estimated!")
    st.balloons()
    st.write("Max Potential Squat= ", squat_est, "lbs, Max Potential Dead lift=", deadlift_est, "lbs, Max Potential Bench Press=", bench_est)