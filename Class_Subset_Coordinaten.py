import pandas as pd

class Subsetcoordinaten:
    def __init__(self, data_frame):
        self.df = data_frame
        self.df['Xwaarde_float'] = self.df['Xwaarde'].astype(float)
        self.df['Ywaarde_float'] = self.df['Ywaarde'].astype(float)
    
    '''Formule om de kleinste afstand tussen de coordinaten te berekenen'''
    def verschil_coordinaten(self, input_x, input_y):
        self.df['verschil'] = ((self.df['Xwaarde_float'] - input_x) ** 2 + (self.df['Ywaarde_float'] - input_y) ** 2) ** 0.5
        df_sorted = self.df.sort_values('verschil')
        smallest_difference_row = df_sorted.iloc[0]
        self.df.drop(['verschil'], axis=1)
        return smallest_difference_row

'''Verwijderen van kolom difference, deze is niet in de originele dataset bedrijven, dus om problemen te voorkomen met wegschrijven en herladen wordt deze kolom verwijderd'''
try:
    bedrijven = bedrijven.drop(['verschil', 'Xwaarde_float', 'Ywaarde_float'], axis=1)
    print(bedrijven) 
except KeyError:
    print("")






