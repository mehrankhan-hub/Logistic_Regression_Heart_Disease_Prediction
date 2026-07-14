import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('framingham.csv')
#print(df)

with open('logReg.pkl', 'rb') as f:
    model = pkl.load(f)

st.title('HEART DISEASE PREDICTION')
st.image("image.jpg",width=600)
st.subheader('This prediction predict whether you have Heart Disease or Not')

gender = st.radio('Gender',(1,0))
age = st.number_input('Age',0,100)
education = st.slider('Enter your Education (Between 1-4)',min_value=0,max_value=4,value=0)
currentsmoker = st.selectbox('Current Smoker',(0,1))
cigperday = st.number_input('Cigper Day',min_value=0,max_value=40,value=0)
BPMeds = st.selectbox('BPMeds',(0,1))
preSrk = st.selectbox('Pre-Srk',(0,1))
preHyp = st.selectbox('Pre-Hyp',(0,1))
diabets = st.selectbox('Diabetes',(0,1))
totcol = st.number_input('Total Cholestrol (between 60-700)',min_value=60,max_value=700,value=60)
sysBP = st.number_input('SysBP (between 70-350)',min_value=70,max_value=350,value=70)
diaBP = st.number_input('DiaBP (between 40-180)',min_value=40,max_value=180,value=40)
BMI = st.number_input('BMI (between 18.0-80.0)',min_value=18.0,max_value=80.0,value=18.0)
heartrate = st.number_input('Heartrate (between 30-150)',min_value=30,max_value=150,value=30)
glucose =st.number_input('Glucose (between 40-400)',min_value=40,max_value=400,value=40)
x_value = pd.DataFrame({
    'male':[gender],'age':[age],'education':[education],'currentSmoker':[currentsmoker],
    'cigsPerDay':[cigperday],'BPMeds':[BPMeds],'prevalentHyp':[preHyp],'prevalentStroke':[preSrk],
    'diabetes':[diabets],'totChol':[totcol],'sysBP':[sysBP],'diaBP':[diaBP],'BMI':[BMI],
    'heartRate':[heartrate],'glucose':[glucose]
})

def footer():
    st.write("---")
    st.write("Heart Disease Prediction System")
    st.write("Developed by Mehran")
    st.write("© 2026 All Rights Reserved")

st.subheader('Input send to the Pipeline')
st.table(x_value)


if st.button('Predict'):
    prediction = model.predict(x_value)
    if prediction == 1:
        st.success('Patient has heart disease')
    else:
        st.error('NO Heart disease')

footer()







