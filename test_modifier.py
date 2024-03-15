import pandas as pd

class DataFrameModifier:
    def __init__(self, df):
        self.df = df
    
    def add_row(self, row_values):
        self.df = pd.concat([self.df, row_values], ignore_index=True)
    
    def change_values(self, new_values):
        self.df.update(new_values)


df = pd.DataFrame({'A': [1, 2, 3], 'B': [400, 500, 600]})

# Create an instance of the DataFrameModifier class
modifier = DataFrameModifier(df)

# Add a row
new_row = pd.DataFrame({'A': [4], 'B': [700]})
modifier.add_row(new_row)

# Change values
new_values = pd.DataFrame({'B': [4, 5, 6]})
modifier.change_values(new_values)

print(modifier.df)
print(df)





import pandas as pd

class DataFrameModifier:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def modify_dataframe(self, row_index, new_value):
        status_value = self.dataframe.at[row_index, 'Status']
        
        if status_value == 'd':
            print("Cannot make changes to the DataFrame. Status value is 'd'.")
        else:
            self.dataframe.at[row_index, 'e'] = new_value
            print("Value in column 'e' updated successfully.")



# Creating a sample DataFrame
data = {
    'Status': ['a', 'b', 'd', 'c'],
    'e': [1, 2, 3, 4]
}
df = pd.DataFrame(data)

# Creating an instance of DataFrameModifier
modifier = DataFrameModifier(df)

# Modifying the DataFrame
modifier.modify_dataframe(1, 10)

# Output: Value in column 'e' updated successfully.

# Trying to modify a row with 'Status' value 'd'
modifier.modify_dataframe(2, 20)

# Output: Cannot make changes to the DataFrame. Status value is 'd'.
print(df)

# Compare input dates
while bezdat > rapdat:
    print("De rapportage datum is eerder dan de bezoekdatum. Zorg ervoor dat de bezoekdatum eerder is dan de rapportage datum")
    bezdat = input("Voer de bezoekdatum in in jjjj-mm-dd format ")
    rapdat = input("Voer de rapportagedatum in in jjjj-mm-dd format ")

bezdat = input("Voer de bezoekdatum in in jjjj-mm-dd format ")
rapdat = input("Voer de rapportagedatum in in jjjj-mm-dd format ")


import datetime

while bezdat == ValueError:
    print("Het door u ingevoerde is geen datum, vul aub een datum in met format yyyy-mm-dd")
    bezdat = input("")



#while bezdat == ValueError:
#    try:
#        datetime.date.fromisoformat(bezdat)
#    except:
#        raise ValueError("Incorrect date")
#    input("Het door u ingevoerde is geen datum, vul aub een datum in met format yyyy-mm-dd")

bezdat < rapdat





# check if input is een string in jjjj-mm-dd format 
