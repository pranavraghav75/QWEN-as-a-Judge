def judge_prompt(question, gpt_answer=None, solution=None, mode="A"):
    if mode == "A":  # Main Evaluation
        return f"""
        You are tasked with evaluating the correctness and quality of an answer provided by GPT-4o mini to a mathematical question.

        Question:
        {question}

        GPT-4o mini's Answer:
        {gpt_answer}

        Your task:
        1. Assess the reasoning and approach of GPT-4o mini's answer and decide whether the answer is correct or incorrect.
        2. Explain why concisely.

        Respond in this exact JSON format:
        {{
        "verdict": "correct" | "incorrect",
        "justification": "short explanation"
        }}
        """


    elif mode == "B":  # Control
        return f"""
        You are tasked with evaluating the correctness and quality of an answer provided by GPT-4o mini to a mathematical question.

        Question: {question}

        GPT-4o mini Answer: {gpt_answer}

        Solution: {solution}

        Your task:
        1. Assess and compare the reasoning and approach of GPT-4o mini's answer with the solution provided and decide whether the answer is correct or incorrect.
        2. Explain why concisely.

        Respond in this exact JSON format:
        {{
        "verdict": "correct" | "incorrect",
        "justification": "short explanation"
        }}
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