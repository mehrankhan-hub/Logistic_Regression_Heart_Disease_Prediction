import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('framingham.csv')
#print(df)

with open('logReg.pkl', 'rb') as f:
    model = pkl.load(f)



st.title('HEART DISEASE RISK PREDICTION SYSTEM')
st.image("image.jpg",width=670)
st.subheader('This application predicts your risk of heart disease based on your health information.')

gender = st.radio('Gender (1 = Male, 0 = Female)',(1,0))
age = st.number_input('Age',0,100)
education = st.slider('Education (1 = No School, 2 = Elementary, 3 = High School, 4 = College+)',min_value=0,max_value=4,value=0)
currentsmoker = st.selectbox('Current Smoker (1 = Yes, 0 = No)',(0,1))
cigperday = st.number_input('Cigarettes Per Day',min_value=0,max_value=40,value=0)
BPMeds = st.selectbox('Blood Pressure Medication (1 = Yes, 0 = No)',(0,1))
preSrk = st.selectbox('Had a Stroke Before? (1 = Yes, 0 = No)',(0,1))
preHyp = st.selectbox('Do You Have High Blood Pressure? (1 = Yes, 0 = No)',(0,1))
diabets = st.selectbox('Do You Have Diabetes? (1 = Yes, 0 = No)',(0,1))
totcol = st.number_input('Total Cholesterol (60–700 mg/dL)',min_value=60,max_value=700,value=60)
sysBP = st.number_input('Systolic Blood Pressure (70–350 mmHg)',min_value=70,max_value=350,value=70)
diaBP = st.number_input('Lower (Diastolic) Blood Pressure (40–180 mmHg)',min_value=40,max_value=180,value=40)
BMI = st.number_input('Body Mass Index (BMI) (18.0–80.0 kg/m²)',min_value=18.0,max_value=80.0,value=18.0)
heartrate = st.number_input('Heart Rate (30–150 BPM)',min_value=30,max_value=150,value=30)
glucose =st.number_input('Blood Glucose Level (40–400 mg/dL)',min_value=40,max_value=400,value=40)
x_value = pd.DataFrame({
    'male':[gender],'age':[age],'education':[education],'currentSmoker':[currentsmoker],
    'cigsPerDay':[cigperday],'BPMeds':[BPMeds],'prevalentHyp':[preHyp],'prevalentStroke':[preSrk],
    'diabetes':[diabets],'totChol':[totcol],'sysBP':[sysBP],'diaBP':[diaBP],'BMI':[BMI],
    'heartRate':[heartrate],'glucose':[glucose]
})

def footer():
    st.write("---")
    st.write("Heart Disease Prediction System")
    st.write("Developed by MEHRAN KHAN")
    st.write("© 2026 All Rights Reserved")

st.subheader('Input send to the Pipeline')
st.table(x_value)


if st.button('Predict'):
    prediction = model.predict(x_value)
    if prediction == 1:
        st.success('🎉 Congratulations! No Evidence of Heart Disease Detected.')
    else:
        st.error('😔 We are sorry. Heart Disease Risk Found.')

footer()


st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #FFFFFF;
}

/* Overall text color */
.stApp, 
.stApp p,
.stApp span,
.stApp label,
.stApp div,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.60), rgba(0,0,0,0.60)),
        url("https://images.unsplash.com/photo-1576091160550-2173dba999ef");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
""", unsafe_allow_html=True)




st.markdown("""
<style>
.stButton > button {
    background-color: white !important;
    color: black !important;
}

.stButton > button p {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)





