import streamlit as st
import tempfile
import os
import sys
from PIL import Image
import numpy as np
# sys.path.insert(0, 'yolov5')
import inference 
from utils.datasets import LoadStreams, LoadImages
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def run():

    st.title("Road Damage Monitoring POC")
    st.sidebar.title('Configuration')
    detection_method = "YOLO"

    if detection_method == 'YOLO':
        IOU_slider = st.sidebar.slider("IOU Threshold", 0.0, 1.0, 0.99, 0.05)
    else:
        pass

    confidence_slider = st.sidebar.slider("Confidence threshold for detection", 0.0, 1.0, 0.2, 0.05)
    file_uploaded = st.file_uploader("Upload an image", type = ['png', 'jpg','jpeg'])
    # create temp dir for storing video and outputs
    temp_dir = tempfile.TemporaryDirectory()
    temp_path = temp_dir.name
    if file_uploaded is not None:
        show_image = Image.open(file_uploaded)
        image = np.array(show_image)
        inference.save_uploaded_file(file_uploaded, temp_path)
    else:
        st.write('** Please upload an image **')

    if st.button('Detect Objects'):

        inference.steamlit_detect(image, temp_path, confidence_slider, IOU_slider, '../results/best.pt')
        # st.image(image, caption = 'Processed Image', use_column_width = True)
        # st.write(labels)



if __name__ == '__main__':

    run()


