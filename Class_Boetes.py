import pandas as pd
import numpy as np

class Boetes:
    def __init__(self, bedrijven, gassen):
        self.bedrijven = bedrijven.copy(deep=True)
        self.bedrijven_gassen = gassen.copy(deep=True)

    def calculate_boete(self):
        # Toevoegen van een nieuwe kolom omgevingsuitstoot 
        self.bedrijven_gassen["omgevingsuitstoot"] = 0

        for index, bedrijf in self.bedrijven.iterrows():
            x = bedrijf["Xwaarde"]
            y = bedrijf["Ywaarde"]

            # Bereken de omgevingsuitstoot op basis van x en y coordinaten range  
            self.bedrijven_gassen["omgevingsuitstoot"] = np.where(
                (self.bedrijven_gassen["x-waarde"].isin(range(x - 2, x + 3))) &
                (self.bedrijven_gassen["y-waarde"].isin(range(y - 2, y + 3))),
                self.bedrijven_gassen["tot_uitstoot"] * 0.25,
                self.bedrijven_gassen["omgevingsuitstoot"]
            )

            self.bedrijven_gassen["omgevingsuitstoot"] = np.where(
                (self.bedrijven_gassen["x-waarde"].isin(range(x - 1, x + 2))) &
                (self.bedrijven_gassen["y-waarde"].isin(range(y - 1, y + 2))),
                self.bedrijven_gassen["tot_uitstoot"] * 0.5,
                self.bedrijven_gassen["omgevingsuitstoot"]
            )

            self.bedrijven_gassen["omgevingsuitstoot"] = np.where(
                (self.bedrijven_gassen["x-waarde"] == x) & (self.bedrijven_gassen["y-waarde"] == y),
                self.bedrijven_gassen["tot_uitstoot"],
                self.bedrijven_gassen["omgevingsuitstoot"]
            )

        # Merge de bestanden samen op basis van x en y coordinaten om zo de omgevingsuitstoot per bedrijf te krijgen. 
        boete = pd.merge(
            self.bedrijven,
            self.bedrijven_gassen,
            left_on=['Xwaarde', 'Ywaarde'],
            right_on=['x-waarde', 'y-waarde'],
            how='left',
            indicator=True
        )
        boete = boete.drop(['x-waarde', 'y-waarde', 'CO2', 'CH4', 'NO2', 'NH3', '_merge'], axis=1)

        # Bereken de Beruitst op basis van omgevingsuitstoot gemiddelde 
        boete['Beruitst'] = boete['tot_uitstoot'] + (boete['omgevingsuitstoot'] / 25)
        boete['Berekening_boete'] = boete["Maxuitst"] - boete['Beruitst']

        # Bereken de boete als de maximale boete overschreven is, per eenheide maal 1000
        boete["Boete"] = np.where(boete['Berekening_boete'] < 0, boete["Berekening_boete"] * -1000, boete["Boete"])
        boete = boete.drop(["Berekening_boete"], axis=1)

        return boete

# Example usage:
# bedrijven_gassen_calculator = Boetes(bedrijven, gassen)
# result_boete = bedrijven_gassen_calculator.calculate_boete()
# print(result_boete)