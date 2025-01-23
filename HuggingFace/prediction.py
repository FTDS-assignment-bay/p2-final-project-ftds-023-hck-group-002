# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pickle

with open ('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open("test_data.pkl", "rb") as file:
    test = pickle.load(file)
    
test['date'] = pd.to_datetime(test['date'])

def forecast_demands(n_future_weeks, future_price_mean):   
    future_exog_vars = pd.DataFrame(future_price_mean, columns=['price_mean'])
    forecast = model.forecast(steps=n_future_weeks, exog=future_exog_vars)
    
    last_date = test['date'].iloc[-1]
    forecast_index = pd.date_range(start=last_date + pd.Timedelta(weeks=1), 
                                   periods=n_future_weeks, freq='W')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(forecast_index, forecast, label='Forecasted Units Sold', color='red', linestyle='--')
    ax.set_title('Forecast of Units Sold Over the Next Weeks')
    ax.set_xlabel('Date')
    ax.set_ylabel('Units Sold')
    ax.legend()
    ax.grid(True)
    
    return fig

def run():
    st.title("Stock Wise")
    st.write('---')
    lg ="mc_inv.jpg"
    st.image(lg, caption="Inventory management and demand forecasting")
    st.write('---')
    st.write('# Start Forecast')
    n_future_weeks = st.slider("Number of Weeks to Forecast", 1, 12, 4)
    
    future_price_mean = []
    for i in range(n_future_weeks):
        future_price_mean.append(st.number_input(f"Week {i+1} Price Mean", value=55.0, step=0.01))
    
    if st.button("## Generate Forecast"):
        # Generate forecast plot
        fig = forecast_demands(n_future_weeks, future_price_mean)
        st.pyplot(fig)

        # Create forecast dataframe
        forecast_index = pd.date_range(
            start=test['date'].iloc[-1] + pd.Timedelta(weeks=1), 
            periods=n_future_weeks, 
            freq='W'
        )

        # we need to extract the forecasted values from it
        forecast_values = list(map(int, [line.get_ydata() for line in fig.axes[0].lines][0]))

        forecast_df = pd.DataFrame({
            'Date': forecast_index,
            'Forecasted Units Sold': forecast_values
        })

        # Display forecast dataframe
        st.write(forecast_df)


if __name__ == "__main__":
    run()