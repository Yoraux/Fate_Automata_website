import streamlit as st
from PIL import Image
import torch
from ultralytics import YOLO
import time
from style import load_style

st.set_page_config(
    page_title="Documentation",
    page_icon="🧫",
    layout="centered"
)

load_style() # to call the style.py











# DOCUMENTATION PAGE ============================================================================================#

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

st.title("Documentation")
st.write("""


### Model Details
- add some stuff

         

### How It Works
- add some stuff

         
### Notes
- The model was trained using unseen data for evaluation.
""")