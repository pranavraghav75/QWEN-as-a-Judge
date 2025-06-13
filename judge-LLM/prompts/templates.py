def judge_prompt(question, gpt_answer=None, solution=None, mode="A"):
    if mode == "A":  # Main Evaluation
        # return f"""
        # You are tasked with evaluating the correctness and quality of an answer provided by GPT-4o mini to a mathematical question. 
        # Below is the question and GPT-4o mini's answer.

        # Question: {question}

        # GPT-4o mini Answer: {gpt_answer}

        # Your task:
        # 1. Assess whether GPT-4o mini's answer is correct, partially correct, or incorrect.
        # 2. Provide feedback on the reasoning and approach used in GPT-4o mini's answer.
        # 3. If GPT-4o mini's answer is incorrect or incomplete, explain the discrepancies and suggest improvements.

        # Evaluation:
        # State your judgement clearly and concisely, and the final evaluatoin in one of the following formats: "The answer is correct", "The answer is partially correct", or "The answer is incorrect".
        # """
    
        return f"""
        You are tasked with evaluating the correctness and quality of an answer provided by GPT-4o mini to a mathematical question.

        Question:
        {question}

        GPT-4o mini's Answer:
        {gpt_answer}

        Your task:
        1. Assess the reasoning and approach of GPT-4o mini's answer and decide whether the answer is **correct** or **incorrect**.
        2. Explain why in 1-2 sentences.
        3. End your response with a final line: 
        "The answer is correct." or "The answer is partially correct." or "The answer is incorrect."
        """

    elif mode == "B":  # Control
        return f"""
        You are tasked with evaluating the correctness and quality of an answer provided by GPT-4o mini to a mathematical question. 
        Below is the question, GPT-4o mini's answer, and the correct solution.

        Question: {question}

        GPT-4o mini Answer: {gpt_answer}

        Solution: {solution}

        Your task:
        1. Compare GPT-4o mini's answer with the solution provided.
        2. Assess whether GPT-4o mini's answer is correct, partially correct, or incorrect.
        3. Provide feedback on the reasoning and approach used in GPT-4o mini's answer.
        4. If GPT-4o mini's answer is incorrect or incomplete, explain the discrepancies and suggest improvements.

        Evaluation:
        State your judgement clearly and concisely, and the final evaluatoin in one of the following formats: "The answer is correct", "The answer is partially correct", or "The answer is incorrect".
        """
    elif mode == "Baseline":  # Baseline
        return f"""
        You are tasked with solving the following mathematical question independently. 
        Below is the question and the correct solution.

        Question: {question}

        Solution: {solution}

        Your task:
        1. Solve the question and provide your answer.
        2. Compare your answer to the solution provided and assess correctness.

        Provide your solution and evaluation in a concise and structured format.
        """