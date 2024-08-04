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
with st.expander('data visuliation'):
    st.scatter_chart(data=data,x='bill_length_mm',y='body_mass_g',color='species')
    
