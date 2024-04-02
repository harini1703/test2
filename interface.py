import pickle
pickle_in=open('windspeed1.pkl','rb')
clf=pickle.load(pickle_in)

import streamlit as st
import sklearn 
import pandas as pd
import numpy as np

st.title(" WIND SPEED PREDICTION")
st.sidebar.header('Input Parameters')
feature_input = st.sidebar.number_input("Feature Value", min_value=0.0, max_value=100.0, value=50.0)

