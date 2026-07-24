import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
import sqlite3
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('framingham.csv')
#print(df)
with open('logReg.pkl', 'rb') as f:
    model = pkl.load(f)

conn = sqlite3.connect('framingham.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS framingham_table(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT,MALE TEXT,AGE INTEGER,EDUCATION INTEGER,CURRENT_SMOKER INTEGER,CIGSPERDAYS INTEGER,
BP_MEDICATION INTEGER,HAD_A_STROKE INTEGER,HIGH_BP INTEGER,DIABETES INTEGER,CHOLESTEROL INTEGER,
SYSTOLIC_BP REAL,DIASTOLIC_BP INTEGER,BMI REAL,HEART_RATE INTEGER,GLUCOSE INTEGER,PREDICTION TEXT)''')
conn.commit()

st.title("HEART  DISEASE  RISK  PREDICTION SYSTEM")
st.image("image.jpg",width=670)
st.subheader('This application predicts your risk of heart disease based on your health information.')
Name = st.text_input('Enter your name')
gender = st.radio('Gender (1 = Male, 0 = Female)',(1,0))
age = st.slider('Age must be 18 or Above',min_value=18,max_value=100,value= 18,step=1)
education = st.slider('Education (1 = No School, 2 = Elementary, 3 = High School, 4 = College+)',
                      min_value=1,max_value=4,value=1)
currentsmoker = st.selectbox('Current Smoker (1 = Yes, 0 = No)',(0,1))
cigperday = st.number_input('Cigarettes Per Day',min_value=0,max_value=40,value=0)
BPMeds = st.selectbox('Blood Pressure Medication (1 = Yes, 0 = No)',(0,1))
preSrk = st.selectbox('Had a Stroke Before? (1 = Yes, 0 = No)',(0,1))
preHyp = st.selectbox('Do You Have High Blood Pressure? (1 = Yes, 0 = No)',(0,1))
diabets = st.selectbox('Do You Have Diabetes? (1 = Yes, 0 = No)',(0,1))
totcol = st.number_input('Total Cholesterol (60–700 mg/dL)',min_value=60,max_value=700,value=60)
sysBP = st.number_input('Systolic Blood Pressure (70–350 mmHg)',min_value=70,max_value=350,value=70)
diaBP = st.number_input('Lower (Diastolic) Blood Pressure (40–180 mmHg)',min_value=40,max_value=180,
                        value=40)
BMI = st.number_input('Body Mass Index (BMI) (18.0–80.0 kg/m²)',min_value=18.0,max_value=80.0,value=18.0)
heartrate = st.number_input('Heart Rate (30–150 BPM)',min_value=30,max_value=150,value=30)
glucose =st.number_input('Blood Glucose Level (40–400 mg/dL)',min_value=40,max_value=400,value=40)
x_value = pd.DataFrame({
    'male':[gender],'age':[age],'education':[education],'currentSmoker':[currentsmoker],
    'cigsPerDay':[cigperday],'BPMeds':[BPMeds],'prevalentHyp':[preHyp],'prevalentStroke':[preSrk],
    'diabetes':[diabets],'totChol':[totcol],'sysBP':[sysBP],'diaBP':[diaBP],'BMI':[BMI],
    'heartRate':[heartrate],'glucose':[glucose]
})


if st.button('Predict'):
    prediction = model.predict(x_value)
    if prediction == 0:
        RESULT = 'NOT DETECTED'
        st.success('🎉 Congratulations! No Evidence of Heart Disease Detected.')
    else:
        RESULT = 'DETECTED'
        st.error('😔 We are sorry. Heart Disease Risk Found.')
    cursor.execute("""INSERT INTO framingham_table(NAME,MALE,AGE,EDUCATION ,CURRENT_SMOKER ,CIGsPERDAYS ,
        BP_MEDICATION,HAD_A_STROKE ,HIGH_BP ,DIABETES ,CHOLESTEROL ,
        SYSTOLIC_BP ,DIASTOLIC_BP ,BMI ,HEART_RATE ,GLUCOSE,PREDICTION) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (Name, gender, age, education, currentsmoker, cigperday, BPMeds, preSrk,
         preHyp,diabets, totcol, sysBP, diaBP, BMI, heartrate, glucose, RESULT))
    conn.commit()
    st.success('Saved Successfully')

if st.checkbox('Prediction History(Only Admin)'):
    password = st.text_input('Enter Password',type='password')
    if password == '1234':
        st.success('Welcome')
        df = pd.read_sql_query('SELECT * FROM framingham_table',conn)
        st.dataframe(df,hide_index=True)
        st.header('Update Record')

        record_id = st.number_input('Record ID',min_value=1)
        column = st.selectbox('Select Column',['NAME','MALE','AGE','EDUCATION' ,'CURRENT_SMOKER',
        'CIGsPERDAYS','BP_MEDICATION','HAD_A_STROKE' ,'HIGH_BP' ,'DIABETES' ,'CHOLESTEROL' ,
        'SYSTOLIC_BP' ,'DIASTOLIC_BP' ,'BMI' ,'HEART_RATE' ,'GLUCOSE','PREDICTION'])
        if column == 'PREDICTION':
            val = st.selectbox('New Value',['Detected','Not Detected'])
        else:
            val = st.text_input('New Value')
        if st.button('Update'):
            cursor.execute(f'UPDATE framingham_table SET {column}= ? WHERE ID = ?',(val,record_id))
            conn.commit()
            st.success('Updated Successfully')
    elif password != "":
        st.error('incorrect password')



def footer():
    st.write("---")
    st.write("Heart Disease Prediction System")
    st.write("Developed by MEHRAN KHAN")
    st.write("© 2026 All Rights Reserved")

st.subheader('Input send to the Pipeline')
st.table(x_value)



footer()

st.sidebar.subheader('REQUIREMENTS')
st.sidebar.markdown("""
- Name
- Male
- Age
- Education
- Current Smoker
- Cigarettes Per Day
- Blood Pressure Medication
- Previous Stroke
- Hypertension
- Diabetes
- Total Cholesterol
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Body Mass Index (BMI)
- Heart Rate
- Glucose
""")




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
        linear-gradient(rgba(0,0,0,0.70), rgba(0,0,0,0.70)),
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
    background-color: #374151;
    color: white !important;
}

.stButton > button p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* ===========================
   Sidebar Background
=========================== */
section[data-testid="stSidebar"]{
    background-color: white !important;
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color: black !important;
}

/* Sidebar Lists */
section[data-testid="stSidebar"] ul,
section[data-testid="stSidebar"] li{
    color: black !important;
}

/* Sidebar Headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] h5,
section[data-testid="stSidebar"] h6{
    color: black !important;
}

/* ===========================
   Sidebar Collapse Arrow
=========================== */
button[kind="header"] svg{
    fill: black !important;
    color: black !important;
}

/* ===========================
   Top Header Buttons
   (Deploy, Menu, etc.)
=========================== */
header[data-testid="stHeader"]{
    background: transparent !important;
}

header[data-testid="stHeader"] button{
    color: black !important;
}

header[data-testid="stHeader"] svg{
    fill: black !important;
    color: black !important;
}

/* Deploy Button */
header[data-testid="stHeader"] .stButton button{
    color: black !important;
    border-color: black !important;
}
/* ===========================
   Three Dots Menu
=========================== */

/* Three-dot icon */
button[aria-label="Main menu"] svg,
button[data-testid="stMainMenuButton"] svg{
    fill: black !important;
    color: black !important;
}

/* Fallback for any header SVG icons */
header[data-testid="stHeader"] button svg{
    fill: white !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Move page content upward */
.block-container{
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)


