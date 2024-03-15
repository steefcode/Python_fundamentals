import pandas as pd
import numpy as np

class Gassen:
    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam

    def lees_gassen(self):
        gassen = np.loadtxt(self.bestandsnaam, delimiter= ",", skiprows=1)
        
        gassen = pd.DataFrame(gassen, 
                      columns=["x-waarde",
                               "y-waarde", 
                               "CO2", 
                               "CH4", 
                               "NO2", 
                               "NH3"])
        
        '''leading zero toevoegen aan x en y coordinaten zodat deze kunnen mergen met bedrijven'''
        gassen["x-waarde"] = gassen["x-waarde"].astype(int)
        gassen["y-waarde"] = gassen["y-waarde"].astype(int)

        '''Aanmaken van totale uitstoot'''
        gassen["tot_uitstoot"] = (1 * gassen["CO2"]) + (25 * gassen["CH4"]) + (5 * gassen["NO2"]) + (1000 * gassen["NH3"])
        return gassen

# Usage
# gassen_instance = Gassen("gassen.csv")
# data = gassen_instance.lees_gassen()
# print(data) 
# 