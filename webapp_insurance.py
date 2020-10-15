# -*- coding: utf-8 -*-
"""webapp_insurance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VNOS-jzKXnIFScBB0tQtUWGheGyqKyG6
"""

# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
import pandas as pd
import numpy as np

df = pd.read_csv("insurance.csv")


import pickle
import streamlit as st

st.subheader("Get an estimate of your medical insurance charges!")

st.sidebar.header("User Input Features")

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        age = st.sidebar.slider("age",18,64,50)
        sex = st.sidebar.selectbox("sex",("male","female"))
        bmi = st.sidebar.slider("bmi",15.96,53.13,30.00)
        children = st.sidebar.slider("children",0,5,2)
        smoker = st.sidebar.selectbox("smoker",("yes","no"))
        region = st.sidebar.selectbox("region",('southwest', 'southeast', 'northwest', 'northeast'))
        data = {'age': age,
                'sex': sex,
                'bmi': bmi,
                'children': children,
                'smoker': smoker,
                'region': region}
        df2 = pd.DataFrame(data,index=[0])
        return df2
    input_df = user_input_features()
st.write("Built by : Riya Jain")
X = df.drop(columns=['charges'])

y = df['charges']

X1 = pd.concat([input_df,X],axis = 0)
X1 = pd.get_dummies(X1)

X =pd.get_dummies(X)

# from xgboost import XGBRegressor
# xgb1 = XGBRegressor(booster = "gbtree",tree_method="hist",learning_rate= 0.2,
#  max_depth= 3,
#  min_child_weight= 4,
#  n_estimators= 100)
# xgb1.fit(X,y)
from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor(n_estimators=150,criterion="mse",max_depth = None,
                               max_features='log2',min_samples_split = 20, bootstrap=True)
clf.fit(X,y)

# Apply model to make predictions
prediction = clf.predict(X1[:1])
st.write(prediction)

