import streamlit as st
from PIL import Image
import torch
from ultralytics import YOLO
import time
from style import load_style

st.set_page_config(
    page_title="About",
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

st.title("About")
st.write("""
### Model Details

- The **YOLOv12** model was trained a total of **six times**. The dataset was annotated using **Roboflow** and went through **four versions** during development.

- **First Training (v1):**  
  The first version of the dataset (**v1**) contained **4,458 images**, split into **72% training**, **14% validation**, and **14% testing**.  
  Preprocessing included **auto-orientation** and **resizing to 640×640**, with augmentation of **blur up to 2 px**.  
  This initial training achieved an mAP@50 score of **70%**.

- **Second Training (v2):**  
  The **v2** dataset consisted of **3,390 images**, split into **82% training**, **9% validation**, and **9% testing**.  
  Preprocessing again included **auto-orientation**, but the images were **resized to 768×768**.  
  Augmentations applied were **rotation between -10° and +10°**, **brightness adjustment between -10% and +10%**, and **blur up to 0.5 px**.  
  This version yielded an **mAP@50 of 0.90636 at epoch 47**, showing a significant improvement over v1.

- **Third Training (v3):**  
  The **v3** dataset contained **3,766 images**, split into **75% training**, **12% validation**, and **13% testing**.  
  The same preprocessing was used, with additional augmentations including:  
  **Horizontal and vertical flips**, **shear of ±5°**, **hue adjustment between -5° and +5°**, **saturation adjustment between -21% and +21%**,  
  and **noise applied to up to 0.01% of pixels**.  
  This version achieved an **mAP@50 of 0.93326 at epoch 1**, marking another improvement.

- **Fourth Training (v4):**  
  Aiming for at least **95% accuracy**, a new version (**v4**) was created with **5,181 images**, split into **82% training**, **9% validation**, and **9% testing**.  
  The same preprocessing steps were applied, with an added **crop augmentation** (minimum zoom: 5%, maximum zoom: 22%).  
         
  Despite three more separate training attempts after v4, the best result was achieved during **training #6**, which reached an **mAP@50 of 0.92632 at epoch 15**.  
  While not the highest value compared to v3, this model was the most consistent, maintaining **above 90% performance across all epochs**.


---

### Notes
- The model was evaluated using **unseen data** to ensure fair performance assessment.
""")

st.divider()
st.write("""
### Model Limitations
- The main limitation of the model is that it struggles to generalize to microscopic images with styles different from those in the training dataset.
- It also has difficulty distinguishing between the **Early** and **Pre** subtypes, as both exhibit similar cell coloration based on the dataset.
- The primary difference between these two classes lies in the **number of such cells present** in each image.
""")