from datasets import load_dataset

# Load the dataset from Hugging Face
dataset = load_dataset("coachprerakmehta/data_jobs", split="train")

# Save to CSV (you can change the path as needed)
dataset.to_csv("data_jobs.csv")
