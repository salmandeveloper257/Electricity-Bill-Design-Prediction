import streamlit as st
import pandas as pd
import joblib

# 1. پیج کی ترتیبات (Page Setup)
st.set_page_config(
    page_title="Electricity Bill Predictor",
    page_icon="⚡",
    layout="centered"
)

# 2. ماڈل لوڈ کریں
model1 = joblib.load('model.pickle')

# 3. عنوان اور بینر
st.title("⚡ Electricity Bill Estimator")
st.write("Please fill in the box below to calculate your bill:")

# خوبصورت تصویر (Banner Image)
st.image("https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800", use_container_width=True)

st.divider()

# 4. ان پٹ فیلڈز کو 2 کالموں میں تقسیم کرنا
col1, col2 = st.columns(2)

with col1:
    units = st.number_input("Total Units", min_value=50, max_value=1000, value=800)
    price_per_unit = st.number_input("Unit Price", min_value=10, max_value=100.0, value=80)
    fpa = st.number_input("Fixed Price Adjustment", min_value=100, max_value=2000.0, value=1700)

with col2:
    tax = st.number_input("Tax", min_value=300, max_value=8000.0, value=5500)
    fixed_charges = st.number_input("Fixed Charges", min_value=100, max_value=1000, value=800)

st.write("")

# 5. بٹن اور پرڈکشن کا ڈسپلے
if st.button("Calculate Bill 💡", type="primary", use_container_width=True):
    input_data = pd.DataFrame(
        [[units, price_per_unit, fpa, tax, fixed_charges]],
        columns=['Units', 'Price Per Unit', 'FPA', 'Tax', 'Fixed Charges']
    )
    
    prediction = model1.predict(input_data)
    
    st.balloons() # جشن کی اینیمیشن
    st.metric(label="Estimated Total Price", value=f"PKR {prediction[0]:,.2f}")

