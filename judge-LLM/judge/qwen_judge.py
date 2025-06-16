from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteriaList, StoppingCriteria
import torch

class StopOnToken(StoppingCriteria):
    def __init__(self, stop_token_id):
        self.stop_token_id = stop_token_id
    def __call__(self, input_ids, scores, **kwargs):
        return input_ids[0][-1] == self.stop_token_id

model_name = "Qwen/Qwen3-1.7B"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
model.eval()

# Get the token ID for the stop character "}"
stop_token_id = tokenizer("}", add_special_tokens=False)["input_ids"][-1]
stopping_criteria = StoppingCriteriaList([StopOnToken(stop_token_id)])

def judge_with_qwen(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=256,
            stopping_criteria=stopping_criteria,
            do_sample=False
        )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    # Slice to just the JSON if needed
    start_idx = decoded.find("{")
    return decoded[start_idx:].strip()
