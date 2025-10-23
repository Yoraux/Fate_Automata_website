import streamlit as st
from PIL import Image
import torch
from ultralytics import YOLO
import time
from style import load_style


st.set_page_config(page_title="Home", page_icon="🧫", layout="centered")

load_style() # to call the style.py



 # HOME PAGE ============================================================================================#
st.markdown(
        """
        <h1 style='text-align: center;'>Acute Lymphoblastic Leukemia Detection using YOLOv12</h1>
        <h3>  <h3>
        <hr style='margin-top: -10px; margin-bottom: 20px;'>
        <h3 style='text-align: center;'>By Group Fate/Automata of CSS181-2 AM2</h3>
        <div style='text-align: center; font-size: 18px; line-height: 1.8;'>
            Chang, Dash Michael<br>
            Cortes, Juan Diego<br>
            Herrera, Kael Lorenzo<br>
            San Miguel, Ian Rafael
        </div>
        """,
        unsafe_allow_html=True
    )
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.info("Use the sidebar on the left to navigate between pages (Model Prediction, Documentation, About, etc.)")




# NOTES:
# To make a new page just make a new .py file and make sure to put it in the "pages" folder, and also make sure to number it correctly 
# for example:
# 3_About us



# References:
# https://www.geeksforgeeks.org/python/a-beginners-guide-to-streamlit/
# https://docs.streamlit.io/develop
# https://docs.streamlit.io/develop/api-reference
