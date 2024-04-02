import pickle
pickle_in=open('windspeed1.pkl','rb')
clf=pickle.load(pickle_in)

import streamlit as st
import sklearn 
import pandas as pd
import numpy as np

st.title(" WIND SPEED PREDICTION")
st.sidebar.header('Input Parameters')
Maximum_Temperature = st.sidebar.number_input("Maximum Temperature", min_value=0, max_value=100, value=0)
Minimum_Temperature = st.sidebar.number_input("Minimum Temperature", min_value=0, max_value=100, value=0)
Dry_Bulb_Temperature = st.sidebar.number_input("Dry Bulb Temperature", min_value=0, max_value=100, value=0)
Wet_Bulb_Temperature = st.sidebar.number_input("Wet Bulb Temperature", min_value=0, max_value=100, value=0)
Dew_point_Temperature = st.sidebar.number_input("Dew point Temperature", min_value=0, max_value=100, value=0)


