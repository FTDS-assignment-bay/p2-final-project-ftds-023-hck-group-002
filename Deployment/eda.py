#import libraries

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    st.title('EDA')
    st.write(' ### Header 2')
    #image loading
    lg ="mc_inv.jpg"
    st.image(lg
    , caption= "Inventory management and demand forecasting")

    st.write('### DF')
    data = pd.read_csv('retail_store_inventory.csv')
    st.dataframe(data)

    ################################################## PIE CHART Section
    #selection box to filter target

    lg ="plot_1.png"
    st.image(lg
    , caption= "Inventory management and demand forecasting")
        
    st.write('''
    From the following, a general pattern can be seen that fitter, less obese people tend to use mrore physical transportation(walking or biking than obese people,
    the outreach program or ad could thus promote walking or biking programs as a way to comute to school or to advertise on public transport)
    ''')

    
    lg ="plot_2.png"
    st.image(lg
    , caption= "Inventory management and demand forecasting")
        
    st.write('''
    From the following, a general pattern can be seen that fitter, less obese people tend to use mrore physical transportation(walking or biking than obese people,
    the outreach program or ad could thus promote walking or biking programs as a way to comute to school or to advertise on public transport)
    ''')

    
    lg ="plot_2.png"
    st.image(lg
    , caption= "Inventory management and demand forecasting")
        
    st.write('''
    From the following, a general pattern can be seen that fitter, less obese people tend to use mrore physical transportation(walking or biking than obese people,
    the outreach program or ad could thus promote walking or biking programs as a way to comute to school or to advertise on public transport)
    ''')
#checks whether to run if not in main
if __name__ == '__main__':
    run()