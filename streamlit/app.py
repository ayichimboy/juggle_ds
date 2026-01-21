# import necessary libraries
import streamlit as st             
import pandas as pd                  
import numpy as np                               
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression   
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler   


# create entrypoint for the app
st.set_page_config(
    page_title = "Temperature Prediction App",
    page_icon = ":thermometer:",
    layout = "wide"
)


