import pandas as pd

# Input dataset path
inputDatasetPath = "src/questions/Formated_Data_dump.csv"

# Read the data_dump csv so that I can insert a schema in it to make it more usable
dataset_questions = pd.read_csv(inputDatasetPath, delimiter=';')
array_2d = dataset_questions.values

# Define the schema that is gonna be inserted inside the dataset
schema = ['id', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']

print(dataset_questions.head(1))

newDataset_questions = pd.DataFrame(data=array_2d, columns=schema)

# Save the updated dataset to the same file
newDataset_questions.to_csv("src\questions\Formated_Data_dump_schema.csv", sep=';', index=False)
