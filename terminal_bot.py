import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
    model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")

    # Get user input
    prompt = input("Enter your prompt: ")

    # Encode and generate response
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)

    # Decode and display the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(response)

if __name__ == "__main__":
    main()