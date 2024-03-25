import os
import pandas as pd

class PandasExporter:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def export_to_txt(self, file_name=None):
        if file_name is None:
            file_name = "output.txt"
        file_path = os.path.join(os.getcwd(), file_name)
        
        # Dataframe veranderen in een TSV opzet
        df_string = self.dataframe.to_csv(index=False, sep='\t')

        # String wegschrijven naar txt bestand
        with open(file_path, 'w') as file:
            file.write(df_string)












