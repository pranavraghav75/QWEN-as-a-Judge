from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from prompts.templates import judge_prompt

model_name = "Qwen/Qwen3-4B"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
model.eval()

def judge_with_qwen(question, gpt_answer):
    prompt = judge_prompt(question, gpt_answer)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=256)
    return tokenizer.decode(output[0], skip_special_tokens=True)