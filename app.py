import streamlit as st
from src.mapping import mock_map_clinical_term

st.title("OMOP Mapper Demo")
term = st.text_input("Enter a clinical term:")
if st.button("Map"):
    result = mock_map_clinical_term(term)
    st.json(result)