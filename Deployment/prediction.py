#import libraries

import numpy as np
import pandas as pd
import streamlit as st
import pickle
# loading model
with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)
def run():
    st.title("Are you at risk of being Obese")
    st.write('---')

    # Set Banner
    link = 'https://gardapublik.id/wp-content/uploads/2024/07/maxresdefault.jpg'
    st.image(link, 
            caption= "source: Nikakado Avocado")
    st.write("This page aims to help diagnosticians identify possible obese or at obese at risk individuals")
    #make form
    with st.form(key= 'form parameters'):
        gender = st.selectbox('Gender:', ('Female', 'Male'))
        age = st.number_input('Age:', min_value=0, max_value=100, value=21)
        height = st.slider('Height (in meters):', min_value=1.0, max_value=2.5, value=1.62)
        weight = st.slider('Weight (in kg):', min_value=30, max_value=200, value=64)
        family_history_with_overweight = st.selectbox('Family History with Overweight:', ('yes', 'no'))
        favc = st.selectbox('FAVC:', ('yes', 'no'))
        fcvc = st.number_input('FCVC:', min_value=1.0, max_value=5.0, value=2.0)
        ncp = st.number_input('NCP:', min_value=1.0, max_value=5.0, value=3.0)
        caec = st.selectbox('CAEC:', ('Always', 'Frequently', 'Sometimes', 'no'))
        smoke = st.selectbox('SMOKE:', ('yes', 'no'))
        ch2o = st.number_input('CH2O:', min_value=0.0, max_value=5.0, value=2.0)
        scc = st.selectbox('SCC:', ('yes', 'no'))
        faf = st.number_input('FAF:', min_value=0.0, max_value=5.0, value=0.0)
        tue = st.number_input('TUE:', min_value=0.0, max_value=5.0, value=1.0)
        calc = st.selectbox('CALC:', ('no', 'Sometimes', 'Frequently', 'Always'))
        mtrans = st.selectbox('MTRANS:', ('Public_Transportation', 'Walking', 'Automobile', 'Motorbike','Bike'))


        submit = st.form_submit_button('submit button')
    #saving data in form of dict to be made into pd for inferencing
    data = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans,
    }
    data = pd.DataFrame([data])
    st.dataframe(data)

    if submit:
        result = model.predict(data)
        st.write(f"### result : {str(result[0])}")
    #action trigger for showing
#to check whether it should run if not in main
if __name__ == '__main__':
    run()
