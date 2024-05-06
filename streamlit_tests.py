import streamlit as st

#Title for this test app
st.title("Streamlit Text Input and Display")

#Initialize the variable for text input
question = st.text_area("Please type your question here")

if question:
  st.write("user:")
  st.write(question)
