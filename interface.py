import pickle
pickle_in=open('windspeed1.pkl','rb')
clf=pickle.load(pickle_in)

import streamlit as st
import sklearn as 
import pandas as pd
import numpy as np

st.title(" WIND SPEED PREDICTION")
