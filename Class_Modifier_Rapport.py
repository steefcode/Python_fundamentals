import pandas as pd
import numpy as np

class Modifier_Rapport:
    def __init__(self, dataframe):
        self.rapporten = dataframe

    def wijzigen_rapport(self, rij_index, kolom_naam, waarde):
        if self.rapporten.loc[rij_index, 'Status']  == 'd':
            print("Waarde kan niet worden aangepast omdat de status van deze rij op d/definitief staat. De wijziging is niet uitgevoerd")
        else:
            self.rapporten[kolom_naam] = np.where(self.rapporten.index == rij_index, waarde, self.rapporten[kolom_naam])
        return self.rapporten



