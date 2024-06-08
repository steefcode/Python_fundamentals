import os
import pandas as pd

class PandasExporter:
    """
    Een Class om de pandas dataframes te exporteren naar een txt file .
    """
    def __init__(self, dataframe):
        """
        Checken of het object een pandas dataframe is.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input moet een pandas dataframe zijn.")
        self.dataframe = dataframe

    def export_to_txt(self, file_name=None):
        """
        Export DataFrame naar ee txt bestand.
        Indien er geen object wordt oegewezen wordt een leeg bestand output.txt gemaakt. 
        """
        if file_name is None:
            file_name = "output.txt"
        file_path = os.path.join(os.getcwd(), file_name)
        
        # Converteren pandas dataframe naar TSV-format string
        df_string = self.dataframe.to_csv(index=False, sep='\t')
        
        # TSV-format string wegschrijven
        with open(file_path, 'w') as file:
            file.write(df_string)














