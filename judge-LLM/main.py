import os
import json
import random
from gpt4o.generate_answers import generate_answers
from judge.qwen_judge import judge_with_qwen, judge_with_nonthinking_qwen, small_judge_with_qwen, small_judge_with_nonthinking_qwen
from prompts.templates import judge_prompt, judge_prompt_nonthinking
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
                            "difficulty": data.get("level", ""),
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

def run_experiment(test_questions):
    results = []
    for sample in tqdm(test_questions, desc=f"Judging Questions)"):
        try:
            if sample["topic"] == "algebra":
                prompt = judge_prompt(sample["question"], mode="algebra", gpt_answer=sample["gpt4o_answer"])
                judgment = judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "algebra"
                })
            elif sample["topic"] == "number_theory":
                prompt = judge_prompt(sample["question"], mode="number_theory", gpt_answer=sample["gpt4o_answer"])
                judgment = judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "number_theory"
                })
            else:
                prompt = judge_prompt(sample["question"], mode="counting_and_probability", gpt_answer=sample["gpt4o_answer"])
                judgment = judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "counting_and_probability"
                })
        except Exception as e:
            print(f"Error during experiment: {e}")
    print(f"Experiment completed, results count: {len(results)}")
    return results

def run_nonthinking_experiment(test_questions):
    results = []
    for sample in tqdm(test_questions, desc=f"Judging Questions)"):
        try:
            if sample["topic"] == "algebra":
                prompt = judge_prompt_nonthinking(sample["question"], mode="algebra", gpt_answer=sample["gpt4o_answer"])
                judgment = judge_with_nonthinking_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "algebra"
                })
                print(judgment)
            elif sample["topic"] == "number_theory":
                prompt = judge_prompt_nonthinking(sample["question"], mode="number_theory", gpt_answer=sample["gpt4o_answer"])
                judgment = judge_with_nonthinking_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "number_theory"
                })
            else:
                prompt = judge_prompt_nonthinking(sample["question"], mode="counting_and_probability", gpt_answer=sample["gpt4o_answer"])
                judgment = judge_with_nonthinking_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "counting_and_probability"
                })
        except Exception as e:
            print(f"Error during experiment: {e}")
    print(f"Experiment completed, results count: {len(results)}")
    return results

def run_small_experiment(test_questions):
    results = []
    for sample in tqdm(test_questions, desc=f"Judging Questions)"):
        try:
            if sample["topic"] == "algebra":
                prompt = judge_prompt(sample["question"], mode="algebra", gpt_answer=sample["gpt4o_answer"])
                judgment = small_judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "algebra"
                })
            elif sample["topic"] == "number_theory":
                prompt = judge_prompt(sample["question"], mode="number_theory", gpt_answer=sample["gpt4o_answer"])
                judgment = small_judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "number_theory"
                })
            else:
                prompt = judge_prompt(sample["question"], mode="counting_and_probability", gpt_answer=sample["gpt4o_answer"])
                judgment = small_judge_with_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "counting_and_probability"
                })
        except Exception as e:
            print(f"Error during experiment: {e}")
    print(f"Experiment completed, results count: {len(results)}")
    return results

def run_small_nonthinking_experiment(test_questions):
    results = []
    for sample in tqdm(test_questions, desc=f"Judging Questions)"):
        try:
            if sample["topic"] == "algebra":
                prompt = judge_prompt_nonthinking(sample["question"], mode="algebra", gpt_answer=sample["gpt4o_answer"])
                judgment = small_judge_with_nonthinking_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "algebra"
                })
            elif sample["topic"] == "number_theory":
                prompt = judge_prompt_nonthinking(sample["question"], mode="number_theory", gpt_answer=sample["gpt4o_answer"])
                judgment = small_judge_with_nonthinking_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "number_theory"
                })
            else:
                prompt = judge_prompt_nonthinking(sample["question"], mode="counting_and_probability", gpt_answer=sample["gpt4o_answer"])
                judgment = small_judge_with_nonthinking_qwen(prompt)
                results.append({
                    "id": sample["id"],
                    "topic": sample["topic"],
                    "difficulty": sample["difficulty"],
                    "question": sample["question"],
                    "gpt4o_answer": sample["gpt4o_answer"],
                    "solution": sample["solution"],
                    "judgment": judgment,
                    "mode": "counting_and_probability"
                })
        except Exception as e:
            print(f"Error during experiment: {e}")
    print(f"Experiment completed, results count: {len(results)}")
    return results

def main():
    # test_questions = load_questions(TEST_DIR, num_questions=20)

    # generate_answers(test_questions, GPT_OUTPUT)

    with open(GPT_OUTPUT, "r") as f:
        test_questions_with_answers = [json.loads(line) for line in f]

    # print("##### Running Setup A #####")
    # setup_a_results = run_experiment(test_questions_with_answers)
    # print(f"Setup A results count: {len(setup_a_results)}")
    # with open("results/setup_a.jsonl", "w") as f:
    #     for result in setup_a_results:
    #         f.write(json.dumps(result) + "\n")
    # print("Setup A file written.")

    setup_b_results = run_nonthinking_experiment(test_questions_with_answers)
    print(f"Setup B results count: {len(setup_b_results)}")
    with open("results/setup_b.jsonl", "w") as f:
        for result in setup_b_results:
            f.write(json.dumps(result) + "\n")
    print("Setup B file written.")

    setup_c_results = run_small_experiment(test_questions_with_answers)
    print(f"Setup C results count: {len(setup_c_results)}")
    with open("results/setup_c.jsonl", "w") as f:
        for result in setup_c_results:
            f.write(json.dumps(result) + "\n")
    print("Setup C file written.")

    setup_d_results = run_small_nonthinking_experiment(test_questions_with_answers)
    print(f"Setup D results count: {len(setup_d_results)}")
    with open("results/setup_d.jsonl", "w") as f:
        for result in setup_d_results:
            f.write(json.dumps(result) + "\n")
    print("Setup D file written.")

    # With Solution
    # print("##### Running Setup B #####")
    # setup_b_results = run_experiment(test_questions_with_answers, mode="B")
    # print(f"Setup B results count: {len(setup_b_results)}")
    # with open("results/setup_b.jsonl", "w") as f:
    #     for result in setup_b_results:
    #         f.write(json.dumps(result) + "\n")
    # print("Setup B file written.")

    # print("##### Running Baseline #####")
    # baseline_results = run_experiment(test_questions_with_answers, mode="Baseline")
    # print(f"Baseline results count: {len(baseline_results)}")
    # with open("results/baseline.jsonl", "w") as f:
    #     for result in baseline_results:
    #         f.write(json.dumps(result) + "\n")
    # print("Baseline file written.")

if __name__ == "__main__":
    main()