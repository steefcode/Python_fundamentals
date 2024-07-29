import pandas as pd

class Subsetcoordinaten_update:
    def __init__(self, data_frame):
        self.df = data_frame
        self.df['Xwaarde_float'] = self.df['Xwaarde'].astype(float)
        self.df['Ywaarde_float'] = self.df['Ywaarde'].astype(float)
    
    def verschil_coordinaten_update(self, input_x, input_y):
        self.df['verschil'] = ((self.df['Xwaarde_float'] - input_x) ** 2 + (self.df['Ywaarde_float'] - input_y) ** 2) ** 0.5
        smallest_difference_row = self.df.loc[self.df['verschil'].idxmin()]
        smallest_difference_row = smallest_difference_row.drop(["Xwaarde_float","Ywaarde_float"])
        self.df.drop(['verschil', 'Xwaarde_float', 'Ywaarde_float'], axis = 1, inplace = True)
        return smallest_difference_row

