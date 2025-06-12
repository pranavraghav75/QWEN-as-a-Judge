def judge_prompt(question, gpt_answer=None, solution=None, mode="A"):
    if mode == "A":  # Main Evaluation
        return f"""
        You are tasked with evaluating the correctness and quality of an answer provided by GPT-4o to a mathematical question. 
        Below is the question and GPT-4o's answer.

        Question: {question}

        GPT-4o Answer: {gpt_answer}

        Your task:
        1. Assess whether GPT-4o's answer is correct, partially correct, or incorrect.
        2. Provide feedback on the reasoning and approach used in GPT-4o's answer.
        3. If GPT-4o's answer is incorrect or incomplete, explain the discrepancies and suggest improvements.

        Provide your evaluation in a concise and structured format.
        """
    elif mode == "B":  # Control
        return f"""
        You are tasked with evaluating the correctness and quality of an answer provided by GPT-4o to a mathematical question. 
        Below is the question, GPT-4o's answer, and the correct solution.

        Question: {question}

        GPT-4o Answer: {gpt_answer}

        Solution: {solution}

        Your task:
        1. Compare GPT-4o's answer with the solution provided.
        2. Assess whether GPT-4o's answer is correct, partially correct, or incorrect.
        3. Provide feedback on the reasoning and approach used in GPT-4o's answer.
        4. If GPT-4o's answer is incorrect or incomplete, explain the discrepancies and suggest improvements.

        Provide your evaluation in a concise and structured format.
        """
    elif mode == "Baseline":  # Solver
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