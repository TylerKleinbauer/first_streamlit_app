import streamlit as st

question = st.text_area("Please type your question here")

placeholder=st.empty()

placeholder.text(question)

def add_placeholder(question):
  if question:
    st.text(question)
