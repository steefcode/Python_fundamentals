# Importeren van benodigde bibliotheken  
import pandas as pd 
import numpy as np 
from tabulate import tabulate
from datetime import date, datetime
from Class_inspecteurs import Inspecteurs

inspecteurs = Inspecteurs.lees_inspecteurs()
Inspecteurs.toon_inspecteurs()

class Rapporten: 
    
    def lees_rapporten():
        """Colspecs definieren voor het inlezen bestanden"""
        colspecs = [(0,3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]

        """Inlezen van rapporten"""
        rapporten = pd.read_fwf("rapporten.txt", header = None, colspecs = colspecs, 
                            names = ["Icode", 
                                     "Bcode", 
                                     "Bezdat", 
                                     "Rapdat", 
                                     "Status", 
                                     "Opm"], 
                            dtype = {"Icode" : str, 
                                    "Bcode" : str, 
                                    "Bezdat" : str, 
                                    "Rapdat" : str, 
                                    "Status" : str,
                                    "Opm" : str}, 
                            parse_dates = ["Bezdat", "Rapdat"])
        return rapporten 
    
    def toon_rapporten(): 
        print(rapporten) 

    def overzicht_rapporten_inspecteur():
        rapport_inspecteur = input("Van welke inspecteur wilt u de rapporten zien? ")
        while rapport_inspecteur not in rapporten["Icode"].unique(): 
            print(f"De door u opgegeven code is niet beschikbaar, deze inspecteurs komen voor {rapporten['Icode'].unique()}")
            rapport_inspecteur = input("Van welke inspecteur wilt u de rapporten zien? ")
        else: 
            selectie_inspecteur_rapport = rapporten.loc[rapporten["Icode"] == rapport_inspecteur]
            print(selectie_inspecteur_rapport)
            selectie_inspecteur = inspecteurs.loc[inspecteurs["ID_inspecteur"] == rapport_inspecteur]
            print("Het rapport is gemaakt door: ")
            print(selectie_inspecteur[["ID_inspecteur", "Naam"]])
    
    def overzicht_rapporten_bedrijf(): 
        rapport_bedrijf = input("Van welk bedrijf wilt u de rapporten zien? ")
        while rapport_bedrijf not in rapporten["Bcode"].unique(): 
            print(f"De door u opgegeven code is niet beschikbaar, deze bedrijven komen voor {rapporten['Bcode'].unique()}")
            rapport_bedrijf = input("Van welk bedrijf wilt u de rapporten zien? ")
        else: 
            selectie_bedrijf_rapport = rapporten.loc[rapporten["Bcode"] == rapport_bedrijf]
            print(selectie_bedrijf_rapport)

    def rapport_wijziging():
        opties_wijzigingen_rapporten = rapporten.columns[2:6]
        print(opties_wijzigingen_rapporten) 
        onderdeel_wijziging_rapport = input("Welke inhoud wilt u wijzigen van de hierboven genoemde kolommen? ") 
        waarde_wijziging_rapport = input(f"Voer de waarde in die u wilt toepassen voor ")
        
        print(rapporten["Bcode"])
        rapport_wijziging_bcode = input(f"Voor welk bedrijf wilt u de wijziging doorvoeren? ")
        print(rapporten["Icode"])
        rapport_wijziging_icode = input(f"Voor welke inspecteur wilt u de wijziging doorvoeren? ")
        print(rapporten["Bezdat"])
        rapport_wijziging_bezdat = (input(f"Voor welke bezoekdatum wilt u de wijziging doorvoeren in format jjjj-mm-dd? "))
        rapport_wijziging_bezdat = datetime.strptime(rapport_wijziging_bezdat, '%Y-%m-%d').date() 
        rapport_wijziging_bezdat =  rapport_wijziging_bezdat.date()
        rapport_wijziging = str(rapport_wijziging_icode) + str(rapport_wijziging_bcode) + str(rapport_wijziging_bezdat) 
        # rapport_wijziging

        rapporten_test = rapporten.copy(deep=True) 
        rapporten_split = rapporten_test["Status"] != "d"
        
        rapporten_definitief = rapporten_test[-rapporten_split]
        rapporten_definitief = rapporten_definitief.reset_index(drop=True)
        print(rapporten_definitief)
        
        rapporten_voorlopig = rapporten_test[rapporten_split]
        rapporten_voorlopig = rapporten_voorlopig.reset_index(drop=True)
        rapporten_voorlopig["key"] = rapporten_voorlopig["Icode"].astype(str) + rapporten_voorlopig["Bcode"].astype(str) + rapporten_voorlopig["Bezdat"].astype(str)
        print(rapporten_voorlopig)
        
        rapporten_voorlopig[onderdeel_wijziging_rapport] = np.where(rapporten_voorlopig["key"] == rapport_wijziging , 
                                                             waarde_wijziging_rapport, rapporten_voorlopig[onderdeel_wijziging_rapport]) 
        print(rapporten_voorlopig)  
        
        rapporten_voorlopig = rapporten_voorlopig.iloc[:, 0:6]
        print(rapporten_voorlopig)
        
        rapporten_test = pd.concat([rapporten_definitief, rapporten_voorlopig], ignore_index=True, sort=False)
        return rapporten_test
    
    def rapport_toevoegen():
        rapporten_leeg = rapporten.copy(deep=True)
        rapporten_leeg = rapporten_leeg.head(0)
        print(rapporten_leeg)
        print(rapporten_leeg.dtypes)  

        print(rapporten)

        toevoegen_icode = input("Voer een inspecteurscode in ")    
        while len(toevoegen_icode) != 3:
            print("De code die u opvoerde is te lang of te kort, maak een code aan met 4 letters")
            toevoegen_icode = input("Voer een bedrijfscode in ")           

        toevoegen_bcode = input("Voer een bedrijfscode in ")   
        while len(toevoegen_bcode) != 4:
            print("De code die u opvoerde is te lang of te kort, maak een code aan met 4 letters")
            toevoegen_bcode = input("Voer een bedrijfscode in ")  
                
        while True:
            try:
                print('open')    
                toevoegen_bezdat_dag = int(input("Voer de dag van het bezoek in "))
                break 
            except ValueError:
                print("Voer de dag van het bezoek in, geen letters ") 
                continue

        while True:
            try:
                print('open')    
                toevoegen_bezdat_maand = int(input("Voer de maand van het bezoek in "))
                break 
            except ValueError:
                print("Voer de maand van het bezoek in, geen letters ") 
                continue

        while True:
            try:
                print('open')    
                toevoegen_bezdat_jaar = int(input("Voer het jaar van het bezoek in "))
                break 
            except ValueError:
                print("Voer het jaar van het bezoek in, geen letters ") 
                continue

        toevoegen_bezdat = datetime(toevoegen_bezdat_jaar, toevoegen_bezdat_maand, toevoegen_bezdat_dag)

        while True:
            try:
                print('open')    
                toevoegen_rapdat_dag = int(input("Voer de dag van de rapportage in "))
                break 
            except ValueError:
                print("Voer de dag van de rapportage in, geen letters ") 
                continue

        while True:
            try:
                print('open')    
                toevoegen_rapdat_maand = int(input("Voer de maand van de rapportage in "))
                break 
            except ValueError:
                print("Voer de maand van de rapportage in, geen letters ") 
                continue

        while True:
            try:
                print('open')    
                toevoegen_rapdat_jaar = int(input("Voer het jaar van de rapportage in "))
                break 
            except ValueError:
                print("Voer het jaar van de rapportage in, geen letters ") 
                continue

        toevoegen_rapdat = datetime(toevoegen_rapdat_jaar, toevoegen_rapdat_maand, toevoegen_rapdat_dag)

        while toevoegen_rapdat < toevoegen_bezdat:
            print("Rapportage datum kan niet eerder hebben plaatsgevonden dan de bezoekdatum, vul een latere rapportage datum in")
            while True:
                try:
                    print('open')    
                    toevoegen_rapdat_dag = int(input("Voer de dag van het bezoek in "))
                    break 
                except ValueError:
                    print("Voer de dag van het bezoek in, geen letters ") 
                    continue

            while True:
                try:
                    print('open')    
                    toevoegen_rapdat_maand = int(input("Voer de maand van het bezoek in "))
                    break 
                except ValueError:
                    print("Voer de maand van het bezoek in, geen letters ") 
                    continue
            
            while True:
                try: 
                    print('open')    
                    toevoegen_rapdat_jaar = int(input("Voer het jaar van het bezoek in "))
                    break 
                except ValueError:
                    print("Voer het jaar van het bezoek in, geen letters ") 
                    continue
            toevoegen_rapdat = date(toevoegen_rapdat_jaar, toevoegen_rapdat_maand, toevoegen_rapdat_dag)

        toevoegen_status =  "v"       
        toevoegen_opm = input("Voer een opmerking in ")

        # Toevoegen van toegekende waardes in een leeg datframe met dezelfde opzet als dataframe rapporten
        rapporten_leeg.at[0, "Icode"] = toevoegen_icode
        rapporten_leeg.at[0, "Bcode"] = toevoegen_bcode
        rapporten_leeg.at[0, "Bezdat"] = toevoegen_bezdat
        rapporten_leeg.at[0, "Rapdat"] = toevoegen_rapdat
        rapporten_leeg.at[0, "Status"] = toevoegen_status
        rapporten_leeg.at[0, "Opm"] = toevoegen_opm

        print(rapporten_leeg)

        rapporten_test2= rapporten.copy(deep=True) 

        rapporten_test2 = pd.concat([rapporten, rapporten_leeg], ignore_index=True, sort=False)
        print(rapporten_test2)

rapporten = Rapporten.lees_rapporten()
Rapporten.toon_rapporten()

######################### Wijzigen van bestaand rapporten ######################### 

class Wijziging_Rapport: 
    def rapport_wijziging():
        opties_wijzigingen_rapporten = rapporten.columns[2:6]
        print(opties_wijzigingen_rapporten) 
        onderdeel_wijziging_rapport = input("Welke inhoud wilt u wijzigen van de hierboven genoemde kolommen? ") 
        waarde_wijziging_rapport = input(f"Voer de waarde in die u wilt toepassen voor ")
        
        print(rapporten["Bcode"])
        rapport_wijziging_bcode = input(f"Voor welk bedrijf wilt u de wijziging doorvoeren? ")
        print(rapporten["Icode"])
        rapport_wijziging_icode = input(f"Voor welke inspecteur wilt u de wijziging doorvoeren? ")
        print(rapporten["Bezdat"])
        rapport_wijziging_bezdat = (input(f"Voor welke bezoekdatum wilt u de wijziging doorvoeren in format jjjj-mm-dd? "))
        # rapport_wijziging_bezdat = date(rapport_wijziging_bezdat, '%Y-%m-%d')
        # rapport_wijziging_bezdat =  rapport_wijziging_bezdat.date()
        rapport_wijziging = str(rapport_wijziging_icode) + str(rapport_wijziging_bcode) + str(rapport_wijziging_bezdat)
        # rapport_wijziging

        rapporten_test = rapporten.copy(deep=True) 
        rapporten_split = rapporten_test["Status"] != "d"
        
        rapporten_definitief = rapporten_test[-rapporten_split]
        rapporten_definitief = rapporten_definitief.reset_index(drop=True)
        print(rapporten_definitief)
        
        rapporten_voorlopig = rapporten_test[rapporten_split]
        rapporten_voorlopig = rapporten_voorlopig.reset_index(drop=True)
        rapporten_voorlopig["key"] = rapporten_voorlopig["Icode"].astype(str) + rapporten_voorlopig["Bcode"].astype(str) + rapporten_voorlopig["Bezdat"].astype(str)
        print(rapporten_voorlopig)
        
        rapporten_voorlopig[onderdeel_wijziging_rapport] = np.where(rapporten_voorlopig["key"] == rapport_wijziging , 
                                                            waarde_wijziging_rapport, rapporten_voorlopig[onderdeel_wijziging_rapport]) 
        print(rapporten_voorlopig)  
        
        rapporten_voorlopig = rapporten_voorlopig.iloc[:, 0:6]
        print(rapporten_voorlopig)
        
        rapporten_test = pd.concat([rapporten_definitief, rapporten_voorlopig], ignore_index=True, sort=False)
        print(rapporten_test)
        print(rapporten)
        
        rapporten= rapporten_test.copy(deep=True) 

Wijziging_Rapport.rapport_wijziging()

# ######################### Toevoegen van bestaand rapporten ######################### 
# class Toevoegen_Rappport:
#     def rapport_toevoegen():
#         rapporten_leeg = rapporten.copy(deep=True)
#         rapporten_leeg = rapporten_leeg.head(0)
#         print(rapporten_leeg)
#         print(rapporten_leeg.dtypes)  

#         print(rapporten)

#         toevoegen_icode = input("Voer een inspecteurscode in ")    
#         while len(toevoegen_icode) != 3:
#             print("De code die u opvoerde is te lang of te kort, maak een code aan met 4 letters")
#             toevoegen_icode = input("Voer een bedrijfscode in ")           

#         toevoegen_bcode = input("Voer een bedrijfscode in ")   
#         while len(toevoegen_bcode) != 4:
#             print("De code die u opvoerde is te lang of te kort, maak een code aan met 4 letters")
#             toevoegen_bcode = input("Voer een bedrijfscode in ")  
                
#         while True:
#             try:
#                 print('open')    
#                 toevoegen_bezdat_dag = int(input("Voer de dag van het bezoek in "))
#                 break 
#             except ValueError:
#                 print("Voer de dag van het bezoek in, geen letters ") 
#                 continue

#         while True:
#             try:
#                 print('open')    
#                 toevoegen_bezdat_maand = int(input("Voer de maand van het bezoek in "))
#                 break 
#             except ValueError:
#                 print("Voer de maand van het bezoek in, geen letters ") 
#                 continue

#         while True:
#             try:
#                 print('open')    
#                 toevoegen_bezdat_jaar = int(input("Voer het jaar van het bezoek in "))
#                 break 
#             except ValueError:
#                 print("Voer het jaar van het bezoek in, geen letters ") 
#                 continue

#         toevoegen_bezdat = datetime(toevoegen_bezdat_jaar, toevoegen_bezdat_maand, toevoegen_bezdat_dag)

#         while True:
#             try:
#                 print('open')    
#                 toevoegen_rapdat_dag = int(input("Voer de dag van de rapportage in "))
#                 break 
#             except ValueError:
#                 print("Voer de dag van de rapportage in, geen letters ") 
#                 continue

#         while True:
#             try:
#                 print('open')    
#                 toevoegen_rapdat_maand = int(input("Voer de maand van de rapportage in "))
#                 break 
#             except ValueError:
#                 print("Voer de maand van de rapportage in, geen letters ") 
#                 continue

#         while True:
#             try:
#                 print('open')    
#                 toevoegen_rapdat_jaar = int(input("Voer het jaar van de rapportage in "))
#                 break 
#             except ValueError:
#                 print("Voer het jaar van de rapportage in, geen letters ") 
#                 continue

#         toevoegen_rapdat = datetime(toevoegen_rapdat_jaar, toevoegen_rapdat_maand, toevoegen_rapdat_dag)

#         while toevoegen_rapdat < toevoegen_bezdat:
#             print("Rapportage datum kan niet eerder hebben plaatsgevonden dan de bezoekdatum, vul een latere rapportage datum in")
#             while True:
#                 try:
#                     print('open')    
#                     toevoegen_rapdat_dag = int(input("Voer de dag van het bezoek in "))
#                     break 
#                 except ValueError:
#                     print("Voer de dag van het bezoek in, geen letters ") 
#                     continue

#             while True:
#                 try:
#                     print('open')    
#                     toevoegen_rapdat_maand = int(input("Voer de maand van het bezoek in "))
#                     break 
#                 except ValueError:
#                     print("Voer de maand van het bezoek in, geen letters ") 
#                     continue
            
#             while True:
#                 try: 
#                     print('open')    
#                     toevoegen_rapdat_jaar = int(input("Voer het jaar van het bezoek in "))
#                     break 
#                 except ValueError:
#                     print("Voer het jaar van het bezoek in, geen letters ") 
#                     continue
#             toevoegen_rapdat = date(toevoegen_rapdat_jaar, toevoegen_rapdat_maand, toevoegen_rapdat_dag)

#         toevoegen_status =  "v"       
#         toevoegen_opm = input("Voer een opmerking in ")

#         # Toevoegen van toegekende waardes in een leeg datframe met dezelfde opzet als dataframe rapporten
#         rapporten_leeg.at[0, "Icode"] = toevoegen_icode
#         rapporten_leeg.at[0, "Bcode"] = toevoegen_bcode
#         rapporten_leeg.at[0, "Bezdat"] = toevoegen_bezdat
#         rapporten_leeg.at[0, "Rapdat"] = toevoegen_rapdat
#         rapporten_leeg.at[0, "Status"] = toevoegen_status
#         rapporten_leeg.at[0, "Opm"] = toevoegen_opm

#         print(rapporten_leeg)

#         rapporten_test2= rapporten.copy(deep=True) 

#         rapporten_test2 = pd.concat([rapporten, rapporten_leeg], ignore_index=True, sort=False)
#         print(rapporten_test2)


