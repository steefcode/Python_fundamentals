import pandas as pd

class DataFrameConcatenator:
    def __init__(self):
        self.dataframes = []

    def add_dataframe(self, dataframe):
        """
        Dataframes toevoegen aan lijst. Met een check als deze geen dataframe is
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("De input moet een pandas dataframe zijn")
        self.dataframes.append(dataframe)

    def concatenate(self, axis=0, reset_index=True):
        """
        Samenvoegen van pandas dataframes die in de lijst zijn ingevoerd. 
        """
        if not self.dataframes:
            return None
        
        concatenated_df = pd.concat(self.dataframes, axis=axis)
        
        # Reassign the data types of the columns from the first DataFrame
        for col_name, col_type in self.dataframes[0].dtypes.items():
            concatenated_df[col_name] = concatenated_df[col_name].astype(col_type)
        
        if reset_index:
            concatenated_df.reset_index(drop=True, inplace=True)
        
        return concatenated_df
