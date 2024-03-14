import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load tokenizer and model only once, using caching
@st.cache(allow_output_mutation=True)
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    return tokenizer, model