from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "Qwen/Qwen3-1.7B"
small_model_name = "Qwen/Qwen3-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
small_tokenizer = AutoTokenizer.from_pretrained(small_model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
small_model = AutoModelForCausalLM.from_pretrained(small_model_name, device_map="auto", trust_remote_code=True)
model.eval()
small_model.eval()

def judge_with_qwen(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=1024
        )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded.strip()

def judge_with_nonthinking_qwen(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=64,
        )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded.strip()

def small_judge_with_qwen(prompt):
    inputs = small_tokenizer(prompt, return_tensors="pt").to(small_model.device)
    with torch.no_grad():
        output = small_model.generate(
            **inputs,
            max_new_tokens=1024
        )
    decoded = small_tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded.strip()

def small_judge_with_nonthinking_qwen(prompt):
    inputs = small_tokenizer(prompt, return_tensors="pt").to(small_model.device)
    with torch.no_grad():
        output = small_model.generate(
            **inputs,
            max_new_tokens=64,
        )
    decoded = small_tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded.strip()