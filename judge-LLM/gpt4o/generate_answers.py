from openai import OpenAI
import os
import json
import time
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt4o_answer(prompt, model="gpt-4o-mini", max_tokens=256):
    for _ in range(3):
        try:
            response = client.chat.completions.create(model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=max_tokens)
            return response.choices[0].message.content
        except Exception as e:
            print(f"Retrying due to error: {e}")
            time.sleep(2)
    return "[ERROR]"

def generate_answers(samples, output_path):
    with open(output_path, "w") as out:
        for sample in tqdm(samples, desc="Generating GPT-4o Mini Answers"):
            if not all(key in sample for key in ["id", "topic", "question", "solution"]):
                print(f"Skipping invalid sample: {sample}")
                continue

            answer = get_gpt4o_answer(
                sample["question"] + " Give only the final answer. Do not explain your reasoning."
            )
            if answer == "[ERROR]":
                print(f"Failed to generate answer for question: {sample['question']}")
                continue

            out.write(json.dumps({
                "id": sample["id"],
                "topic": sample["topic"],
                "difficulty": sample.get("difficulty", ""),
                "question": sample["question"],
                "gpt4o_answer": answer,
                "solution": sample["solution"]
            }) + "\n")
    print(f"Answers written to {output_path}")