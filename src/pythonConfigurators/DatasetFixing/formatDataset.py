import pandas as pd
import csv


# Input dataset path
inputDatasetPath = "src/questions/Data_dump.csv"
# Output dataset path
outputDatasetPath = "src/questions/Formated_Data_dump.csv"

# Read the CSV file and replace commas with semicolons
with open(inputDatasetPath, mode='r', newline='', encoding='utf-8') as infile, \
    open(outputDatasetPath, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=';')
    
    for row in reader:
        writer.writerow(row)

# Verify the output
df = pd.read_csv(outputDatasetPath, delimiter=';')
print(df.head(1))