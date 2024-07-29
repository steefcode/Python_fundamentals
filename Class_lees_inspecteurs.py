import pandas as pd 
# import numpy as np 
from tabulate import tabulate

class InspecteursDataReader: 
  def __init__(self):
    self.inspecteurs = "inspecteurs.txt"

  def lees_inspecteurs(self): 
    """Inlezen van bestand met pandas en kolom namen weergeven"""
    inspecteurs = pd.read_fwf(self.inspecteurs, header=None) 
    inspecteurs.columns = ["ID_inspecteur_naam", "Plaats", "Naam"]
                
    """Substring van de ID_inspecteur_naam om de id en de naam te kunnen scheiden"""
    inspecteurs["ID_inspecteur"] = inspecteurs["ID_inspecteur_naam"].str[:3] 
    inspecteurs["Naam"] = inspecteurs["ID_inspecteur_naam"].str[3:]
                
    """Herschikken van kolommen zodat de volgorde logischer is""" 
    inspecteurs = inspecteurs[["ID_inspecteur", "Naam", "Plaats"]]

    return inspecteurs  


