import pandas as pd

class DataFrameModifier:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def add_column(self, column_name, column_data):
        self.dataframe[column_name] = column_data
    
    def remove_column(self, column_name):
        self.dataframe.drop(column_name, axis=1, inplace=True)
    
    def filter_rows(self, condition):
        self.dataframe = self.dataframe[condition]
    
    def modify_column(self, column_name, modification):
        self.dataframe[column_name] = modification(self.dataframe[column_name])
    
    def show_dataframe(self):
        print(self.dataframe)


# Example usage
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# Create an instance of DataFrameModifier
modifier = DataFrameModifier(df)

# Add a new column
modifier.add_column('Country', ['USA', 'France', 'UK'])

# Remove a column
modifier.remove_column('City')

# Filter rows based on a condition
modifier.filter_rows(modifier.dataframe['Age'] > 25)

# Modify a column using a lambda function
modifier.modify_column('Age', lambda x: x + 1)

# Show the modified DataFrame
modifier.show_dataframe()
