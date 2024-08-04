import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 first try of streamlit deployment')

st.write('Hello world! mustafa')
st.write('first try')
with st.expander('data'):
    data=pd.read_csv('penguins_cleaned.csv')
    data
    st.write(data.shape)
    st.write('***X***')
    X=data.drop('species',axis=1)
    X
    st.write('***y***')
    y=data['species']
    y
    st.text(data.columns)
with st.expander('data visuliation'):
    st.scatter_chart(data=data,x='bill_length_mm',y='body_mass_g',color='species')
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))
# Create a DataFrame for the input features
data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
input_df = pd.DataFrame(data, index=[0])
  
input_penguins = pd.concat([input_df, X], axis=0)
st.write('input data',input_df)
st.write('input penguins',input_penguins)
    
      


