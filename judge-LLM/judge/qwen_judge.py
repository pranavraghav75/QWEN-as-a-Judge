from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteriaList, StoppingCriteria
import torch

model_name = "Qwen/Qwen3-1.7B"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
model.eval()

def judge_with_qwen(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.3,
            top_p=0.9,
            top_k=50
        )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded.strip()
