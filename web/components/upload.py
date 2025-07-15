import streamlit as st

def upload_component():
    uploaded_file = st.file_uploader("Upload sample dataset")
    if uploaded_file:
        # TODO: Infer schema
        st.write('File uploaded')