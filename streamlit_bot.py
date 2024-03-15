import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load tokenizer and model only once, using caching
@st.cache(allow_output_mutation=True)
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    return tokenizer, model
    
    tokenizer, model = load_model()
    
    # Streamlit app
    st.title("GPT-2 Interactive Chat")
    
    # Text input for user prompt
    prompt = st.text_input("Enter your prompt:")