import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
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
# # After fill missing values
#print(df.isnull().sum())

# Model training
print('-----Model Training-----')
X = df[['male','age','education','currentSmoker','cigsPerDay','BPMeds',
              'prevalentHyp','prevalentStroke','diabetes','totChol','sysBP',
              'diaBP','BMI','heartRate','glucose']]
y = df['TenYearCHD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

logReg = LogisticRegression(C = 100,solver='liblinear',max_iter=100)
logReg.fit(X_train,y_train)
print('Score :',logReg.score(X_test,y_test))

#print('Coefficients :',logReg.coef_)
#print('Intercept :',logReg.intercept_)

# print('Check Prediction :',check_pred)
#
# with open('logReg.pkl', 'wb') as f:
#     pkl.dump(logReg, f)

