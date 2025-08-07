
# Step 2: Load the dataset from Hugging Face
from datasets import load_dataset

# Load the dataset (only the "train" split exists)
dataset = load_dataset("coachprerakmehta/data_jobs", split="train")

# Step 3: Convert to pandas DataFrame
df = dataset.to_pandas()

# Step 4: Save as CSV
df.to_csv("data_jobs.csv", index=False)
from datasets import load_dataset

# Load the dataset from Hugging Face
dataset = load_dataset("coachprerakmehta/data_jobs", split="train")

# Save to CSV (you can change the path as needed)
dataset.to_csv("data_jobs.csv")


