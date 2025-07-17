# app.py (web/): Streamlit web application for user-facing UI.
# Provides a simple interface for schema inference, generation, and download.
# This is a stub; expand with more UI elements (e.g., heuristics inputs).

import streamlit as st
import pandas as pd
from data_gen.parsers import infer_from_sample, infer_from_ddl
from data_gen.generators import generate_rows
from data_gen.writers import get_writer
import io

st.title("Data Generation Tool")  # Set page title.

option = st.selectbox("Infer schema from:", ["DDL", "Sample File"])  # Dropdown for inference method.

if option == "DDL":
    ddl = st.text_area("Enter SQL DDL:")  # Text area for DDL input.
    schema = infer_from_ddl(ddl) if ddl else None  # Infer if DDL provided.
else:
    uploaded_file = st.file_uploader("Upload sample file (CSV):")  # File uploader.
    if uploaded_file:
        # Note: Streamlit uploader provides file-like object; may need temp handling for non-CSV.
        schema = infer_from_sample(uploaded_file.name)  # Infer schema.
    else:
        schema = None

if schema:  # Display schema if inferred.
    st.write("Inferred Schema:", schema)

    num_rows = st.number_input("Number of rows:", min_value=1, value=100)  # Input for row count.
    format = st.selectbox("Output Format:", ["csv", "txt", "parquet", "delta"])  # Format selection.
    heuristics = {}  # Placeholder; add UI widgets for heuristics in future.

    if st.button("Generate"):  # Button to trigger generation.
        data_gen = generate_rows(num_rows, schema, heuristics)  # Generate rows.
        data = list(data_gen)  # Materialize.
        writer = get_writer(format)  # Get writer.

        buffer = io.BytesIO()  # In-memory buffer for download.
        # Handle CSV/TXT with Pandas for easy download.
        if format in ["csv", "txt"]:
            sep = ',' if format == 'csv' else '\t'  # Set separator.
            pd.DataFrame(data).to_csv(buffer, sep=sep, index=False)  # Write to buffer.
            st.download_button("Download", buffer, f"data.{format}")  # Provide download button.
        else:
            st.write("Generation complete; download support for this format coming soon.")  # Placeholder for other formats.