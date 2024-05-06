import streamlit as st

# Title for the app
st.title('Streamlit Text Input and Display')

# Initialize or retrieve the session state for storing texts
if 'texts' not in st.session_state:
    st.session_state.texts = []

# Display all previous texts above the text area
st.write("Previous entries:")
for text in st.session_state.texts:  # Display from oldest to newest
    st.write(text)

# Text area for input
user_input = st.text_area("Enter your text here:")

# Button to submit the text
if st.button("Submit"):
    if user_input:  # Check if there is something to add
        st.session_state.texts.append(user_input)  # Append the input to the list
