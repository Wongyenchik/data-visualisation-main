import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import joblib

st.subheader("Correlation between factors and diabetes outcome")
st.markdown("###")
col1, col2 = st.columns(2)
with col1:
    image = Image.open('heatmap.png')
    st.image(image)  # Adjust the width parameter to make the image smaller

with col2:
    st.markdown("###")
    st.markdown("<p style='line-height: 40px;'>This diagram showed that Glucose has the highest correlation with diabetes outcome, follow by BMI, Age, Pregnancies, Skin Thickness, Insulin, Blood Pressure and Diabetes Pedigree Function.</p>", unsafe_allow_html=True)
st.markdown("###")
st.subheader("How does Pregnancy influence the risk of getting diabetes?")
st.markdown("The risk of getting diabetes tends to be lower with two or fewer pregnancies. With three to six pregnancies, the risk is moderate, but it increases significantly with more than six pregnancies.")
st.components.v1.html(open("pregnancies_diabetes_plot.html", 'r').read(), height=500)

st.subheader("How does Glucose influence the risk of getting diabetes?")
st.markdown("When glucose levels are 120 or lower, the likelihood of getting diabetes is low, but if they exceed this threshold, the risk of getting diabetes increases.")
st.components.v1.html(open("glucose_diabetes_plot.html", 'r').read(), height=500)

st.subheader("How does Blood Pressure influence the risk of getting diabetes?")
st.markdown("When Blood pressure are 68 or lower, the likelihood of getting diabetes is low, but if they exceed this threshold, the risk of getting diabetes increases.")
st.components.v1.html(open("blood_pressure_diabetes_plot.html", 'r').read(), height=500)

st.subheader("How does Skin Thickness influence the risk of getting diabetes?")
st.markdown("When Skin thickness are 28 or lower, the likelihood of getting diabetes is low, but if they exceed this threshold, the risk of getting diabetes increases.")
st.components.v1.html(open("skin_thickness_diabetes_plot.html", 'r').read(), height=500)

st.subheader("How does Insulin influence the risk of getting diabetes?")
st.markdown("When Insulin level are 100 or lower, the likelihood of getting diabetes is low, but if they exceed this threshold, the risk of getting diabetes increases.")
st.components.v1.html(open("insulin_diabetes_plot.html", 'r').read(), height=500)

st.subheader("How does BMI influence the risk of getting diabetes?")
st.markdown("When BMI level are 30 or lower, the likelihood of getting diabetes is low, but if they exceed this threshold, the risk of getting diabetes increases.")
st.components.v1.html(open("bmi_diabetes_plot.html", 'r').read(), height=500)

st.subheader("How does DiabetesPedigreeFunction influence the risk of getting diabetes?")
st.markdown("When DiabetesPedigreeFunction level are 0.5 or lower, the likelihood of getting diabetes is low, but if they exceed this threshold, the risk of getting diabetes increases.")
st.components.v1.html(open("pedigree_diabetes_plot.html", 'r').read(), height=500)

st.subheader("How does Age influence the risk of getting diabetes?")
st.markdown("People that is younger than 29 years old have a lower chance of getting diabetes.")
st.components.v1.html(open("age_diabetes_plot.html", 'r').read(), height=500)

