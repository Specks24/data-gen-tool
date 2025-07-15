import streamlit as st

def ddl_input_component():
    ddl = st.text_area("Paste DDL")
    if ddl:
        # TODO: Parse DDL
        st.write('DDL received')