def judge_prompt(question, mode, gpt_answer):
    topic = {
        "algebra": "algebra",
        "number_theory": "number theory",
        "counting_and_probability": "counting and probability"
    }.get(mode, "mathematics")

    return f"""You are a mathematical judge. You specialize in solving {topic} problems. Your task is to determine whether a student's answer to a math question is mathematically correct.

    Question:
    {question}

    Student Answer:
    {gpt_answer}

    Do not include any extra text or commentary. Only return your answer in this JSON format:
    {{
    "analysis": one-sentence explanation that clearly justifies your verdict using math logic
    "verdict": correct or incorrect
    }}
    """

# added in the json brakcets, also moved the rquirement to after the question and answer
# also removed the requirements part and just made it short and simple, no extra words and only return in json format

# def judge_prompt(question, gpt_answer=None, solution=None, mode="A"):
#     # if mode == "A": # Main Evaluation
#         # return f"""
#         # You are a math evaluator. Given a question and a student's answer, decide if the answer is mathematically correct.

#         # Question:
#         # {question}

#         # Student Answer:
#         # {gpt_answer}

#         # Respond in this JSON format with two keys:
#         # - "analysis": one-sentence explanation based on math logic
#         # - "verdict": pick only one from "correct" or "incorrect"

#         # Guildelines:
#         # - Be objective and strict in your evaluation.
#         # - Only mark "correct" if the answer is fully mathematically valid.
#         # - Do not explain your reasoning outside the JSON. Do not include any extra text or commentary.
#         # """
    
#     # Prompt for Algebra
#     if mode == "algebra":
#         return f"""You are a mathematical judge that assesses whether the question has been answered correctly. \
#             You excel at solving algebra questions. \
#             You will be provided with the original question, and an answer with explanations. \
#             Your job is to tell whether the provided answer is correct or not. \
#             Give out your final judgment at the end of your evaluation. \
#             Your final judgment should strictly follow the following format: My Judgment: ###judgment###. \
#             Replace the content inside the hashtags with your judgment, which should be either correct or wrong."""
#     elif mode == "number_theory":
#         return f"""You are a mathematical judge that assesses whether the question has been answered correctly. \
#             You excel at solving number theory questions. \
#             You will be provided with the original question, and an answer with explanations. \
#             Your job is to tell whether the provided answer is correct or not. \
#             Give out your final judgment at the end of your evaluation. \
#             Your final judgment should strictly follow the following format: My Judgment: ###judgment###. \
#             Replace the content inside the hashtags with your judgment, which should be either correct or wrong."""
#     else:
#         return f"""You are a mathematical judge that assesses whether the question has been answered correctly. \
#             You excel at solving counting and probability questions. \
#             You will be provided with the original question, and an answer with explanations. \
#             Your job is to tell whether the provided answer is correct or not. \
#             Give out your final judgment at the end of your evaluation. \
#             Your final judgment should strictly follow the following format: My Judgment: ###judgment###. \
#             Replace the content inside the hashtags with your judgment, which should be either correct or wrong."""

#     # elif mode == "B":  # Control
#     #     return f"""
#     #     You are a math evaluator. Given a question, a student's answer, and the correct solution, determine if the student's answer is correct by comparing it to the solution.

#     #     Question:
#     #     {question}

#     #     Student Answer:
#     #     {gpt_answer}

#     #     Correct Solution:
#     #     {solution}

#     #     Respond in this JSON format with two keys:
#     #     - "analysis": one-sentence explanation based on math logic
#     #     - "verdict": pick only one from "correct" or "incorrect"

#     #     Guildelines:
#     #     - Be objective and strict in your evaluation.
#     #     - Only mark "correct" if the answer is fully mathematically valid.
#     #     - Do not explain your reasoning outside the JSON. Do not include any extra text or commentary.
#     #     """

#     # elif mode == "Baseline":  # Baseline
#     #     return f"""
#     #     You are tasked with solving the following mathematical question independently. 

#     #     Question: {question}

#     #     Solution: {solution}

#     #     Your task:
#     #     1. Solve the question and provide your answer.
#     #     2. Compare your answer to the solution provided and assess correctness.

#     #     Provide your solution and evaluation in a concise and structured format.
#     #     """

# # Commenting out Mode B prompting
# # system_message_judge_mode_b = \
# #     f"""You are a mathematical judge that assesses whether the question has been answered correctly. \
# #         You will be provided with the original question, an answer with explanations, and the ground-truth solution. \
# #         Your job is to tell whether the provided answer is correct or not, considering the ground-truth solution. \
# #         Give out your final judgment at the end of your evaluation. \
# #         Your final judgment should strictly follow the following format: My Judgment: ###judgment###. \
# #         Replace the content inside the hashtags with your judgment, which should be either correct or wrong."""