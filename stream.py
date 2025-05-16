import pandas as pd  
import numpy as np                    
import matplotlib.pyplot as plt                                                               
import streamlit as st 


# read data/ import data
# df = pd.read_csv('C:\Users\Owner\juggle_ds\juggle_ds\dev_space\data\iris.csv')

# streamlit setup 
st.markdown('# Data Dashboard')
st.header('Ambigious')
st.subheader('travel to mars')
st.caption('poop')

# display code 
code_snippet = """
def green(x):
    if x = 'green':
        print('the color green')
    else:
        print('something else')
    
"""
st.code(code_snippet, language='python')

fruits = ['orange', 'mango', 'apples', 'pinneaple']
select_fruits = st.selectbox(label='Fruits',
                             options=fruits,
                             help='select fruit type',
                             key='fruit_list')

# Multiple select feature
multi_fruits = st.multiselect(label='Many Fruits',
                              options = fruits,
                              help='many favourites',
                              max_selections=2,
                              placeholder='select fruit',
                              )

# slider widget
basic_slider = st.slider(
                            label='Basic level',
                            min_value=1,
                            max_value=100,
                            value=70
)
st.write('Selected Number : {}'.format(basic_slider))

# slider widget
step_slider = st.slider(
                            label='Float level',
                            min_value=1.0,
                            max_value=10.0,
                            step=0.5,
                            value=3.0
)
st.write('Selected Number : {}'.format(step_slider))

# Number input widget
