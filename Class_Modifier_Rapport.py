import pandas as pd

class Modifier_Rapport:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def wijzigen_rapport(self, row_index, column_name, new_value):
        '''Check of de status kolom een d bevat op de gegeven index'''
        if self.dataframe.loc[row_index, 'Status']  == 'd':
            print("Waarde kan niet worden aangepast omdat deze ")

        # Voer de verandering uit op de rij index en kolom 
        self.dataframe.at[row_index, column_name] = new_value




