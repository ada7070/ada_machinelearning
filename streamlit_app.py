import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 first try of streamlit deployment')

st.write('Hello world! mustafa')
st.write('first try')
with st.expander('data'):
    data=pd.read_csv('penguins_cleaned.csv')
    st.write(data)
    st.write(data.shape)
