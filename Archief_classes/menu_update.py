# Importeer python bibliotheken
try: 
    import pandas as pd 
    import numpy as np 
    from tabulate import tabulate   
    import matplotlib.pyplot as plt 
    import seaborn as sns
    from datetime import date, datetime
    import datetime
    import os
except ImportError:
     print("Gebruik pip install <bibliotheeknaam> of conda install <bibliotheeknaam> om de bibliotheken te installeren en te plaatsen in uw virtual environment.\n"
           "Gebruik conda als u deze als package manager gebruikt anders gebruik pip")

# Beperking om aantal kolommen zichtbaar te maken teniet doen
pd.set_option('display.max_columns', None)

# Importeer modules 
from Class_gassen import Gassen 
from Class_lees_bedrijven_update import BedrijvenDataReader 
from Class_lees_rapporten_update import RapportenDataReader 
from Class_inspecteurs import Inspecteurs 
from Class_Subset_Rapporten import Subset_Rapporten 
from Class_Heatmap_Gassen import HeatmapGassen 
from Class_Boetes import Boetes 
from Class_analyse import AntiJoinAndSort 
from Class_Subset_Coordinaten import Subsetcoordinaten 
from Class_Subset_Bedrijfsnaam import Subset_Bedrijfsnaam 
from Class_Concatenator import DataFrameConcatenator 
from Class_Modifier_Bedrijven import Modifier_Bedrijven 
from Class_Modifier_Rapport import Modifier_Rapport
from Class_PandasExport import PandasExporter

# Toewijzen datasets aan variabelen
bedrijven_reader = BedrijvenDataReader()
bedrijven = bedrijven_reader.lees_bedrijven_data()
reader_rapporten = RapportenDataReader()
rapporten = reader_rapporten.lees_rapporten_data()
gassen = Gassen.lees_gassen() 
inspecteurs = Inspecteurs.lees_inspecteurs() 

def tonen_menu():
    print("=== Welkom in het menu, maak een keuze ===") 
    print("1. Tonen van inspecteurs") 
    print("2. Tonen  bedrijven") 
    print("3. Tonen bezoekrapporten per inspecteur") 
    print("4. Tonen bezoekrapporten per bedrijf") 
    print("5. Plotten van meetgegevens") 
    print("6. Bepalen en tonen boetes")  
    print("7. Analyseren meetgegevens") 
    print("8. Beheer bedrijfsgegevens, zoek locatie") 
    print("9. Beheer bedrijfsgegevens, zoek naam") 
    print("10. Beheer bedrijfsgegevens, toevoegen gegevens") 
    print("11. Beheer bedrijfsgegevens, wijzigen gegevens") 
    print("12. Beheer bezoekrapporten, toevoegen rapport gegevens") 
    print("13. Beheer bezoekrapporten, wijzigen rapport gegevens")
    print("Stop.")

def keuze_gebruiker():
    keuze = input("Voer uw keuze in (1 t/m 13) ")
    return keuze

def optie1():
    # Optie 1 toon een overzicht van de inspecteurs
    print(inspecteurs)

def optie2():
    # Optie 2 toont de bedrijven
    print(bedrijven)

def optie3():
    # Optie 3 toont de rapportages per inpsecteur. De gebruiker wordt gevraagd om een keuze te maken
    # Vervolgens wordt er een subset gemaakt van de Pandas Dataframe op basis van de input van de gebruiker
    icode_keuze = input("Voer de inpsecteurscode in om de rapportages van de desbetreffende inspecteur te zien ")
    sub_rapport = Subset_Rapporten(rapporten)
    icode_rapporten = sub_rapport.subset_icode(icode_keuze)
    print(icode_rapporten)

def optie4():
    # Optie 4 toont de rapportages per inpsecteur. De gebruiker wordt gevraagd om een keuze te maken
    # Vervolgens wordt er een subset gemaakt van de Pandas Dataframe op basis van de input van de gebruiker
    bcode_keuze = input("Voer de bedrijfscode in om de rapportages van het desbetreffende bedrijf te zien ")
    sub_rapport = Subset_Rapporten(rapporten)
    bcode_rapporten = sub_rapport.subset_bcode(bcode_keuze)
    print(bcode_rapporten)

def optie5():
    # Optie 5 plot een heatmap van het gassen bestand. De gebruiker maakt een keuze. 
    # Vervolgens wordt deze keuze weergegeven in een heatmap. 
    gas_keuze = input("Voer een gas in die u wilt zien in de heatmap ")
    heatmap_gen = HeatmapGassen(gassen)
    heatmap_gen.create_heatmap(gas_keuze)

def optie6():
    print("Dit moet nog gemaakt en getest worden")
    bedrijven_gassen_calculator = Boetes(bedrijven, gassen)
    result_boete = bedrijven_gassen_calculator.calculate_boete()
    print(result_boete) 

def optie7():
    # Optie 7 maakt een anti-join op de datasets van gassen en bedrijven
    # Vervolgens wordt de gebruiker om input gevraagd. 
    # De input is een gas of de berek_uitstoot in het gassen bestand
    # Vervolgens wordt op basis van de input van de gebruiker de dataset gesorteerd. 
    # Zo kan een gebruiker opzoek naar vervuilende bedrijven die niet voorkomen in het bedrijven bestand
    anti_join_sorter = AntiJoinAndSort(bedrijven, gassen)
    anti_join_sorter.perform_anti_join()

    user_input = input("Voer een keuze in: CO2, CH4, NO2 of tot_uitstoot ")
    anti_join_sorter.sort_data(user_input)
    sorted_data = anti_join_sorter.sorted_data
    print(sorted_data)

def optie8():
    # Deze functie zoekt op basis van de coordinaten x en y en geeft het bedrijf weer met de kleinste afstand tot de ingegeven coordinaten van de gebruiker
    
    # Voeg een x en y coordinaat toe om op te zoeken 
    input_y = float(input("Voer een y coordinaat in "))
    input_x = float(input("Voer een x coordinaat in "))

    # Create an instance of the DataSubset class
    diff_subset_coordinaten = Subsetcoordinaten(bedrijven)

    resultaten = diff_subset_coordinaten.verschil_coordinaten(input_x, input_y)
    print("Subset with smallest difference:")
    print(resultaten)

def optie9():
    # Deze functie zoekt op basis de naam of een deel van de naam. Deze wordt door de gebruiker ingevoerd. 
    # Vervolgens wordt het eerst gevonden bedrijf gevonden. 
    # Create an instance of the DataSubset class
    data_subsetter = Subset_Bedrijfsnaam(bedrijven)

    # # Enter the substring you want to search for in the BedrijfsNaam column
    zoekterm_bedrijf = input("Op welk bedrijfsnaam wilt u zoeken ")

    # Call the method to perform the data subset
    resultaten = data_subsetter.zoek_bedrijfsnaam(zoekterm_bedrijf )

    print(resultaten)

def optie10():

    input_code = input("Voer een bedrijfscode in ")
    input_naam = input("Voer de naam van het bedrijf in ")
    input_straat = input("Voer de straat van het bedrijf in ")
    input_huisnr = input("Voer het huisnummer van het bedrijf in ")
 
    while True:
        input_postcode = input("Voer de postcode van het bedrijf in ")
        '''Check of de input bestaat uit 6 karakters en vervolgens checken of de eerste 4 karakters getallen zijn'''
        '''Vervolgens checken of de laatste 2 karakters letters zijn'''
        if len(input_postcode) == 6 and input_postcode[:4].isdigit() and input_postcode[4:].isalpha():
            print("Het door u opgegeven postcode is niet geldig, het format moeten 4 getallen zijn gevolgd door 2 letters")
            break
        else:
            print("Geldige postcode")
    
    input_plaats = input("Voer de plaast van het bedrijf in ")
    input_xwaarde = int(input("Voer het x coordinaat van het bedrijf in "))
    input_ywaarde = int(input("Voer het y coordinaat van het bedrijf in "))
    input_maxuitst = int(input("Voer de maximale uitstoot van het bedrijf toe "))
    input_controle = input("Voer in of er een controle heeft plaatsgevonde, zo ja voer j in zo niet dan voer n in ")
    input_frequentie = float(input("Voer het aantal bezoeken in dat heeft plaatsgevonden "))

    '''Controle of het getal van 1 tot en met 12 is. Anders wordt de gebruiker gevraagd dit aan te passen'''
    while input_frequentie < 0.0 or input_frequentie > 12.0: 
        print("Het maximum aantal  geplande bezoeken is tussen 1 en 12 bezoeken per jaar, voer een getal in van 1 t/m 12")
        input_frequentie = float(input("Voer het aantal bezoeken in dat heeft plaatsgevonden "))
    
    input_ctpers = input("Voer de naam in van de contactpersoon van het bedrijf")

    '''Kopie maken van bedrijven dataframe zodat de nieuwe regels eraan kan worden toegvoegd'''
    bedrijven_regel = bedrijven.copy(deep=True).head(0)

    bedrijven_regel.at[0, "Code"] = input_code
    bedrijven_regel.at[0, "Naam"] = input_naam
    bedrijven_regel.at[0, "Straat"] = input_straat
    bedrijven_regel.at[0, "Huisnr"] = input_huisnr
    bedrijven_regel.at[0, "Postcd"] = input_postcode
    bedrijven_regel.at[0, "Plaats"] = input_plaats
    bedrijven_regel.at[0, "Xwaarde"] = input_xwaarde
    bedrijven_regel.at[0, "Ywaarde"] = input_ywaarde
    bedrijven_regel.at[0, "Maxuitst"] = input_maxuitst
    bedrijven_regel.at[0, "Controle"] = input_controle
    bedrijven_regel.at[0, "Freq"] = input_frequentie
    bedrijven_regel.at[0, "Ctpers"] =  input_ctpers

    concatenator = DataFrameConcatenator()
    concatenator.add_dataframe(bedrijven)
    concatenator.add_dataframe(bedrijven_regel)

    resultaten = concatenator.concatenate()
    return resultaten

def optie11(): 
    '''Gezien python zero based index heeft is het rijnummer altijd min 1'''
    rij_index = int(input("Op welke rij wilt u een wijziging door voeren? ")) - 1
    kolom_naam = input("Voer de kolom in waar u de wijziging wilt door voeren ")
    waarde_wijziging = input("Voer een waarde in die u wilt wijzigen")

    '''Hier wordt de wijziging uitgevoerd '''
    bedrijven_modify = Modifier_Bedrijven(bedrijven)
    bedrijven_modify.wijzigen_bedrijf(rij_index, kolom_naam, waarde_wijziging)
    print(bedrijven)

def optie12(): 
    input_icode = input("Voer een inspecteurscode in ")
    input_bcode = input("Voer een bedrijfscode in ")
    input_bez_datum = input("Voer de bezoekdatum in ")
    
    '''Controle of de ingevoerde input wel een datum format is '''
    while True: 
        try: 
            date.fromisoformat(input_bez_datum)
            break
        except ValueError:
            input_bez_datum = input("Geen geldige datum, vul aub een datum in met format jjjj-mm-dd ") 
    
    input_rap_datum = input("Voer de rapportage datum in ")

    while True: 
        try: 
            date.fromisoformat(input_rap_datum)
            break
        except ValueError:
            input_rap_datum = input("Geen geldige datum, vul aub een datum in met format jjjj-mm-dd ") 
    
    while input_bez_datum > input_rap_datum: 
        print("De bezoekdatum is eerder dan de rapportage datum. vul aub beide datums nogmaals in zodat de rapportage datum later is dan de bezoekdatum")
        input_bez_datum = input()
        input_rap_datum = input()
        
        '''Gezien er wederom een ongeldige datum kan worden ingevoerd moet de date.fromisoformat() methode wederom worden toegepast '''
        while True: 
            try: 
                date.fromisoformat(input_bez_datum)
                break
            except ValueError:
                input_bez_datum = input("Geen geldige datum, vul aub een datum in met format jjjj-mm-dd ") 
    
        while True: 
            try: 
                date.fromisoformat(input_rap_datum)
                break
            except ValueError:
                input_rap_datum = input("Geen geldige datum, vul aub een datum in met format jjjj-mm-dd ") 

    input_status = input("Voer de status in van het rapport ")
    input_opm = input("Voer een opmerking in voor het rapport ")


    '''Kopie maken van bedrijven dataframe zodat de nieuwe regels eraan kan worden toegvoegd'''
    rapport_regel = rapporten.copy(deep=True).head(0)

    rapport_regel.at[0, "Icode"] = input_icode
    rapport_regel.at[0, "Bcode"] = input_bcode
    rapport_regel.at[0, "Bezdat"] = input_bez_datum
    rapport_regel.at[0, "Rapdat"] = input_rap_datum
    rapport_regel.at[0, "Status"] = input_status
    rapport_regel.at[0, "Opm"] = input_opm

    concatenator = DataFrameConcatenator()
    concatenator.add_dataframe(rapporten)
    concatenator.add_dataframe(rapport_regel)

    resultaten = concatenator.concatenate()
    return resultaten

def optie13():
    '''Gezien python zero based index heeft is het rijnummer altijd min 1'''
    rij_index = int(input("Op welke rij wilt u een wijziging door voeren? ")) - 1
    kolom_naam = input("Voer de kolom in waar u de wijziging wilt door voeren ")
    waarde_wijziging = input("Voer een waarde in die u wilt wijzigen")

    modifier = Modifier_Rapport(rapporten)

    modifier.wijzigen_rapport(rij_index, kolom_naam, waarde_wijziging)
    print(rapporten)

# Menu keuzes en de daarbij behorende functies 

while True:
    tonen_menu()
    keuze = keuze_gebruiker()

    if keuze == '1':
        optie1()
    elif keuze == '2':
        optie2()
    elif keuze == '3':
        optie3()
    elif keuze == '4':
        optie4()
    elif keuze == "5":
        optie5()
    elif keuze == "6":
        optie6()
    elif keuze == "7":
        optie7()
    elif keuze == "8":
        optie8()
    elif keuze == "9":
        optie9()
    elif keuze == "10":
        optie10()
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        bedrijven = optie10()
    elif keuze == "11":
        optie11()
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        bedrijven = optie11()
    elif keuze == "12":
        optie12() 
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        rapporten = optie12()
    elif keuze == "13": 
        optie13()
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        rapporten = optie13()
    elif keuze == 'Stop':
        '''Als het programma stopt worden de wijzigingen en toevoegingen opgeslagen'''
        '''Gezien het format afwijkt van de daadwerkelijke txt bestanden wordt er een _update toegevoegd aan de bestanden'''
        export_bedrijven = PandasExporter(bedrijven)
        export_bedrijven.export_to_txt('bedrijven_update.txt')
        export_rapporten = PandasExporter(rapporten)
        export_rapporten.export_to_txt('rapporten_update.txt')
        print("Het programma wordt afgesloten. De gewijzigde gegevens worden opgeslagen")
        break
    else:
        print("Uw heeft een ongeldige keuze gemaakt. Kies nogmaals.\n")
