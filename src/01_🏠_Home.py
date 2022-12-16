import streamlit as st

with open("README.md", "r") as f:
    st.markdown(f.read())

st.markdown("Pages on the panel to the left!")
