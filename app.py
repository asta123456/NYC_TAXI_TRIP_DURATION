import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("taxi_model.pkl", "rb"))

st.title("Taxi Trip Duration Prediction")

passenger_count = st.number_input("Passenger Count")
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
hour = st.number_input("Pickup Hour")

if st.button("Predict"):
    data = np.array([[passenger_count, pickup_longitude, pickup_latitude,
                      dropoff_longitude, dropoff_latitude, hour]])
    
    prediction = model.predict(data)
    
    st.success(f"Estimated Trip Duration: {prediction[0]} seconds")