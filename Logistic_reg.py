import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
import pickle as pkl

df = pd.read_csv('framingham.csv')
#print(df)
print('Shape :',df.shape)
# Data Pre-processing
df['education'] = df['education'].fillna(df['education'].median())
df['cigsPerDay'] = df['cigsPerDay'].fillna(df['cigsPerDay'].mean())
df['BPMeds'] =df['BPMeds'].fillna(0)
df['totChol'] = df['totChol'].fillna(df['totChol'].median())
df['BMI'] = df['BMI'].fillna(df['BMI'].mean())
df['glucose'] = df['glucose'].fillna(df['glucose'].median())
df['heartRate'] = df['heartRate'].fillna(df['heartRate'].median())
# After fill missing values
print(df.isnull().sum())

# Model training
print('-----Model Training-----')
logReg = LogisticRegression(solver='liblinear',max_iter=50)
logReg.fit(df[['male','age','education','currentSmoker','cigsPerDay','BPMeds',
               'prevalentHyp','prevalentStroke','diabetes','totChol','sysBP',
               'diaBP','BMI','heartRate','glucose']],df.TenYearCHD)
print('Score :',logReg.score(df[['male','age','education','currentSmoker',
                'cigsPerDay','BPMeds','prevalentHyp','prevalentStroke',
                'diabetes','totChol','sysBP','diaBP','BMI','heartRate',
                'glucose']],df.TenYearCHD))
print('Prediction :',logReg.predict([[1,70,4,1,30,1,1,1,1,245,160,60,29.1,95,88]]))
print('Coefficients :',logReg.coef_)
print('Intercept :',logReg.intercept_)
check_pred =  (0.45520684*1 + 0.0509825*70 + -0.05853552*4 + -0.06972079*1+
               0.02149773*30 + 0.28703992*1 + 0.44065134*1 + 0.77724509*1+
               0.33938429*1 + 0.00078324*245 + 0.01323525*160 -0.00944519*60
               -0.01254296*29.1 -0.00700632*95 + 0.0052233*88 -5.56606581)
# print('Check Prediction :',check_pred)
#
# with open('logReg.pkl', 'wb') as f:
#     pkl.dump(logReg, f)

#print(df['education'].unique())
# print(df['totChol'].max())
# print(df['totChol'].min())
print(df['heartRate'].max())
print(df['heartRate'].min())