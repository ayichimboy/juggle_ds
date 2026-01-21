# import libraries for analysis and visualization
import streamlit as st             
import pandas as pd                  
import numpy as np                               
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression   
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler                

# start building the data dashboard
st.set_page_config(layout= "centered", page_title="Weather Data Dashboard", page_icon=":sunny:")
st.title("Weather Data Dashboard :sunny:")


# Assuming the data is in a CSV file named 'weather_data.csv'
@st.cache_data
def load_data():
    data = pd.read_csv('weather_data.csv')
    return data

data = load_data()

#selece columns to analyze
data_drop = data.iloc[:, 1:5]

# convert date column to datetime format
data_drop['Date-Time (CDT)'] = pd.to_datetime(data_drop['Date-Time (CDT)'])

# rename columns for easier access
data_rename = data_drop.rename(columns={
                            'Date-Time (CDT)': 'date_time',
                            'Temperature   (°F)': 'temperature', 
                            'RH   (%)' : 'humidity',
                            'Dew Point   (°F)' :  'dew_point'
                            })

# clean data by dropping rows with missing values
data_clean = data_rename.dropna(subset= ['temperature', 'humidity', 'dew_point'])


# build a linear regression model to predict temperature based on humidity and dew point
X = data_clean[['humidity', 'dew_point']]
y = data_clean['temperature']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)

# calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

# data_clean = data_rename.dropna()

# Display the first few rows of the data
st.subheader("Data Overview")
st.write("This is a sample weather dataset containing various weather features.")

st.dataframe(data_rename.head())

# Display basic statistics of the data
st.subheader("Descriptive Statistics")
st.write("Here are some descriptivie statistics of the weather dataset.")
st.write(data_clean.describe().T)

# Display a histogram of the temperature feature
st.subheader("Feature Histogram Distribution")


# Display a histogram of the temperature feature
st.write("Here is a histogram of the temperature distribution in the dataset.")
fig, ax = plt.subplots(figsize=(10, 6))
data_clean['temperature'].hist(bins=30, ax=ax, color='skyblue', edgecolor='black')
# data_rename['temperature'].plot(kind='kde', ax=ax, color='red')
ax.set_title("Temperature Distribution")
ax.set_xlabel("Temperature (°F)")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Display a histogram of the humidity feature
st.write("Here is a histogram of the humidity distribution in the dataset.")
st.subheader("Humidity Distribution")
fig, ax = plt.subplots(figsize=(10,6))
ax.hist(x = data_rename['humidity'], bins=30, color='lightgreen', edgecolor='black')
ax.set_title("Humidity Distribution")
ax.set_xlabel("Humidity (%)")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Display a histogram of the dew point feature
# Display a histogram of the humidity feature
st.write("Here is a histogram of the dew point distribution in the dataset.")
st.subheader("Dew Point Distribution")
fig, ax = plt.subplots(figsize=(10,6))
ax.hist(x = data_rename['dew_point'], bins=30, color='red', edgecolor='black')
ax.set_title("Dew Point Distribution")
ax.set_xlabel("Dew Point (°F)")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Create 
