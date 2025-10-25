import streamlit as st
from PIL import Image
import torch
from ultralytics import YOLO
import time
from style import load_style

st.set_page_config(
    page_title="Dataset",
    page_icon="🧫",
    layout="centered"
)

load_style() # to call the style.py


# DATASET PAGE ============================================================================================#

st.title("The Dataset")


st.write("""
Using the dataset provided by the authors (see link below), we trained our model based on images collected and prepared in the bone marrow laboratory of Taleqani Hospital, Tehran, Iran. 
This dataset includes 3,256 peripheral blood smear (PBS) images obtained from 89 patients suspected of having Acute Lymphoblastic Leukemia (ALL). 
All samples were prepared and stained by experienced laboratory technicians. The dataset is categorized into two main classes: **benign** and **malignant**. 
The benign class consists of hematogones, while the malignant class represents the ALL group, which is further divided into three subtypes: **Early Pre-B**, **Pre-B**, and **Pro-B ALL**.
""")

st.markdown("[Click here to view the Kaggle Dataset](https://www.kaggle.com/datasets/mehradaria/leukemia)")
st.write("")
st.write("")
st.image("images/Screenshot 2025-10-25 220224.png", caption="snippet")
st.write("")
st.write("""
The dataset creators also published their own research paper and trained their own model, which can be accessed through the link below if you want to check that out.
""")

st.markdown("[A fast and efficient CNN model for B-ALL diagnosis and its subtypes classification using peripheral blood smear images](https://onlinelibrary.wiley.com/doi/10.1002/int.22753)")

st.divider()

st.subheader("References")
st.write("""
Mehrad Aria, Mustafa Ghaderzadeh, Davood Bashash, Hassan Abolghasemi, Farkhondeh Asadi, and Azamossadat Hosseini. 
"Acute Lymphoblastic Leukemia (ALL) image dataset." *Kaggle*, (2021). DOI: 10.34740/KAGGLE/DSV/2175623.
""")

st.write("""
Ghaderzadeh, M., Aria, M., Hosseini, A., Asadi, F., Bashash, D., & Abolghasemi, H. 
"A fast and efficient CNN model for B-ALL diagnosis and its subtypes classification using peripheral blood smear images." 
*International Journal of Intelligent Systems*, 2022; 37: 5113–5133. DOI: 10.1002/int.22753.
""")
