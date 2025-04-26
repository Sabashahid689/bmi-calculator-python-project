import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight (in kg):", min_value=0.0)
height = st.number_input("Enter your height (in meters):", min_value=0.0)

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
    else:
        st.error("Height must be greater than 0.")