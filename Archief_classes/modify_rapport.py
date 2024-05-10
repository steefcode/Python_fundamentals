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



class ValueModifier:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def add_row(self, row_data):
        self.dataframe = self.dataframe.pd.concat(row_data, ignore_index=True)
    
    def modify_value(self, inspecteur, bedrijf, column, new_value):
        self.dataframe[column] = np.where(self.dataframe[inspecteur] and self.dataframe[bedrijf], new_value, column) 

rapporten_class = ValueModifier(rapporten) 

# Testen waarde wijzigen 
rapport_inspecteur = input("Voor welke ICode wilt u een verandering? ")
rapport_bedrijf = input("Voor welk Bcode wilt u een verandering doorvoeren? ")
rapport_kolom = input("Voor welke kolom wilt u een waarde wijzigen? ")
rapport_waarde = input("Voer de waarde om de wijziging te realiseren ")



# Testen waarde toevoegen 
new_row = pd.DataFrame({'Icode': "Test", 'Bcode': "Test"}, index= [0])

rapporten_class.modify_value('001', '0001', "Opm", "Test")
rapporten_class.add_row(new_row)

test = pd.concat(rapporten, new_row)



print(rapporten)








import pandas as pd
# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
					'Name': ['ABC', 'PQR', 'DEF', 'GHI']})

# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
					'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})


frames = [df1, df2]

result = pd.concat(frames)
print(result)


import pandas as pd

class DataFrameConcatenator:
    def __init__(self, dataframe1, dataframe2):
        self.dataframe1 = dataframe1
        self.dataframe2 = dataframe2

    def concatenate_dataframes(self):
        concatenated_df = pd.concat([self.dataframe1, self.dataframe2], ignore_index=True)
        return concatenated_df





