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
     print("Als de python bibliotheken niet geimporteerd kunnen worden open dan de terminal/command prompt en kopieer onderstaande code \n" 
           "pip install -r requirements.txt")

# Beperking om aantal kolommen zichtbaar te maken teniet doen
pd.set_option('display.max_columns', None)

# Importeer modules 
from Class_gassen_update import Gassen 
from Class_lees_bedrijven_update import BedrijvenDataReader 
from Class_lees_rapporten_update import RapportenDataReader 
from Class_inspecteurs import Inspecteurs 
from Class_Subset_Rapporten import Subset_Rapporten 
from Class_Heatmap_Gassen import HeatmapGassen 
from Class_Boetes import Boetes 
from Class_analyse import AntiJoinAndSort 
from Class_Subset_Coordinaten_update import Subsetcoordinaten_update
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
gassen_reader = Gassen("gassen.csv")
gassen = gassen_reader.lees_gassen()
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
    print("14. Stop de applicatie.")

def keuze_gebruiker():
    keuze = input("Voer uw keuze in (1 t/m 14) ")
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
    while True:
        try:
            icode_keuze = int(input("Voer de inspecteurscode in om de rapportages van de desbetreffende inspecteur te zien "))
            break  
        except ValueError:
            print("Ongeldige invoer. Voer een inspecteurscode in.") 

    sub_rapport = Subset_Rapporten(rapporten)
    icode_rapporten = sub_rapport.subset_icode(icode_keuze)
    print(icode_rapporten)

def optie4():
    # Optie 4 toont de rapportages per inpsecteur. De gebruiker wordt gevraagd om een keuze te maken
    # Vervolgens wordt er een subset gemaakt van de Pandas Dataframe op basis van de input van de gebruiker
    while True:
        try:
            bcode_keuze = int(input("Voer de bedrijfscode in om de rapportages van het desbetreffende bedrijf te zien "))
            break  
        except ValueError:
            print("Ongeldige invoer. Voer een bedrijfscode in.") 

    sub_rapport = Subset_Rapporten(rapporten)
    bcode_rapporten = sub_rapport.subset_bcode(bcode_keuze)
    print(bcode_rapporten)

def optie5():
    # Optie 5 plot een heatmap van het gassen bestand. De gebruiker maakt een keuze. 
    # Vervolgens wordt deze keuze weergegeven in een heatmap. 

    while True:
        input_gas = input("Voer naam van het gas in waar u een heatmap van wilt zien ")
        input_gas = input_gas.replace(" ", "") # Verwijderen van whitespaces
        if input_gas not in gassen.columns:
            print("Ongeldige invoer. Voer CO2, CH4, NO2, NH3 of tot_uitstoot in.")
        else:
            break
    
    heatmap_gen = HeatmapGassen(gassen)
    heatmap_gen.create_heatmap('x-waarde', 'y-waarde', input_gas)

def optie6():
    bedrijven_gassen_calculator = Boetes(bedrijven, gassen)
    result_boete = bedrijven_gassen_calculator.calculate_boete()
    print(result_boete) 

def optie7():
    # Optie 7 maakt een anti-join op de datasets van gassen en bedrijven
    # Vervolgens wordt de gebruiker om input gevraagd. 
    # De input is een gas of de berek_uitstoot in het gassen bestand
    # Vervolgens wordt op basis van de input van de gebruiker de dataset gesorteerd. 
    # Zo kan een gebruiker opzoek naar vervuilende bedrijven die niet voorkomen in het bedrijven bestand
    while True:
        input_gas_sort = input("Voer een keuze in: CO2, CH4, NO2, NH3 of tot_uitstoot om inzicht te krijgen in de grootste \n"
                                "vervuiler per gekozen gas ")
        input_gas_sort = input_gas_sort.replace(" ", "") # Verwijderen van whitespaces
        if input_gas_sort.strip() not in gassen.columns:
            print("Ongeldige invoer. Voer CO2, CH4, NO2, NH3 of tot_uitstoot in.")
        else:
            break

    anti_join_sorter = AntiJoinAndSort(bedrijven, gassen)
    anti_join_sorter.perform_anti_join()

    anti_join_sorter.sort_data(input_gas_sort)
    sorted_data = anti_join_sorter.sorted_data
    print(sorted_data)

def optie8():
    # Deze functie zoekt op basis van de coordinaten x en y en geeft het bedrijf weer met de kleinste afstand tot de ingegeven coordinaten van de gebruiker
    
    # Voeg een x en y coordinaat toe om op te zoeken 
    while True:
        try:
            input_y = float(input("Voer een y coordinaat in "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal.")

    while True:
        try:
            input_x = float(input("Voer een x coordinaat in "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal.")

    # Create an instance of the DataSubset class
    diff_subset_coordinaten = Subsetcoordinaten_update(bedrijven)

    resultaten = diff_subset_coordinaten.verschil_coordinaten_update(input_x, input_y)
    print(resultaten)

def optie9():
    # Deze functie zoekt op basis de naam of een deel van de naam. Deze wordt door de gebruiker ingevoerd. 
    # Vervolgens wordt het eerst gevonden bedrijf gevonden. 
    # Create an instance of the DataSubset class
    
    # Valideer zoekterm bedrijf
    while True:
        input_zoekterm_bedrijf = input("Op welk bedrijfsnaam wilt u zoeken  ")
        if input_zoekterm_bedrijf.strip().isalpha():
            break
        else:
            print("Ongeldige invoer. De bedrijfsnaam mag alleen letters bevatten.")

    data_subsetter = Subset_Bedrijfsnaam(bedrijven)

    # Methode om bedrijf te zoeken aanroepen die naar benadering het dichtsbij komt met de ingevoerde naam. 
    resultaten = data_subsetter.zoek_bedrijfsnaam(input_zoekterm_bedrijf)

    print(resultaten)

def optie10():
    # Valideer input voor bedrijfscode
    while True:
        try:
            input_code = int(input("Voer een bedrijfscode in "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor de bedrijfscode.")

    # Valideer input voor bedrijfsnaam
    while True:
        input_naam = input("Voer de naam van het bedrijf in ")
        if input_naam.strip().isalpha():
            break
        else:
            print("Ongeldige invoer. De bedrijfsnaam mag alleen letters bevatten.")
        
    # Valideer input voor straat
    while True:  
        input_straat = input("Voer de straat van het bedrijf in ")
        if input_straat.strip().isalpha():
            break
        else:
            print("Ongeldige invoer. De straatnaam mag alleen letters bevatten.")
            
    # Valideer input voor postcode
    while True:
        input_postcode = input("Voer de postcode van het bedrijf in ")
        input_postcode = input_postcode.replace(" ", "")
        if len(input_postcode) == 6 and input_postcode[:4].isdigit() and input_postcode[4:].isalpha():
            break
        else:
            print("Het door u opgegeven postcode is niet geldig, het formaat moet bestaan uit 4 cijfers gevolgd door 2 letters.")
        
    # Valideer input voor plaats
    while True:
        input_plaats = input("Voer de plaats van het bedrijf in ")
        if input_plaats.strip().isalpha():
            break
        else:
            print("Ongeldige invoer. De plaatsnaam mag alleen letters bevatten.")

    # Valideer input voor huisnummer
    while True:
        try:
            input_huisnr = int(input("Voer het huisnummer in "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor het huisnummer")

    # Valideer input voor x coordinaat
    while True:
        try:
            input_xwaarde = int(input("Voer een x coordinaat in "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor de xwaarde.")
        
    # Valideer input voor y coordinaat
    while True:
        try:
            input_ywaarde = int(input("Voer een y coordinaat in "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor de ywaarde.")
        
    # Valideer input voor maximale uitstoot
    while True:
        try:
            input_maxuitst = int(input("Voer de maximale uitstoot van het bedrijf toe. "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor de maximale uitstoot.")
        
    # Valideer input voor controle
    while True:
        input_controle = input("Voer in of er een controle heeft plaatsgevonden, zo ja voer j in, zo niet dan voer n in ")
        input_controle = input_controle.strip()
        if input_controle.lower() in ('j', 'n'):
            break
        else:
            print("Ongeldige invoer. Voer 'j' in als er een controle heeft plaatsgevonden, 'n' anders.")

    # Valideer input voor frequentie
    while True:
        try:
            input_frequentie = float(input("Voer het aantal bezoeken in dat heeft plaatsgevonden "))
            if input_frequentie in range(0,13):
                break
            else:
                print("Ongeldige invoer. Voer een getal geldig getal in. Van 0 t/m 12.")
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor de frequentie.")
        
    # Valideer input voor contactpersoon
    while True:
        input_ctpers = input("Voer de naam in van de contactpersoon van het bedrijf ")
        if input_ctpers.strip().isalpha():
            break
        else:
            print("Ongeldige invoer. De contactpersoon mag alleen letters bevatten.")
        
    # Kopie van bedrijven aanmaken zodat dezelfde structuur gehanteerd wordt voor concatoneren
    bedrijven_regel = bedrijven.copy(deep=True).head(0)

    # Nieuwe regel aanmaken voor bedrijven kopie dataframe
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

    # Originele bedrijven bestand samenvoegen met nieuw gemaakte regel
    concatenator = DataFrameConcatenator()
    concatenator.add_dataframe(bedrijven)
    concatenator.add_dataframe(bedrijven_regel)

    # Bedrijven dataframe updaten met nieuwe regel
    resultaten = concatenator.concatenate()
    resultaten_bedrijven = resultaten

    return resultaten_bedrijven

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
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        bedrijven= optie10()
    elif keuze == "11": 
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        bedrijven_wijzigen = optie11()
        bedrijven = bedrijven_wijzigen 
    elif keuze == "12":
        optie12() 
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        rapporten = optie12()
    elif keuze == "13": 
        optie13()
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        rapporten = optie13()
    elif keuze == '14':
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
