def judge_prompt(question, gpt_answer=None, solution=None, mode="A"):
    if mode == "A": # Main Evaluation
        return f"""
        You are a math evaluator. Given a question and a student's answer, decide if the answer is mathematically correct.

        Question:
        {question}

        Student Answer:
        {gpt_answer}

        Respond in this JSON format with two keys:
        - "verdict": pick only one from "correct" or "incorrect"
        - "justification": one-sentence explanation based on math logic

        Only return one single valid JSON response. Do not include any extra text or commentary.
        """

    elif mode == "B":  # Control
        return f"""
        You are a math evaluator. Given a question, a student's answer, and the correct solution, determine if the student's answer is correct by comparing it to the solution.

        Question:
        {question}

        Student Answer:
        {gpt_answer}

        Correct Solution:
        {solution}

        Respond in this JSON format with two keys:
        - "verdict": pick only one from "correct" or "incorrect"
        - "justification": one-sentence explanation based on math logic

        Only return one single valid JSON response. Do not include any extra text or commentary.
        """

    # elif mode == "Baseline":  # Baseline
    #     return f"""
    #     You are tasked with solving the following mathematical question independently. 

    #     Question: {question}

    #     Solution: {solution}

    #     Your task:
    #     1. Solve the question and provide your answer.
    #     2. Compare your answer to the solution provided and assess correctness.

    #     Provide your solution and evaluation in a concise and structured format.
    #     """