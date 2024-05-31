# import pandas as pd

# class DataFrameConcatenator:
#     def __init__(self):
#         self.dataframes = []

#     def add_dataframe(self, dataframe):
#         """
#         Add a DataFrame to the list of DataFrames to concatenate.

#         Parameters:
#         dataframe (pandas.DataFrame): The DataFrame to add.

#         Raises:
#         ValueError: If the input is not a pandas DataFrame.
#         """
#         if not isinstance(dataframe, pd.DataFrame):
#             raise ValueError("Input for concatenation must be a pandas DataFrame type")
#         self.dataframes.append(dataframe)

#     def concatenate(self, axis=0, reset_index=True):
#         """
#         Concatenate the DataFrames.

#         Parameters:
#         axis (int, optional): The axis along which to concatenate. Defaults to 0.

#         Returns:
#         pandas.DataFrame or None: The concatenated DataFrame if DataFrames are present, else None.
#         """
#         if not self.dataframes:
#             return None
        
#         concatenated_df = pd.concat(self.dataframes, axis=axis)
        
#         # Reassign the data types of the columns from the first DataFrame
#         for col_naam, col_type in self.dataframes[0].dtypes.items():
#             concatenated_df[col_naam] = concatenated_df[col_naam].astype(col_type)
        
#         return concatenated_df

import pandas as pd

class DataFrameConcatenator:
    def __init__(self):
        self.dataframes = []

    def add_dataframe(self, dataframe):
        """
        Add a DataFrame to the list of DataFrames to concatenate.

        Parameters:
        dataframe (pandas.DataFrame): The DataFrame to add.

        Raises:
        ValueError: If the input is not a pandas DataFrame.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input for concatenation must be a pandas DataFrame type")
        self.dataframes.append(dataframe)

    def concatenate(self, axis=0, reset_index=True):
        """
        Concatenate the DataFrames.

        Parameters:
        axis (int, optional): The axis along which to concatenate. Defaults to 0.
        reset_index (bool, optional): Whether to reset the index of the resulting DataFrame. Defaults to True.

        Returns:
        pandas.DataFrame or None: The concatenated DataFrame if DataFrames are present, else None.
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
