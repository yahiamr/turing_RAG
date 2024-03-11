import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
