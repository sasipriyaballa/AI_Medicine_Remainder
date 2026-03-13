import streamlit as st
import pickle
import pandas as pd
import time
from plyer import notification
from threading import Thread

# -----------------------------
# Load trained ML model
# -----------------------------
model = pickle.load(open("model.pkl","rb"))
med_encoder = pickle.load(open("medicine_encoder.pkl","rb"))
cond_encoder = pickle.load(open("condition_encoder.pkl","rb"))
status_encoder = pickle.load(open("status_encoder.pkl","rb"))

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("AI Medicine Reminder & Prediction System")

st.write("Enter your medicine details below")

# User inputs
medicine = st.selectbox("Medicine Name", med_encoder.classes_)
age = st.number_input("Age",20,100)
condition = st.selectbox("Health Condition", cond_encoder.classes_)
time_input = st.text_input("Reminder Time (HH:MM)","08:00")

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Medicine Adherence"):

    hour = int(time_input.split(":")[0])

    med_encoded = med_encoder.transform([medicine])[0]
    cond_encoded = cond_encoder.transform([condition])[0]

    input_data = pd.DataFrame({
        "medicine_name":[med_encoded],
        "age":[age],
        "condition":[cond_encoded],
        "hour":[hour]
    })

    prediction = model.predict(input_data)
    result = status_encoder.inverse_transform(prediction)

    st.success("Prediction: " + result[0])


# -----------------------------
# Reminder Notification
# -----------------------------
def send_reminder(medicine):
    
    notification.notify(
        title="Medicine Reminder",
        message=f"Time to take your medicine: {medicine}",
        timeout=10
    )


# -----------------------------
# Schedule Reminder
# -----------------------------
if st.button("Set Reminder"):

    schedule.every().day.at(time_input).do(send_reminder, medicine)

    st.success(f"Reminder set for {medicine} at {time_input}")


# -----------------------------
# Background Scheduler
# -----------------------------
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(30)

thread = Thread(target=run_scheduler)
thread.daemon = True
thread.start()
