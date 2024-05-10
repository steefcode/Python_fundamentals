# Importeren van benodigde bibliotheken  
import pandas as pd 
import numpy as np 
from tabulate import tabulate   
import matplotlib.pyplot as plt 
import seaborn as sns

class Gassen: 

    def lees_gassen():
        gassen = np.loadtxt("gassen.csv", delimiter= ",", skiprows=1)
        
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




