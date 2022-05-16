# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:43:23 2022

@author: migue
"""
import streamlit as st
import pandas as pd



with st.container():
    st.subheader("Deploying my first app")
    st.title("Forecast prediction")
    st.write("""Hello Motherfuckets""")
    
    title = st.text_input('Write your name', 'Life of Brian')
    MinTemp = st.text_input("MinTemp","")
    MaxTemp = st.text_input("MaxTemp","")
    Rainfall = st.text_input("Rainfall","")
    Evaporation = st.text_input("Evaporation","")
    Sunshine = st.text_input("Sunshine","")
    WindGustSpeed = st.text_input("WindGustSpeed","")
    Humidity9am = st.text_input("Humidity9am","")
    Humidity3pm = st.text_input("Humidity3pm","")
    Pressure9am = st.text_input("Pressure9am","")
    Pressure3pm = st.text_input("Pressure3pm","")
    Cloud3pm = st.text_input("Cloud3pm","")
    Temp3pm = st.text_input("Temp3pm","")