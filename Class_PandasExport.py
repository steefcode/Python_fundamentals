import os
import pandas as pd

class PandasExporter:
    """
    A class to export Pandas DataFrame to tab-separated text files.
    """
    def __init__(self, dataframe):
        """
        Initialize PandasExporter with a DataFrame object.
        
        Parameters:
        dataframe (DataFrame): The DataFrame to export.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a Pandas DataFrame")
        self.dataframe = dataframe

    def export_to_txt(self, file_name=None):
        """
        Export DataFrame to a tab-separated text file.
        
        Parameters:
        file_name (str): The name of the output text file. If not provided, defaults to "output.txt".
        """
        if file_name is None:
            file_name = "output.txt"
        file_path = os.path.join(os.getcwd(), file_name)
        
        # Convert DataFrame to TSV-formatted string
        df_string = self.dataframe.to_csv(index=False, sep='\t')
        
        # Write string to text file
        with open(file_path, 'w') as file:
            file.write(df_string)














