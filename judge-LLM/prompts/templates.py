def judge_prompt(question, gpt_answer=None, solution=None, mode="A"):
    if mode == "A":  # Main Evaluation
        return f"""
        You are evaluating the correctness of a math answer by GPT-4o mini.

        Question:
        {question}

        GPT-4o mini's Answer:
        {gpt_answer}

        Respond in this exact JSON format:
        {{"verdict": "correct" or "incorrect", "justification": "<short one-sentence explanation>"}}
        Only return valid JSON and nothing else.
        """

    elif mode == "B":  # Control
        return f"""
        You are evaluating the correctness of a math answer by GPT-4o mini by comparing with the solution.

        Question: {question}

        GPT-4o mini Answer: {gpt_answer}

        Solution: {solution}

        Respond in this exact JSON format:
        {{"verdict": "correct" or "incorrect", "justification": "<short one-sentence explanation>"}}
        Only return valid JSON and nothing else.
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