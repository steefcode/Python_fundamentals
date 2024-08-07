import pandas as pd

class Subset_Bedrijfsnaam:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def zoek_bedrijfsnaam(self, substring_zoeken):
        try:
            # Subset data op bases van str.contains iloc[0] om eerste resultaat weer te geven.
            subset_data = self.df[self.df['Naam'].str.contains(substring_zoeken, case=False)].iloc[0]
            return subset_data
        except IndexError:
            print(f"De substring '{substring_zoeken}' is niet gevonden in de kolom 'Naam'.")
            return None
