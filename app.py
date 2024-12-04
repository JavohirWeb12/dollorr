import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Modelni yuklash
model = joblib.load('usd_forecast_model.pkl')

# Streamlit ilovasining sarlavhasi
st.title("Dollar Kursini Bashorat Qilish")

# Foydalanuvchidan yangi ma'lumotlarni olish
inflation_rate = st.number_input("Inflatsiya darajasi (%)", min_value=0.0, max_value=100.0, value=15.0)
interest_rate = st.number_input("Foiz stavkasi (%)", min_value=0.0, max_value=100.0, value=10.0)
oil_price = st.number_input("Neft narxi ($)", min_value=0.0, max_value=500.0, value=50.0)
other_factors = st.number_input("Boshqa omillar", min_value=0.0, max_value=10.0, value=3.0)

# Bashorat qilish uchun yangi ma'lumotni tayyorlash
new_data = np.array([[inflation_rate, interest_rate, oil_price, other_factors]])

# Agar foydalanuvchi "Bashorat qilish" tugmasini bossa
if st.button("Bashorat qilish"):
    # Bashorat qilish
    predicted_value = model.predict(new_data)
    
    # Natijani chiqarish
    st.write(f"Bashorat qilingan USD/UZS kursi: {predicted_value[0]:.2f}")
