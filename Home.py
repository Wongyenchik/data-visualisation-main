import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import joblib
# Load the model
model = joblib.load('diabetes.joblib')

st.set_page_config(
    page_icon= "🩺",
    page_title= "Diabetes Analysis",
    layout="wide"
)
# st.markdown("<h4 style='color: grey; '></h4>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Diabetes Analysis 🩺</h1>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<h2 style='text-align: center; '>Topics</h2>", unsafe_allow_html=True)

# Point form using HTML unordered list
st.markdown("""
<ul >
  <li style="font-size: 20px;">Correlation between factors and diabetes outcome</li>
  <li style="font-size: 20px;">How does Pregnancy influence the risk of getting diabetes?</li>
  <li style="font-size: 20px;">How does Glucose influence the risk of getting diabetes?</li>
  <li style="font-size: 20px;">How does Blood Pressure influence the risk of getting diabetes?</li>
  <li style="font-size: 20px;">How does Skin Thickness influence the risk of getting diabetes?</li>
  <li style="font-size: 20px;">How does Insulin influence the risk of getting diabetes?</li>
  <li style="font-size: 20px;">How does BMI influence the risk of getting diabetes?</li>
  <li style="font-size: 20px;">How does DiabetesPedigreeFunction influence the risk of getting diabetes?</li>
  <li style="font-size: 20px;">How does Age influence the risk of getting diabetes?</li>
</ul>
""", unsafe_allow_html=True)


