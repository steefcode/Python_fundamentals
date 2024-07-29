import pandas as pd
import numpy as np
import uuid

class Boetes:
    def __init__(self, bedrijven, gassen):
        self.bedrijven = bedrijven.copy(deep=True)
        self.bedrijven_gassen = gassen.copy(deep=True)

    def calculate_boete(self):
        # Toevoegen nieuwe kolom omgeveingsuitstoot
        self.bedrijven_gassen["omgevingsuitstoot"] = 0.0

        for index, bedrijf in self.bedrijven.iterrows():
            x = bedrijf["Xwaarde"]
            y = bedrijf["Ywaarde"]

            # Omgevingsuitstoot berekeninen op basis van x-y coordinaten combinaties
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

        # Aanmaken van UUID's om te kunnen aggregeren op basis van omgevingsuitstoot. Zo kan een gemiddelde per groep worden berekend
        self.bedrijven_gassen["UUID"] = ""

        for index, bedrijf in self.bedrijven.iterrows():
            x = bedrijf["Xwaarde"]
            y = bedrijf["Ywaarde"]

            uuid_value = str(uuid.uuid4())
            mask = (self.bedrijven_gassen["x-waarde"].between(x - 2, x + 2)) & \
                   (self.bedrijven_gassen["y-waarde"].between(y - 2, y + 2))
    
            self.bedrijven_gassen.loc[mask, "UUID"] = uuid_value

        # Uitreken van gemiddelde uitstoot per groep
        uitstoot_per_uuid = self.bedrijven_gassen.groupby("UUID")["omgevingsuitstoot"].mean()

        bedrijven_omgevingsuitstoot = pd.merge(self.bedrijven_gassen, 
                                               uitstoot_per_uuid, 
                                               left_on="UUID",
                                               right_on="UUID",
                                               how='left', 
                                               suffixes=('_x', '_y'))

        bedrijven_omgevingsuitstoot = bedrijven_omgevingsuitstoot.drop(['CO2', 'CH4', 'NO2', 'NH3', 'UUID', 'omgevingsuitstoot_x'], axis=1)
        bedrijven_omgevingsuitstoot = bedrijven_omgevingsuitstoot.rename(columns={'omgevingsuitstoot_y': 'omgevingsuitstoot'})
        
        #  Samen voegen van gassenbestand en bedrijven bestand met als key x en y coordinaten. 
        boete = pd.merge(
            self.bedrijven,
            bedrijven_omgevingsuitstoot,
            left_on=['Xwaarde', 'Ywaarde'],
            right_on=['x-waarde', 'y-waarde'],
            how='left'
        )

        boete = boete.drop(['x-waarde', 'y-waarde'], axis=1)

        # Bereken de Beruitst basis van de gemiddelde omgevingsuitstoot  
        boete['Beruitst'] = boete['omgevingsuitstoot']
        boete['Berekening_eenheden'] = (boete["Maxuitst"] - boete['Beruitst']) * 1000

        # Bereken de boete als de maximale omgevingsuitstoot is overschreden.  
        boete["Boete"] = np.where(boete['Berekening_eenheden'] < 0, boete["Berekening_eenheden"] * -1000, boete["Berekening_eenheden"])
        boete = boete.drop(['tot_uitstoot', 'omgevingsuitstoot', 'Berekening_eenheden'], axis=1)
        
        return boete
