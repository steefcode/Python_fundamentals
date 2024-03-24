import pandas as pd

class Modifier_Rapport:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def wijzigen_rapport(self, rij_index, kolom_naam, waarde):
        '''Check of de status kolom een d bevat op de gegeven index'''
        if self.dataframe.loc[rij_index, 'Status']  == 'd':
            print("Waarde kan niet worden aangepast omdat deze ")

        # Voer de verandering uit op de rij index en kolom 
        self.dataframe.at[rij_index, kolom_naam] = waarde

        return self.dataframe




