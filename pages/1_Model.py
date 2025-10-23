import streamlit as st
from PIL import Image
import torch
from ultralytics import YOLO
import time
from style import load_style

st.set_page_config(
    page_title="Model",
    page_icon="🧫",
    layout="centered"
)

load_style() # to call the style.py








# MODEL PAGE ============================================================================================#
########################## UPLOAD FILE ##########################
@st.cache_resource
def load_model():
    return YOLO("yolov12/best.pt") #this is the model itself. In our case Train3 or version 3's best.pt was picked since it scored 93% 
model = load_model()


st.title("The model")
st.header("Using Yolov12 provided by our professor, we trained the model to help detect the cells in a leukemia blood smear")
test_image = st.file_uploader("", type=["jpg", "jpeg", "png",]) #this is to upload a image file
st.write("Please make sure that the image is at least 768 x 768 and above")
st.write("The image you uploaded will appear below\n")


########################### DETECT AND OUTPUT ##########################
if test_image is not None:
    image = Image.open(test_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    progress_text = "Running detection, please wait..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
            time.sleep(0.03)  # this is where to change how long the progress bar loads. 0.01 = 1 second
            my_bar.progress(percent_complete + 1, text=progress_text) 
        #This is a simple progress bar from: https://docs.streamlit.io/develop/api-reference/status/st.progress
        #It's just here to add some flair or "life" to the website
        #Right now It is actually not tied to how long the model predicts. There is a set timer for how long the progress bar loads, which is 3 seconds.


        #!!!DISCLAIMER!!!
        #for this part AI (Chatgpt) was used to help with the code with the prompt "How do I load my model into streamlit?
    results = model.predict(image, imgsz=768, conf=0.5) # prediction starts
    my_bar.empty() # Removes the progress bar when done

    res_plotted = results[0].plot() # Display results
    st.image(res_plotted, caption="Detection Result", use_container_width=True)

    st.subheader("Detected Classes:")
    names = results[0].boxes.cls.tolist()
    unique_labels = [model.names[int(i)] for i in set(names)]
    st.write(unique_labels)

