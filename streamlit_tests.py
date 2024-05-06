import streamlit as st

question = st.text_area("Please type your question here")

placeholder=st.empty()

placeholder.text(question)
