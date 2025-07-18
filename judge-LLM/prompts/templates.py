def judge_prompt(question, mode, gpt_answer):
    topic = {
        "algebra": "algebra",
        "number_theory": "number theory",
        "counting_and_probability": "counting and probability"
    }.get(mode, "mathematics")

    return f"""You are a mathematical evaluator specailzing in  {topic}. You are NOT to assume the student's answer is correct. Instead, verify the answer independently based on your own math reasoning.

    Instructions:
    1) Think through the problem on your own first, concisely explaining your reasoning and solution.
    2) Compare the student's answer to your own.
    3) Your response must state a "verdict" field as one of {"correct", "incorrect", "incomplete"}, followed by a justification if the answer is incorrect or incomplete.

    Problem:
    {question}

    Student's Answer:
    {gpt_answer}
    """

def judge_prompt_nonthinking(question, mode, gpt_answer):
    topic = {
        "algebra": "algebra",
        "number_theory": "number theory",
        "counting_and_probability": "counting and probability"
    }.get(mode, "mathematics")

    return f"""You are a mathematical evaluator specailzing in  {topic}. You are NOT to assume the student's answer is correct. Verify the student's answer based on your own math reasoning without any additional thinking.

    Instructions:
    - Output EXACTLY ONE of: correct, incorrect, incomplete.
    - If incorrect or incomplete, append a short justification in ONE sentence.

    Problem:
    {question}

    Student's Answer:
    {gpt_answer}
    /no_think
    """




# added the incopmlete state to verdict and changd answer generation script slightly

# for judging, look at answers starting from and including the changes made to temp 0.4 to 0.3 ...


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