import pandas as pd 
import numpy as np 
from tabulate import tabulate   
import matplotlib.pyplot as plt 
import seaborn as sns

class Gassen: 
    def __init__(self, naam):
        self.naam = naam
        self.dataset = None
    
    '''Inladen als Numpy array'''
    def inladen_gassen(self):
        
        '''Een check of de dataset wel in gebruik is genomen'''
        self.dataset = np.loadtxt(self.naam, delimiter= ",", skiprows=1)

        '''Vervolgens de Numpy array aanpassen naar een Pandas Dataframe'''
        self.dataset = pd.DataFrame(self.dataset, 
                      columns=["x-waarde",
                               "y-waarde", 
                               "CO2", 
                               "CH4", 
                               "NO2", 
                               "NH3"]) 
        
        '''Type van de x en y coordinaten omzetten naat integer, zodat deze later kan worden gemerged met bedrijven bestand'''
        self.dataset["x-waarde"] = self.dataset["x-waarde"].astype(int)
        self.dataset["y-waarde"] = self.dataset["y-waarde"].astype(int)

        # '''Maak variabelen aan zodat deze in de range functie kunnen worden gebruikt om de gemiddelde uitstoot en boetes te bepalen'''
        # x_waarde = self.dataset["x-waarde"]
        # y_waarde = self.dataset["y-waarde"]

        '''Aanmaken van totale uitstoot'''
        self.dataset["tot_uitstoot"] = (1 * self.dataset["CO2"]) + (25 * self.dataset["CH4"]) + (5 * self.dataset["NO2"]) + (1000 * self.dataset["NH3"])
