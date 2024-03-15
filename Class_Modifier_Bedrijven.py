import pandas as pd

class Modifier_Bedrijven:
    def __init__(self, dataframe):
        self.bedrijven = dataframe

    def wijzigen_bedrijf(self, rij_index, kolom_index, waarde):
        try:
            if self.bedrijven.loc[rij_index, kolom_index] == 'j':
                print("Deze waarde mag niet worden gewijzigd omdat er al een controle is geweest.")
            elif kolom_index == "Code":
                print("Van een bestaand bedrijf mag de code niet worden aangepast.")
            elif kolom_index == "Straat":
                print("De locatie van een bedrijf mag niet worden gewijzigd.")
            else:
                self.bedrijven.loc[rij_index, kolom_index] = waarde
        except KeyError:
            print("De opgegeven kolom komt niet voor in de keuze.")

