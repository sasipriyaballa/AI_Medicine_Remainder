import streamlit as st
import pandas as pd
import joblib

st.title("AI Based Medicine Reminder System")

# Load trained model
model = joblib.load("medicine_model.pkl")

st.header("Enter Patient Details")

age = st.number_input("Age", 1, 100)
medicine = st.text_input("Medicine Name")
day = st.selectbox("Day", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
time_input = st.time_input("Reminder Time")

if st.button("Predict Medicine Reminder"):

    input_data = pd.DataFrame({
        "age":[age],
        "medicine":[medicine],
        "day":[day]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Medicine should be taken")
    else:
        st.warning("Medicine not required")

    st.info(f"Reminder scheduled at {time_input}")
