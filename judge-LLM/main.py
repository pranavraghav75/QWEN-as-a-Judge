from utils.math_dataset import load_math_questions
from gpt4o.generate_answers import generate_answers
from judge.run_judging import run_judging

DATA_DIR = "data/MATH"
GPT_OUTPUT = "results/gpt4o_answers.jsonl"
JUDGMENT_OUTPUT = "results/judgments.jsonl"

def main():
    questions = load_math_questions(DATA_DIR)
    generate_answers(questions, GPT_OUTPUT)
    run_judging(GPT_OUTPUT, JUDGMENT_OUTPUT)

if __name__ == "__main__":
    main()