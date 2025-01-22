#import libraries

import numpy as np
import pandas as pd
import streamlit as st
import pickle
# loading model
# with open('final_model.pkl', 'rb') as file:
#     model = pickle.load(file)
def run():

    st.title("Prediction of algorithm")
    st.write('---')

    st.write('### Overall 20 product Prediction for demand')
    st.image("overall 20 aggregate demand forecast.png", caption="Demand for 20 products predictions over time")

    st.write('''
        This plot shows that the model trained using XGBoost Regression. The average Error rate is 
        Mean Absolute Error: 8.303871111650215
        Root Mean Squared Error: 10.018814932940813
        meaning at most we have 8-10 products being under or over stocked!
    ''')

    
    st.write('### product 1 prediction Daily')
    st.image("pd1_df.png", caption="predicted demand for product 1")

    st.write('''
        This plot shows that the model trained using XGBoost Regression. The average Error rate is 
        8.748227856375955
        meaning at most we have 8 products being under or over stocked!

    ''')
    st.write('### predictions vs actual table')
    st.image("prediction.jpg", caption="predicted demand for product 1 vs actual demand")

    st.write('''
        This plot shows that the model trained using XGBoost Regression. The discrepency is better than before, meaning following this we can save more money since we wont have
        as much idle stock
    ''')



if __name__ == '__main__':
    run()
