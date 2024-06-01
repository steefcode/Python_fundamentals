# import pandas as pd
# import numpy as np
# import uuid

# class Boetes:
#     def __init__(self, bedrijven, gassen):
#         self.bedrijven = bedrijven.copy(deep=True)
#         self.bedrijven_gassen = gassen.copy(deep=True)

#     def calculate_boete(self):
#         # Toevoegen van een nieuwe kolom omgevingsuitstoot 
#         self.bedrijven_gassen["omgevingsuitstoot"] = 0

#         for index, bedrijf in self.bedrijven.iterrows():
#             x = bedrijf["Xwaarde"]
#             y = bedrijf["Ywaarde"]

#             # Bereken de omgevingsuitstoot op basis van x en y coordinaten range  
#             self.bedrijven_gassen["omgevingsuitstoot"] = np.where(
#                 (self.bedrijven_gassen["x-waarde"].isin(range(x - 2, x + 3))) &
#                 (self.bedrijven_gassen["y-waarde"].isin(range(y - 2, y + 3))),
#                 self.bedrijven_gassen["tot_uitstoot"] * 0.25,
#                 self.bedrijven_gassen["omgevingsuitstoot"]
#             )

#             self.bedrijven_gassen["omgevingsuitstoot"] = np.where(
#                 (self.bedrijven_gassen["x-waarde"].isin(range(x - 1, x + 2))) &
#                 (self.bedrijven_gassen["y-waarde"].isin(range(y - 1, y + 2))),
#                 self.bedrijven_gassen["tot_uitstoot"] * 0.5,
#                 self.bedrijven_gassen["omgevingsuitstoot"]
#             )

#             self.bedrijven_gassen["omgevingsuitstoot"] = np.where(
#                 (self.bedrijven_gassen["x-waarde"] == x) & (self.bedrijven_gassen["y-waarde"] == y),
#                 self.bedrijven_gassen["tot_uitstoot"],
#                 self.bedrijven_gassen["omgevingsuitstoot"]
#             )

#         # Aanmaken van groepen die horen bij de omgevingsuitstoot van de bedrijven. 
#         self.bedrijven_gassen["UUID"] = ""

#         for index, bedrijf in self.bedrijven.iterrows():
#             x = bedrijf["Xwaarde"]
#             y = bedrijf["Ywaarde"]

#         # Aanmaken van unieke identiefier per groep om zo te aggregeren naar gemiddelde omgevingsuitstoot.   
#             uuid_value = str(uuid.uuid4())
#             mask = (self.bedrijven_gassen["x-waarde"].between(x - 2, x + 2)) & \
#                         (self.bedrijven_gassen["y-waarde"].between(y - 2, y + 2))
    
#             self.bedrijven_gassen.loc[mask, "UUID"] = uuid_value

#         # Gemiddelde omgevingsuitstoot per UUID om een gewogen gemiddelde te berekenen. 
#         uitstoot_per_uuid = self.bedrijven_gassen.groupby("UUID")["omgevingsuitstoot"].mean()

#         bedrijven_omgevingsuitstoot = pd.merge(self.bedrijven_gassen, 
#                                                uitstoot_per_uuid, 
#                                                left_on=["UUID"],
#                                                right_on = ["UUID"],
#                                                how = 'left', 
#                                                indicator=True) 
        
#         bedrijven_omgevingsuitstoot = bedrijven_omgevingsuitstoot.drop(['CO2', 'CH4', 'NO2', 'NH3','UUID',  
#                                                                         'omgevingsuitstoot_x', '_merge'], axis=1)
#         bedrijven_omgevingsuitstoot = bedrijven_omgevingsuitstoot.rename(columns={'omgevingsuitstoot_y': 'omgevingsuitstoot'})
#         # print(bedrijven_omgevingsuitstoot)
        
#         # Test met print
#         #print(self.bedrijven_gassen.head(100))
#         #print(self.bedrijven_gassen.loc[self.bedrijven_gassen['x-waarde'] == 2])
#         #print(self.bedrijven_gassen.loc[self.bedrijven_gassen['y-waarde'] == 2])
#         # test_df = self.bedrijven_gassen.loc[self.bedrijven_gassen['omgevingsuitstoot'] > 0.0] 
#         # print(test_df)
         
#         # Merge de bestanden samen op basis van x en y coordinaten om zo de omgevingsuitstoot per bedrijf te krijgen. 
#         boete = pd.merge(
#             self.bedrijven,
#             bedrijven_omgevingsuitstoot,
#             left_on=['Xwaarde', 'Ywaarde'],
#             right_on=['x-waarde', 'y-waarde'],
#             how='left',
#             indicator=True
#         )
#         boete = boete.drop(['x-waarde', 'y-waarde','_merge'], axis=1)
#         # Test met print
#         # print(boete)'
       
#         # Bereken de Beruitst op basis van omgevingsuitstoot gemiddelde  
#         boete['Beruitst'] = boete['omgevingsuitstoot']
#         boete['Berekening_eenheden'] = (boete["Maxuitst"] - boete['Beruitst']) * 1000

#         # Bereken de boete als de maximale boete overschreven is, per eenheide maal 1000
#         boete["Boete"] = np.where(boete['Berekening_eenheden'] < 0, boete["Berekening_eenheden"] * -1000, boete["Berekening_eenheden"])
#         boete = boete.drop(['tot_uitstoot', 'omgevingsuitstoot', 'Berekening_eenheden'], axis=1) 
#         print(type(boete))

#         x = boete
#         print(type(x))
        
#         return boete

import pandas as pd
import numpy as np
import uuid

class Boetes:
    def __init__(self, bedrijven, gassen):
        self.bedrijven = bedrijven.copy(deep=True)
        self.bedrijven_gassen = gassen.copy(deep=True)

    def calculate_boete(self):
        # Adding a new column for environmental emissions
        self.bedrijven_gassen["omgevingsuitstoot"] = 0.0

        for index, bedrijf in self.bedrijven.iterrows():
            x = bedrijf["Xwaarde"]
            y = bedrijf["Ywaarde"]

            # Calculate environmental emissions based on x and y coordinate range
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

        # Create UUIDs for groups to aggregate average environmental emissions
        self.bedrijven_gassen["UUID"] = ""

        for index, bedrijf in self.bedrijven.iterrows():
            x = bedrijf["Xwaarde"]
            y = bedrijf["Ywaarde"]

            uuid_value = str(uuid.uuid4())
            mask = (self.bedrijven_gassen["x-waarde"].between(x - 2, x + 2)) & \
                   (self.bedrijven_gassen["y-waarde"].between(y - 2, y + 2))
    
            self.bedrijven_gassen.loc[mask, "UUID"] = uuid_value

        # Calculate average environmental emissions per UUID
        uitstoot_per_uuid = self.bedrijven_gassen.groupby("UUID")["omgevingsuitstoot"].mean()

        bedrijven_omgevingsuitstoot = pd.merge(self.bedrijven_gassen, 
                                               uitstoot_per_uuid, 
                                               left_on="UUID",
                                               right_on="UUID",
                                               how='left', 
                                               suffixes=('_x', '_y'))

        bedrijven_omgevingsuitstoot = bedrijven_omgevingsuitstoot.drop(['CO2', 'CH4', 'NO2', 'NH3', 'UUID', 'omgevingsuitstoot_x'], axis=1)
        bedrijven_omgevingsuitstoot = bedrijven_omgevingsuitstoot.rename(columns={'omgevingsuitstoot_y': 'omgevingsuitstoot'})
        
        # Merge the dataframes based on x and y coordinates to get environmental emissions per company
        boete = pd.merge(
            self.bedrijven,
            bedrijven_omgevingsuitstoot,
            left_on=['Xwaarde', 'Ywaarde'],
            right_on=['x-waarde', 'y-waarde'],
            how='left'
        )

        boete = boete.drop(['x-waarde', 'y-waarde'], axis=1)

        # Calculate Beruitst based on average environmental emissions  
        boete['Beruitst'] = boete['omgevingsuitstoot']
        boete['Berekening_eenheden'] = (boete["Maxuitst"] - boete['Beruitst']) * 1000

        # Calculate the fine if the maximum emission is exceeded
        boete["Boete"] = np.where(boete['Berekening_eenheden'] < 0, boete["Berekening_eenheden"] * -1000, boete["Berekening_eenheden"])
        boete = boete.drop(['tot_uitstoot', 'omgevingsuitstoot', 'Berekening_eenheden'], axis=1)
        
        return boete
