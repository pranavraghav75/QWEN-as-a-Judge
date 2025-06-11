import openai
import os
import json
import time
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt4o_answer(prompt, model="gpt-4o", max_tokens=512):
    for _ in range(3):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=max_tokens
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Retrying due to error: {e}")
            time.sleep(2)
    return "[ERROR]"

def generate_answers(samples, output_path):
    with open(output_path, "w") as out:
        for sample in tqdm(samples, desc="Generating GPT-4o Answers"):
            answer = get_gpt4o_answer(sample["question"])
            out.write(json.dumps({
                "id": sample["id"],
                "topic": sample["topic"],
                "question": sample["question"],
                "gpt4o_answer": answer,
                "solution": sample["solution"]
            }) + "\n")