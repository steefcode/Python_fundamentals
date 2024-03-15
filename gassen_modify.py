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
        if self.dataset is None:
            raise ValueError("De dataset van gassen is niet ingeladen. Zorg ervoor dat deze eerst ingeladen is")
    
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
        # self.dataset["x-waarde"] = self.dataset["x-waarde"].astype(int)
        # self.dataset["y-waarde"] = self.dataset["y-waarde"].astype(int)

        '''Maak variabelen aan zodat deze in de range functie kunnen worden gebruikt om de gemiddelde uitstoot en boetes te bepalen'''
        #x_waarde = self.dataset["x-waarde"]
        #y_waarde = self.dataset["y-waarde"]

        '''Aanmaken van totale uitstoot'''
        self.dataset["tot_uitstoot"] = (1 * self.dataset["CO2"]) + (25 * self.dataset["CH4"]) + (5 * self.dataset["NO2"]) + (1000 * self.dataset["NH3"])

        '''Maak een loop om zo een berekening te kunnen maken voor de uitstoot met verschillende afstanden tot de coordinaten'''
        # for index, bedrijf in bedrijven.iterrows():
        # self.dataset["berek_uitstoot"] = np.where((self.dataset["x-waarde"].isin(range(x_waarde -2, x_waarde + 3))) &
        #                                 (self.dataset["y-waarde"].isin(range(y_waarde, y_waarde + 3))), 
        #                                 self.dataset["tot_uitstoot"] * 0.25, 0) 
        # return self.dataset
    
analyser = Gassen('gassen.csv')  
gassen = analyser.inladen_gassen()  
print(gassen)


gassen_test = gassen.copy(deep=True)
print(gassen_test)








gassen_test["x-waarde"] = gassen_test["x-waarde"].astype(int)
gassen_test["y-waarde"] = gassen_test["y-waarde"].astype(int)

x_waarde = gassen_test["x-waarde"]
y_waarde = gassen_test["y-waarde"]

gassen_test['berek'] = np.where((gassen_test["x_waarde"].isin(range(x_waarde - 2, x_waarde + 3))) &
                                (gassen_test["y_waarde"].isin(range(y_waarde - 2, y_waarde + 3))), 
                                gassen_test["tot_uitstoot"] * 0.25, 0) 


# gassen_test['berek'] = np.where((gassen_test["x-waarde"].isin(range(gassen_test["x-waarde"] -2, gassen_test["x-waarde"] + 3))) &
#                                (gassen_test["y-waarde"].isin(range(gassen_test["y-waarde"] -2, gassen_test["y-waarde"] + 3))), 
#                                gassen_test["tot_uitstoot"] * 0.25, 0)


