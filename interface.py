import pickle
pickle_in=open('windspeed1.pkl','rb')
clf=pickle.load(pickle_in)

import streamlit as st
import sklearn 
import pandas as pd
import numpy as np

st.header("Streamlined Wind Speed Forecasting: A Web-Based  Machine Learning Approach for Wind Mill Operators with  Real-Time data Data Using Streamlit")
st.sidebar.header('Input Parameters')
Maximum_Temperature = st.sidebar.number_input("Maximum Temperature", min_value=0, max_value=100, value=0)
Minimum_Temperature = st.sidebar.number_input("Minimum Temperature", min_value=0, max_value=100, value=0)
Dry_Bulb_Temperature = st.sidebar.number_input("Dry Bulb Temperature", min_value=0, max_value=100, value=0)
Wet_Bulb_Temperature = st.sidebar.number_input("Wet Bulb Temperature", min_value=0, max_value=100, value=0)
Dew_point_Temperature = st.sidebar.number_input("Dew point Temperature", min_value=0, max_value=100, value=0)

def predict(Maximum_Temperature,Minimum_Temperature,Dry_Bulb_Temperature,Wet_Bulb_Temperature,Dew_point_Temperature):
    prediction = clf.predict([[Maximum_Temperature,Minimum_Temperature,Dry_Bulb_Temperature,Wet_Bulb_Temperature,Dew_point_Temperature]])
    return int(prediction[0])

def interpret_wind_speed(wind_speed):
    if wind_speed < 15:
        return "Wind will blow at low level"
    elif 50 <= wind_speed <= 60:
        return "Wind will generate at full capacity"
    elif wind_speed > 80:
        return "Turn off wind mill"
    else:
        return "Wind speed is in a normal range"
        
#if st.button('Predict'):
    #prediction = predict(Maximum_Temperature,Minimum_Temperature,Dry_Bulb_Temperature,Wet_Bulb_Temperature,Dew_point_Temperature)
    #st.write('Predicted Target Value:', prediction)
if st.button('Predict'):
    prediction = predict(Maximum_Temperature, Minimum_Temperature, Dry_Bulb_Temperature, Wet_Bulb_Temperature, Dew_point_Temperature)
    interpretation = interpret_wind_speed(prediction)
    st.header('Predicted Wind Speed: ' + str(prediction) + ' km/hr')
    st.write('Interpretation:',interpretation)
    #st.title(interpretation)
