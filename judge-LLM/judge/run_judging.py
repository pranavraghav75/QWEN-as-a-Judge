import json
from tqdm import tqdm
from judge.qwen_judge import judge_with_qwen

def run_judging(gpt4o_path, output_path):
    with open(gpt4o_path) as f:
        lines = [json.loads(l) for l in f]

    if not lines:
        print(f"No answers found in {gpt4o_path}")
        return

    with open(output_path, "w") as out:
        for item in tqdm(lines, desc="Judging with QWEN"):
            judgment = judge_with_qwen(item["question"], item["gpt4o_answer"])
            if not judgment:
                print(f"Failed to judge answer for question: {item['question']}")
                continue
            out.write(json.dumps({
                "id": item["id"],
                "topic": item["topic"],
                "judgment": judgment,
                "gpt4o_answer": item["gpt4o_answer"],
                "solution": item["solution"]
            }) + "\n")
    print(f"Judgments written to {output_path}")