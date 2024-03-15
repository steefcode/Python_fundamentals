import pandas as pd

class PandasExporter:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def export_to_txt(self, file_path):
        # Pandas dataframe omzetten naar een string
        df_string = self.dataframe.to_string(index=False, header = False)  # Verwijderen van headers en index rijen 

        # De regels van de dataframe string wegschrijven in een txt bestand
        with open(file_path, 'w') as file:
            file.writelines(df_string)

        print(f"De gegevens zijn opgeslagen")


