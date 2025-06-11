def judge_prompt(question, model_answer):
    return f"""You are a math judge. You are given a high school-level math question and an answer. Your job is to assess whether the answer is correct. First, solve the problem yourself. Then compare your solution to the given answer and say if it is correct.

Question: {question}

Answer by Model: {model_answer}

Your Solution and Judgment:"""
