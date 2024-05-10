# Importeer python bibliotheken
import pandas as pd 
import numpy as np 
from tabulate import tabulate   
import matplotlib.pyplot as plt 
import seaborn as sns
from datetime import date, datetime
pd.set_option('display.max_columns', None)

# Importeer modules 
from Class_gassen import Gassen
from Class_lees_bedrijven import Bedrijven
from Class_inspecteurs import Inspecteurs
from Class_lees_rapporten import Rapporten

# Toewijzen datasets aan variabelen
gassen = Gassen.lees_gassen() # Inlezen werkt
bedrijven = Bedrijven.lees_bedrijven() # Inlezen werkt
inspecteurs = Inspecteurs.lees_inspecteurs() # Inlezen werkt
bedrijven = Bedrijven.lees_bedrijven() # Inlezen werkt
rapporten = Rapporten.lees_rapporten() # Inlezen werkt
# Keuzes voor het keuze menu

def keuze_menu():
    """een while loop om de keuzes steeds te laten terug keren"""
    while True: 
        keuze = input("\nHallo, maakt u een keuze uit het keuze menu\n"
                  "1: Tonen inspecteurs\n"
                  "2: Tonen  bedrijven\n"
                  "3: Tonen bezoekrapporten\n" 
                  "4: Plotten van meetgegevens\n"
                  "5: Bepalen en tonen boetes\n"
                  "6: Analyseren meetgegevens\n"
                  "7: Beheer bedrijfsgegevens, wijzigen gegevens\n"
                  "8: Beheer bedrijfsgegevens, toevoegen gegevens\n"
                  "9: Beheer bedrijfsgegevens, zoek locatie\n"
                  "10: Beheer bedrijfsgegevens, zoek naam\n"
                  "11: Beheer bezoekrapporten, wijzigen rapport gegevens\n"
                  "12: Beheer bezoekrapporten, toevoegen rapport gegevens\n"
                  "Stop\n")
        print(f"Uw keuze was {keuze}") 

        """Geldige keuze aanmaken en deze formateren naar een string, zodat deze vergeleken kunnen worden met gegeven antwoorden van gebruikers"""
        geldige_keuzes = [f"{i:01d}" for i in range(1,13)]

        if keuze not in geldige_keuzes and keuze != "Stop" and keuze != "stop": 
            print("U heeft een ongeldige keuze gemaakt. U wordt terug geleid naar het hoofdmenu")

        """Toon de resultaten en de acties die gelden voor de verschillende keuzes"""
        if keuze == "1":
            print(f"U heeft gekozen om de inspecteurs te tonen")  
            Inspecteurs.lees_inspecteurs()

        elif keuze == "2":
            print(f"U heeft gekozen om een overzicht te tonen van de bedrijven")
            Bedrijven.toon_bedrijven()
            
        elif keuze == "3": 
            print(f"U heeft gekozen om een overzicht te tonen van de rapporten")
            Rapporten.toon_rapporten()
        
        elif keuze == "4": 
            print(f"U heeft gekozen om de gassen gegevens te plotten")
            Gassen_plot.plot_gassen()
        
        elif keuze == "5":
            print("U heeft gekozen om een overzicht van de boetes te genereren")
        
        elif keuze == "6":
            print(f"U heeft gekozen om de meetgegevens te analyseren")
            Bedrijven.analyse()
        
        elif keuze == "7": 
            print("U heeft gekozen om de bedrijfsgegevens te beheren")
            Bedrijven.bedrijf_wijzigen()
            bedrijven = Bedrijven.bedrijf_wijzigen()
        
        elif keuze == "8":
            print("U heeft gekozen om bedrijfsgegevens toe te voegen")
            Bedrijven.bedrijf_toevoegen() 
            bedrijven = Bedrijven.bedrijf_toevoegen() 
        
        elif keuze == "9": 
            print("U wilt een bedrijf zoeken op basis van coördinaten")
            Bedrijven.zoek_bedrijven_locatie()
        
        elif keuze == "10":
            print("U wilt een bedrijf zoeken op basis van een naam")
            Bedrijven.zoek_bedrijven_naam()
        
        elif keuze == "11":
            print("U wilt een rapport wijzigen")
            Rapporten.rapport_wijziging()
            rapporten =  Rapporten.rapport_wijziging()
        
        elif keuze == "12":
            print("U wilt een rapport toevoegen")
            Rapporten.rapport_toevoegen()
            rapporten = Rapporten.rapport_toevoegen()
           
        """Stop het programma als de gebruiker Stop of stop invoert"""
        if keuze == "Stop" or keuze == "stop": 
            """Automatisch opslaan van bestanden"""
            print("Het programma wordt gesloten en de data wordt opgeslagen")
            
            path = r'update_bedrijven.txt'
            #export DataFrame to text file
            bedrijven.to_csv('bedrijven_update.txt', sep=' ', index=False, header=False)
            rapporten.to_cvs('rapporten_update.txt', sep=' ', index=False)
            break

keuze_menu()        

