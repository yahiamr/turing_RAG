# Import necessary libraries: Streamlit for the web app, and OpenAI's library for interacting with the API.
import streamlit as st
from langchain.llms import OpenAI

# Set the title of the web app, which appears at the top of the page.
st.title('🦜🔗 Quickstart langchain App')

# Create a sidebar input for the OpenAI API key, masking the input for privacy.
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Define a function to generate responses using OpenAI's language models.
def generate_response(input_text):
    # Initialize the OpenAI model with a specific temperature and the provided API key.
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Generate a response for the input text and display it using Streamlit's info widget.
    st.info(llm(input_text))

# Create a form for user input. This groups elements together visually and functionally.
with st.form('my_form'):
    # Create a text area for user input, with a default value.
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    # Create a submit button for the form.
    submitted = st.form_submit_button('Submit')
    # Check if the provided API key doesn't start with 'sk-', which is a basic validation for OpenAI API keys.
    if not openai_api_key.startswith('sk-'):
        # Display a warning if the API key is invalid, prompting the user to enter a correct one.
        st.warning('Please enter your OpenAI API key!', icon='⚠️')
    # If the form is submitted and the API key is valid, call the function to generate and display the response.
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)