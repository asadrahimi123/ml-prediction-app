# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:50:30 2024

@author: DELL
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the saved models

diabetes_model = pickle.load(open('trained_model.sav', 'rb'))

heart_model = pickle.load(open('trained_model_heart.sav', 'rb'))

# Sidebar for navigate

with st.sidebar:
    selected = option_menu(
            'Multiplt Disease Prediction System',
            ['Diabetes Predection',
             'Heart Disease Prediction'
                ],
            
            icons = ['activity','heart'],
            
            default_index = 0
        )
    
# Diabetes Prediction Page
if (selected == 'Diabetes Predection'):
    st.title('Diabetes Predection using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')    
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin value')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    diab_dignosis = ''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0] == 1):
            diab_dignosis = 'The person is Diabetic'
        else:
            diab_dignosis = 'The person is not Diabetic'
            
    st.success(diab_dignosis)
    
    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Enter the Age of Person')
    
    with col2:
        sex = st.text_input('Sex of Person')
    
    with col3:
        cp = st.text_input('Chest Pain types')    
    
    with col1:
        trestbps = st.text_input('Restin Boold Pressure')
    
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    
    with col3:
        fbs = st.text_input('Fasting Boold Suger > 120 mg/dl')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic result')
    
    with col2:
        thalach = st.text_input('Maximum Heart Reate Achived')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST Depression Induced by exercise')
        
    with col2:
        slope = st.text_input('Slop of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal:0 = normal; 1=fixed defect; 2=reversable defect')
        
        
    heart_dignosis = ''
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_prediction[0] == 1):
            heart_dignosis = 'The person is Diabetic'
        else:
            heart_dignosis = 'The person is not Diabetic'
            
    st.success(heart_dignosis)


    
    
    
    
    
    
    
    
    
    
    
    
