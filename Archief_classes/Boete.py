import pandas as pd
import numpy as np

bedrijven_gassen = gassen.copy(deep=True) 
bedrijven_gassen["omgevingsuitstoot"] = 0


for index, bedrijf in bedrijven.iterrows():
    x = bedrijf["Xwaarde"]
    y = bedrijf["Ywaarde"]

    '''Indien de omgeving in een range van 2 ligt ten opzichte van de x en y coordinaten tot_uitstoot * 0.25'''
    bedrijven_gassen["omgevingsuitstoot"] = np.where((bedrijven_gassen["x-waarde"].isin(range(x -2, x + 3))) &
                                        (bedrijven_gassen["y-waarde"].isin(range(y -2, y + 3))), 
                                        bedrijven_gassen["tot_uitstoot"] * 0.25, bedrijven_gassen["omgevingsuitstoot"])
    '''Indien de omgeving in een range van 2 ligt ten opzichte van de x en y coordinaten tot_uitstoot * 0.5'''
    bedrijven_gassen["omgevingsuitstoot"] = np.where((bedrijven_gassen["x-waarde"].isin(range(x -1, x + 2))) &
                                        (bedrijven_gassen["y-waarde"].isin(range(y -1, y + 2))), 
                                        bedrijven_gassen["tot_uitstoot"] * 0.5, bedrijven_gassen["omgevingsuitstoot"])
    '''Indien de omgeving in een range van 2 ligt ten opzichte van de x en y coordinaten tot_uitstoot * 1'''
    bedrijven_gassen["omgevingsuitstoot"] = np.where((bedrijven_gassen["x-waarde"] == x) & (bedrijven_gassen["y-waarde"] == y), 
                                               bedrijven_gassen["tot_uitstoot"], bedrijven_gassen["omgevingsuitstoot"])
    

'''Het mergen van het gassen bestand met de tot_berekening en de omgevingsuitstoot'''
'''Zo kan er een verschil berekend worden tussen de Maxuitstoot en de tot_uitstoot en de omgevingsuitstoot'''
boete = pd.merge(bedrijven, bedrijven_gassen, left_on=['Xwaarde','Ywaarde'], right_on=['x-waarde','y-waarde'], how='left', indicator=True)
boete = boete.drop(['x-waarde', 'y-waarde', 'CO2', 'CH4', 'NO2', 'NH3', '_merge'], axis=1)
'''De omgevingsuitstoot is een gemiddelde, vandaar gedeeld door 25'''
boete['Beruitst'] = boete['tot_uitstoot'] + (boete['omgevingsuitstoot']/25) 
boete['Berekening_boete'] = boete["Maxuitst"] -  boete['Beruitst']  

'''Als de waarde negatief is dan iedere eenheid die agwijkt van de Maxuist maal 1000'''
boete["Boete"] = np.where(boete['Berekening_boete'] < 0, boete["Berekening_boete"] * -1000, boete["Boete"]) 
boete = boete.drop(["Berekening_boete"], axis = 1)


















































