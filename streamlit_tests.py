import streamlit as st

question = st.text_area("Please type your question here")

placeholder=st.empty()
placeholder.text(question)
st.text()

def add_text_block():
  if question:
    st.text("test")
