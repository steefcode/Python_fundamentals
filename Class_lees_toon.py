# class Person:

# Import required packages    
import pandas as pd  

class Bestanden: 
  
  def lees_inspecteurs(): 
    """Inlezen van bestand met pandas en kolom namen weergeven"""
    inspecteurs = pd.read_fwf("inspecteurs.txt", header = None) 
    inspecteurs.columns = ["ID_inspecteur_naam", "Plaats", "Naam"]
                
    """Substring van de ID_inspecteur_naam om de id en de naam te kunnen scheiden"""
    inspecteurs["ID_inspecteur"] = inspecteurs["ID_inspecteur_naam"].str[:3] 
    inspecteurs["Naam"] = inspecteurs["ID_inspecteur_naam"].str[3:]
                
    """Herschikken van kolommen zodat de volgorde logischer is""" 
    inspecteurs = inspecteurs[["ID_inspecteur", "Naam", "Plaats"]]
  
  def toon_bestanden():    
    """Inlezen van bestand met pandas en kolom namen weergeven"""
    inspecteurs = pd.read_fwf("inspecteurs.txt", header = None) 
    inspecteurs.columns = ["ID_inspecteur_naam", "Plaats", "Naam"]
                
    """Substring van de ID_inspecteur_naam om de id en de naam te kunnen scheiden"""
    inspecteurs["ID_inspecteur"] = inspecteurs["ID_inspecteur_naam"].str[:3] 
    inspecteurs["Naam"] = inspecteurs["ID_inspecteur_naam"].str[3:] 
                
    """Herschikken van kolommen zodat de volgorde logischer is""" 
    inspecteurs = inspecteurs[["ID_inspecteur", "Naam", "Plaats"]]
    print(inspecteurs)

inspecteurs = Bestanden.toon_bestanden()

inspecteurs = Bestanden.lees_inspecteurs() 





