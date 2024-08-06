import pandas as pd

# Input dataset path
inputDatasetPath = "src/questions/Latest_Dataset.csv"

# Read the data_dump csv so that I can insert a schema in it to make it more usable
dataset_questions = pd.read_csv(inputDatasetPath, delimiter=';')

# Drop the id column since the index is wrong
if 'id' in dataset_questions.columns:
    dataset_questions.drop('id', inplace=True, axis=1)
else:
    print("Column id does not exist in this dataset!!")

# Insert a new column called probability that takes for value only one's
if "probability" not in dataset_questions.columns:
    dataset_questions["probability"] = 1
else:
    print("Column probability already exists in this dataset, and cannot be added!!")

# Write the dataset to a csv file 
# dataset_questions.to_csv(inputDatasetPath, sep=";", index=False)

