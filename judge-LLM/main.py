import os
import json
import random
from gpt4o.generate_answers import generate_answers
from judge.qwen_judge import judge_with_qwen
from prompts.templates import judge_prompt
from tqdm import tqdm
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# TRAIN_DIR = "data/MATH/train"
TEST_DIR = "data/MATH/test"
GPT_OUTPUT = "results/gpt4o_answers.jsonl"
JUDGMENT_OUTPUT = "results/judgments.jsonl"

def load_questions(data_dir, num_questions):
    topics = ["algebra", "number_theory", "counting_and_probability"]
    samples = []

    for topic in topics:
        topic_dir = os.path.join(data_dir, topic)
        if not os.path.exists(topic_dir):
            print(f"Topic directory does not exist: {topic_dir}")
            continue
        topic_samples = []
        for fname in os.listdir(topic_dir):
            if fname.endswith(".json"):
                with open(os.path.join(topic_dir, fname)) as f:
                    try:
                        data = json.load(f)
                        topic_samples.append({
                            "id": fname.split(".")[0],
                            "topic": topic,
                            "question": data.get("problem", ""),
                            "solution": data.get("solution", "")
                        })
                    except json.JSONDecodeError:
                        print(f"Skipping invalid JSON file: {fname}")
                        continue

        if num_questions:
            samples.extend(random.sample(topic_samples, min(len(topic_samples), num_questions)))

    print(f"Total questions loaded: {len(samples)}")
    return samples

def run_experiment(test_questions, mode):
    results = []
    print(f"Running experiment in mode: {mode}")
    for sample in tqdm(test_questions, desc=f"Judging ({mode})"):
        try:
            if mode == "Baseline":
                prompt = judge_prompt(sample["question"], solution=sample["solution"], mode=mode)
                judgment = judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "question": sample["question"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": mode
                })
            elif mode == "B":
                prompt = judge_prompt(sample["question"], gpt_answer=sample["gpt4o_answer"], solution=sample["solution"], mode=mode)
                judgment = judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": mode
                })
            else:
                prompt = judge_prompt(sample["question"], gpt_answer=sample["gpt4o_answer"], mode=mode)
                judgment = judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "judgment": judgment,
                    "mode": mode
                })

        except Exception as e:
            print(f"Error during experiment in mode {mode}: {e}")
    print(f"Experiment completed for mode: {mode}, results count: {len(results)}")
    return results

def main():
    # test_questions = load_questions(TEST_DIR, num_questions=25)

    # generate_answers(test_questions, GPT_OUTPUT)

    with open(GPT_OUTPUT, "r") as f:
        test_questions_with_answers = [json.loads(line) for line in f]

    # Main Evaluation
    print("##### Running Setup A #####")
    setup_a_results = run_experiment(test_questions_with_answers, mode="A")
    print(f"Setup A results count: {len(setup_a_results)}")
    with open("results/setup_a.jsonl", "w") as f:
        for result in setup_a_results:
            f.write(json.dumps(result) + "\n")
    print("Setup A file written.")

    # Control
    print("##### Running Setup B #####")
    setup_b_results = run_experiment(test_questions_with_answers, mode="B")
    print(f"Setup B results count: {len(setup_b_results)}")
    with open("results/setup_b.jsonl", "w") as f:
        for result in setup_b_results:
            f.write(json.dumps(result) + "\n")
    print("Setup B file written.")

    # Baseline
    # print("##### Running Baseline #####")
    # baseline_results = run_experiment(test_questions_with_answers, mode="Baseline")
    # print(f"Baseline results count: {len(baseline_results)}")
    # with open("results/baseline.jsonl", "w") as f:
    #     for result in baseline_results:
    #         f.write(json.dumps(result) + "\n")
    # print("Baseline file written.")

if __name__ == "__main__":
    main()