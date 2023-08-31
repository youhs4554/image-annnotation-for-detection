import streamlit as st
from glob import glob
from streamlit_image_annotation import detection

import streamlit as st
from PIL import Image

img_file_buffer = st.camera_input("Take a picture")
image_path = 'input.png'

if img_file_buffer:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)
    img.save(image_path)

    label_list = ['class1', 'class2', 'class3']
    if 'result_dict' not in st.session_state:
        result_dict = {}
        result_dict[image_path] = {'bboxes': [[]],'labels':[]}
        st.session_state['result_dict'] = result_dict.copy()

    new_labels = detection(image_path=image_path, 
                        bboxes=st.session_state['result_dict'][image_path]['bboxes'], 
                        labels=st.session_state['result_dict'][image_path]['labels'], 
                        label_list=label_list, key=image_path)
    if new_labels is not None:
        st.session_state['result_dict'][image_path]['bboxes'] = [v['bbox'] for v in new_labels]
        st.session_state['result_dict'][image_path]['labels'] = [v['label_id'] for v in new_labels]
        
    st.json(st.session_state['result_dict'])