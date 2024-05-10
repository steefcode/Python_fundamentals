import pandas as pd 
import numpy as np 
from tabulate import tabulate
from datetime import date, datetime

"""Colspecs definieren voor het inlezen bestanden"""
colspecs = [(0,3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]

"""Inlezen van rapporten"""
rapporten = pd.read_fwf("rapporten.txt", header = None, colspecs = colspecs, 
                            names = ["Icode", 
                                     "Bcode", 
                                     "Bezdat", 
                                     "Rapdat", 
                                     "Status", 
                                     "Opm"], 
                            dtype = {"Icode" : str, 
                                    "Bcode" : str, 
                                    "Bezdat" : str, 
                                    "Rapdat" : str, 
                                    "Status" : str,
                                    "Opm" : str}, 
                            parse_dates = ["Bezdat", "Rapdat"])

print(rapporten)

class Modifier_Rapporten:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def wijzigen_rapport(self, condition_value, target_column, new_value):
        if 'd' not in self.dataframe['Status'].values:
            rows_to_modify = self.dataframe.index[self.dataframe['status'] != condition_value]
            self.dataframe.loc[rows_to_modify, target_column] = new_value
            print("Values modified successfully.")
        else:
            print("Values cannot be modified because 'd' exists in the status column.")

# data = {'status': ['a', 'b', 'c', 'd', 'e'],
#         'value': [1, 2, 3, 4, 5]}
# df = pd.DataFrame(data)

modifier = Modifier_Rapporten(rapporten)
print(df)

modifier.wijzigen_rapport('d', 'value', 10)
print(df)

modifier.modify_value('d', 'value', 20)
print(df)

