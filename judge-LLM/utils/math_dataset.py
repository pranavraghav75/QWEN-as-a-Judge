import os
import json

def load_math_questions(data_dir):
    topics = ["algebra", "number_theory", "counting_and_probability"]
    samples = []
    for topic in topics:
        topic_dir = os.path.join(data_dir, topic)
        for fname in os.listdir(topic_dir):
            if fname.endswith(".json"):
                with open(os.path.join(topic_dir, fname)) as f:
                    data = json.load(f)
                    samples.append({
                        "id": f"{topic}/{fname.replace('.json', '')}",
                        "topic": topic,
                        "level": data.get("level", "unknown"),
                        "question": data["problem"],
                        "solution": data["solution"]
                    })
    return samples
