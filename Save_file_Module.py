import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Specify the file path
file_path = 'data.txt'

# Convert DataFrame to string representation
data_string = df.to_string(index=False, header=False)

# Write DataFrame contents to file
with open(file_path, 'w') as file:
    file.write(data_string)
