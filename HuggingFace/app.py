import streamlit as st
import eda 
import prediction
#immediately runs both in that order, so we cant do it right away but modular

#navigation
navigation = st.sidebar.selectbox("select page : ", ('EDA','Predictor'))

#check which page to run as a function
if navigation == 'Predictor':
    prediction.run()
else:
    eda.run()
