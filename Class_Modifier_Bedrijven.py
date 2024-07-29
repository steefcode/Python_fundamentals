import pandas as pd
import numpy as np

class Modifier_Bedrijven:
    def __init__(self, dataframe):
        self.bedrijven = dataframe

    def wijzigen_bedrijf(self, rij_index, kolom_naam, waarde):
        if self.bedrijven.loc[rij_index, kolom_naam] == 'j':
            print("Deze waarde mag niet worden gewijzigd omdat er al een controle is geweest.")
        elif kolom_naam == "Code":
            print("Van een bestaand bedrijf mag de code niet worden aangepast. De wijziging is niet uitgevoerd")
        elif kolom_naam == "Straat":
            print("De locatie van een bedrijf mag niet worden gewijzigd. De wijziging is niet uitgevoerd")
        else:
            self.bedrijven[kolom_naam] = np.where(self.bedrijven.index == rij_index, waarde, self.bedrijven[kolom_naam])
        return self.bedrijven


