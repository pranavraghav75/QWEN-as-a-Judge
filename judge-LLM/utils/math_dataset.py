import os
import json
import random

def load_math_questions(data_dir):
    topics = ["algebra", "number_theory", "counting_and_probability"]
    split = "train"
    samples = []

    for topic in topics:
        topic_dir = os.path.join(data_dir, split, topic)
        if not os.path.exists(topic_dir):
            continue
        for fname in os.listdir(topic_dir):
            if fname.endswith(".json"):
                with open(os.path.join(topic_dir, fname)) as f:
                    try:
                        data = json.load(f)
                        samples.extend(data)
                    except json.JSONDecodeError:
                        print(f"Skipping invalid JSON file: {fname}")
                        continue

        samples = random.sample(samples, min(len(samples), random.randint(25, 50)))

    return samples