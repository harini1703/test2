import pickle
pickle_in=open("windspeed1.pkl",'rb')
clf=pickle.load(pickle_in)

import streamlit as st
import numpy as np
import pandas as pd

st.title("Wind speed prediction")
