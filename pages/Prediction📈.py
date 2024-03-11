import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import joblib
# Load the model
model = joblib.load('diabetes.joblib')

st.subheader("Prediction")
def predict_outcome(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
    st.markdown("<h3>Result</h3>", unsafe_allow_html=True)

    # Make prediction
    user_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
    prediction = model.predict(user_data)

    # Display the prediction
    if prediction == 0:
        st.write("<p style='color: green;'>Low risk getting diabetes</p>", unsafe_allow_html=True)
    else:
        st.write("<p style='color: red;'>High risk getting diabetes</p>", unsafe_allow_html=True)
        st.markdown("<h4>Reason</h4>", unsafe_allow_html=True)
        if pregnancies > 3:
            st.markdown("<p>Pregnancies: High risk</p>", unsafe_allow_html=True)
        if glucose > 177:
            st.markdown("<p>Glucose: High risk</p>", unsafe_allow_html=True)
        if blood_pressure > 68:
            st.markdown("<p>Blood pressure: High risk</p>", unsafe_allow_html=True)
        if skin_thickness > 28:
            st.markdown("<p>Skin thickness: High risk</p>", unsafe_allow_html=True)
        if insulin > 100:
            st.markdown("<p>Insulin: High risk</p>", unsafe_allow_html=True)
        if bmi > 30:
            st.markdown("<p>BMI: High risk</p>", unsafe_allow_html=True)
        if diabetes_pedigree_function > 0.5:
            st.markdown("<p>Diabetes pedigree function: High risk</p>", unsafe_allow_html=True)
        if age > 29:
            st.markdown("<p>Age: High risk</p>", unsafe_allow_html=True)

def main():
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.slider('Pregnancies', 0, 15, 8)
        skin_thickness = st.slider('Skin Thickness', 0, 100, 50)
        diabetes_pedigree_function = st.slider('Diabetes Pedigree Function', 0.0, 2.4, 0.3)

    with col2:
        glucose = st.slider('Glucose', 0, 200, 100)
        insulin = st.slider('Insulin', 0, 900, 100)
        age = st.slider('Age', 0, 100, 20)

    with col3:
        blood_pressure = st.slider('Blood Pressure', 0, 130, 70)
        bmi = st.slider('BMI', 0, 70, 30)

    if st.button("Predict"):
        if not pregnancies or not glucose or not blood_pressure or not skin_thickness or not insulin or not bmi or not diabetes_pedigree_function or not age:
            st.error("Please fill in all fields before predicting.")
        else:
            predict_outcome(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)

# Call the function to get user input and make predictions
main()