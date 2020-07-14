# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:33:17 2020

@author: parth
"""


from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

st.header("""
Simple Iris Flower Prediction App

This app predicts the **Iris flower** type!
""") 
dataset=load_iris()
print(dataset.data)
st.sidebar.header('User Input Parameters')


def user_input_parameter():
    sepal_length=st.sidebar.slider('Sepal Length', 4.3,7.9,5.4)
    sepal_width=st.sidebar.slider('Sepal Width', 2.0,4.4,3.4)
    petal_length=st.sidebar.slider('Petal Length', 1.0,6.9,1.3)
    petal_width=st.sidebar.slider('Petal Width', 0.1,2.5,0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    feature=pd.DataFrame(data,index=[0])
    return feature


df = user_input_parameter()
st.subheader('User Input parameters')
st.write(df)
X=dataset.data
y=dataset.target 
clf=RandomForestClassifier()
clf.fit(X,y) 


prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(dataset.target_names)

st.subheader('Prediction')
st.write(dataset.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
