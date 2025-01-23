import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():

    lg ="the-10-best-minecraft-memes-from-reddit_kgh3.2560.webp"
    st.image(lg, caption="Inventory management and demand forecasting")


    st.title('Exploratory Data Analysis (EDA)')
    st.write('## Retail Store Inventory Analysis')

    # Load and display data
    st.write('### Dataset Overview')
    data = pd.read_csv('retail_store_inventory.csv')
    st.dataframe(data.head())

    # Inventory vs Units Sold Plot
    st.write('### Demand over time(weeks)')
    st.image("plot_1.png", caption="Demand over time (Weekly)")

    st.write('''
    The graph shows how demand fluctuates for product 1 over time. It can be inferred that the demand of the products fluctuate wildly in between weeks with the average being about 1000 units sold. A reason could be due to the product being produce meaning people might buy it when it is restocked at certain dates for freshness.
    ''')

    st.write('### Inventory vs Units Sold')
    st.image("plot_3.png", caption="Inventory levels vs Units sold (Weekly)")

    st.write('''
    This graph showcases the weekly trend of inventory levels and units sold. High peaks in inventory suggest replenishment 
    activities, while dips in the "Units Sold" line may indicate low demand periods. From the following we can see a constant discrepency with the stock available and its demand meaning we are way overstocked
    ''')

    # Feature Importance Plot
    st.write('### Feature Importance')
    st.image("plot_2.png", caption="Feature importance for units sold")

    st.write('''
    This plot highlights the most significant features contributing to the demand forecasting model. 
    Inventory levels dominate in importance, followed by price, competitor pricing, unit orders, and discounts.
    The reason why inventory level is the highest is because it follows the units sold 
                    ''')

#checks whether to run if not in main
if __name__ == '__main__':
    run()
