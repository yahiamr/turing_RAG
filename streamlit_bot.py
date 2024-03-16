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
    
    
    if prompt:
        # Encode and generate response
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    
        # Decode and display the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.text_area("Response:", value=response, height=200, max_chars=None, key=None)