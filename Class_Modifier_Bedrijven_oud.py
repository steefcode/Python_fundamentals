import pandas as pd

bedrijven.loc[0, "Controle"]

test_index = int(input("Voer een index regel in ")) - 1
kolom = input("Voer een kolom in ")

def wijzigen_bedrijf(rij_index, kolom_index, waarde):
    try: 
        if bedrijven.loc[rij_index, kolom_index] == 'j':
            print("Deze waarde mag niet worden gewijzigd omdat er al een controle is geweest. ")
        elif kolom_index == "Code":
            print("Van een bestaand bedrijf mag de code niet worden aangepast")
        elif kolom_index == "Straat": 
            print("De locatie van een bedrijf mag niet ")
        else:
            bedrijven.loc[rij_index, kolom_index] = waarde
    except KeyError: 
        print("kolom komt niet voor in de keuze")


import pandas as pd

class BedrijfWijziger:
    def __init__(self, bedrijven_dataframe):
        self.bedrijven = bedrijven_dataframe

    def wijzigen_bedrijf(self, rij_index, kolom_index, waarde):
        try:
            if self.bedrijven.loc[rij_index, kolom_index] == 'j':
                print("Deze waarde mag niet worden gewijzigd omdat er al een controle is geweest.")
            elif kolom_index == "Code":
                print("Van een bestaand bedrijf mag de code niet worden aangepast.")
            elif kolom_index == "Straat":
                print("De locatie van een bedrijf mag niet worden gewijzigd.")
            else:
                self.bedrijven.loc[rij_index, kolom_index] = waarde
        except KeyError:
            print("De opgegeven kolom komt niet voor in de keuze.")




















class DataFrameModifier:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def check_controle(self, index):
        return self.df.loc[index, 'Controle'] != 'j'

    def modify_value(self, index, column, new_value):
        if column == 'Controle':
            print("Cannot modify 'Controle' column.")
            return

        if self.check_controle(index):
            self.df.loc[index, column] = new_value
        else:
            print(f"Cannot modify '{column}' when 'Controle' is 'j'.")

    def get_dataframe(self):
        return self.df

# Example usage:
data = {
    'Code': [101, 102, 103, 104],
    'Naam': ['John', 'Alice', 'Bob', 'Eve'],
    'Straat': ['Main St', 'Park Ave', 'Oak St', 'Maple Rd'],
    'Controle': ['a', 'b', 'j', 'c']
}

df = pd.DataFrame(data)
modifier = DataFrameModifier(df)

print("Original DataFrame:")
print(df)

# Try modifying values
modifier.modify_value(2, 'Code', 203)      # Modify 'Code' even when 'Controle' is 'j'.
modifier.modify_value(2, 'Naam', 'Carl')   # Modify 'Naam' even when 'Controle' is 'j'.
modifier.modify_value(2, 'Straat', 'Elm St')  # Modify 'Straat' even when 'Controle' is 'j'.
modifier.modify_value(2, 'Controle', 'x')  # Cannot modify 'Controle' column.

print("\nModified DataFrame:")
print(modifier.get_dataframe())
