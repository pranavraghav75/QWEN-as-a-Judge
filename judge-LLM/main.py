import os
import json
import random
from gpt4o.generate_answers import generate_answers
from judge.qwen_judge import judge_with_qwen

DATA_DIR = "data/MATH/train"
GPT_OUTPUT = "results/gpt4o_answers.jsonl"
JUDGMENT_OUTPUT = "results/judgments.jsonl"

def load_questions(data_dir):
    topics = ["algebra", "number_theory", "counting_and_probability"]
    samples = []

    for topic in topics:
        topic_dir = os.path.join(data_dir, topic)
        if not os.path.exists(topic_dir):
            continue
        topic_samples = []
        for fname in os.listdir(topic_dir):
            if fname.endswith(".json"):
                with open(os.path.join(topic_dir, fname)) as f:
                    try:
                        data = json.load(f)
                        topic_samples.append(data)
                    except json.JSONDecodeError:
                        print(f"Skipping invalid JSON file: {fname}")
                        continue
        # Flatten the list and randomly select 25-50 questions
        topic_samples = [item for sublist in topic_samples for item in sublist]
        samples.extend(random.sample(topic_samples, min(len(topic_samples), random.randint(25, 50))))

    return samples

def main():
    questions = load_questions(DATA_DIR)
    generate_answers(questions, GPT_OUTPUT)
    with open(GPT_OUTPUT, "r") as f, open(JUDGMENT_OUTPUT, "w") as out:
        for line in f:
            sample = json.loads(line)
            judgment = judge_with_qwen(sample["question"], sample["gpt4o_answer"])
            out.write(json.dumps({
                "id": sample["id"],
                "topic": sample["topic"],
                "question": sample["question"],
                "gpt4o_answer": sample["gpt4o_answer"],
                "judgment": judgment
            }) + "\n")

if __name__ == "__main__":
    main()