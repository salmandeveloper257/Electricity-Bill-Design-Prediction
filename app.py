!pip install streamlit
import streamlit as st
import pandas as pd
import joblib
model1 = joblib.load('model.pickle')
st.title("Electricity Bill Design Prediction")
units = st.number_input("Total Units", min_value=0, max_value=1000, value=500)
price_per_unit = st.number_input("Unit Price", min_value=0.0, max_value=100.0, value=20.0)
fpa = st.number_input("Fixed Price Adjustment", min_value=0.0, max_value=100.0, value=10.0)
tax = st.number_input("Tax", min_value=0.0, max_value=100.0, value=10.0)
fixed_charges = st.number_input("Fixed Charges", min_value=0.0, max_value=1000.0, value=500.0)

if st.button("Predict Price"):
       input_data_all_columns = pd.DataFrame(
        [[units, price_per_unit, fpa, tax, fixed_charges]],
        columns=['Units', 'Price Per Unit', 'FPA', 'Tax', 'Fixed Charges']
    )
       prediction = model1.predict(input_data)
       st.success(
        f"Estimated Price: {prediction[0]:,.2f}"
    )
