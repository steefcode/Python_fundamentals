# Importeer python bibliotheken
try: 
    import pandas as pd 
    import numpy as np 
    from tabulate import tabulate   
    import PyQt5
    import matplotlib
    matplotlib.use('Qt5Agg')  # Gebruik Qt5Agg backend
    import matplotlib.pyplot as plt
    import seaborn as sns
    from datetime import date, datetime
    # import datetime
    import os
    import uuid
except ImportError:
     print("Als de python bibliotheken niet geimporteerd kunnen worden open dan de terminal/command prompt en kopieer onderstaande code \n" 
           "pip install -r requirements.txt")

# Beperking om aantal kolommen zichtbaar te maken teniet doen
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Importeer modules 
try:
    from Class_gassen_update import Gassen 
    from Class_lees_bedrijven_update import BedrijvenDataReader 
    from Class_lees_rapporten_update import RapportenDataReader 
    from Class_lees_inspecteurs import InspecteursDataReader 
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
except ImportError:
    print("Zorg dat de handgemaakte modules allemaal in de map zitten waarin ook de data bestanden staan. /n"
          "Probeer daarna het programma weer te draaien.")

# Toewijzen datasets aan variabelen
bedrijven_reader = BedrijvenDataReader()
try:
    bedrijven = bedrijven_reader.lees_bedrijven_data()
except FileNotFoundError:
    print('Bestand bedrijven bestaat niet in de map, plaats deze er in om verder te kunnen met het programma')

reader_rapporten = RapportenDataReader()
try:
    rapporten = reader_rapporten.lees_rapporten_data()
except FileNotFoundError:
    print('Bestand rapporten bestaat niet in de map, plaats deze er in om verder te kunnen met het programma')

gassen_reader = Gassen("gassen.csv")
try:
    gassen = gassen_reader.lees_gassen()
except FileNotFoundError:
    print('Bestand gassen bestaat niet in de map, plaats deze er in om verder te kunnen met het programma')

reader_inspecteurs = InspecteursDataReader()
try:
    inspecteurs = reader_inspecteurs.lees_inspecteurs()
except FileNotFoundError:
    print('Bestand inspecteurs bestaat niet in de map, plaats deze er in om verder te kunnen met het programma')

# Test met printen van originele bestanden tov update bestanden
# print(rapporten)
# print(type(rapporten))
# print(rapporten.dtypes)

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
    clean_bedrijven = bedrijven.fillna('').astype(str).replace('NaT', '').sort_values(by=['Code'])
    print(clean_bedrijven)

def optie3():
    # Optie 3 toont de rapportages per inpsecteur. De gebruiker wordt gevraagd om een keuze te maken
    # Vervolgens wordt er een subset gemaakt van de Pandas Dataframe op basis van de input van de gebruiker
    # unique_icodes = rapporten['Icode'].unique()
    # print("Unieke inspecteurscodes:")
    # for icode in unique_icodes:
    #     print(icode)

    while True:
        try:
            unieke_icodes = np.sort(rapporten['Icode'].unique())
            print("Unieke inspecteurscodes die voorkomen in rapporten:")
            for icode in unieke_icodes:
                print(icode)
            icode_keuze = input("Voer de inspecteurscode in om de rapportages van de desbetreffende inspecteur te zien ")
            icode_keuze = icode_keuze.strip()
            if icode_keuze in unieke_icodes:
                break
            else:
                print("De ingevoerde inspecteurscode komt niet voor in de lijst.")  
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
            unieke_bcodes = np.sort(rapporten['Bcode'].unique())
            print("Unieke bedrijfscodes die voorkomen in rapporten:")
            for bcode in unieke_bcodes:
                print(bcode)
            bcode_keuze = input("Voer de bedrijfscode in om de rapportages van het desbetreffende bedrijf te zien ")
            bcode_keuze = bcode_keuze.strip()
            if bcode_keuze in unieke_bcodes:
                break  
            else:
                print("De ingevoerde bedrijfsscode komt niet voor in de lijst.")
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
            print("Ongeldige invoer. Voer CO2, CH4, NO2, NH3 of tot_uitstoot in. Let op de input is hoofdletter gevoelig")
        else:
            break
    
    heatmap_gen = HeatmapGassen(gassen)
    heatmap_gen.create_heatmap('x-waarde', 'y-waarde', input_gas)

def optie6():
    bedrijven_gassen_calculator = Boetes(bedrijven, gassen)
    result_boete = bedrijven_gassen_calculator.calculate_boete()
    print(type(result_boete)) 

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
            print("Ongeldige invoer. Voer CO2, CH4, NO2, NH3 of tot_uitstoot in. Let op de input is hoofdletter gevoelig")
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
    # Valideer input voor bedrijfscode, startend met een 0 gevolgd door een getal. 
    while True:
        input_code = input("Voer een bedrijfscode in: ")
        if input_code.strip().isdigit() and input_code.startswith('0') and len(input_code) == 4:
            break
        else:
            print("Ongeldige invoer. Voer alstublieft een 0 in volgend met een getal en wat bestaat uit 4 cijfers.")

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
    while True:
        try:
            rij_index = int(input("Voer in op welke regelnummer een wijziging moet plaatsvinden: ")) - 1
            if rij_index < 0 or rij_index >= len(bedrijven):
                raise IndexError(f"De index moet tussen 1 en {len(bedrijven)} zijn.")
            # Proceed with the rest of your code here for processing the valid input
            
            # For example, you can access the row with the given index like this:
            print("De huidige gegevens van de rij_index die u gekozen heeft")
            print(bedrijven.iloc[rij_index])
            
            # Exit the loop as the input is valid
            break
        
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor de rij_index.")
        
        except IndexError as e:
            print(e) 

    while True:
        kolom_naam = input("Voer de kolom naam in waar u de wijziging wilt door voeren ")
        kolom_naam = kolom_naam.strip().title() # Verwijderen van whitespaces en hoofdletter maken
        if kolom_naam not in bedrijven.columns:
            print("Ongeldige invoer. Voer een van de volgende namen in.")
            print(bedrijven.columns) 
        else:
            break
    
    while True:
        # variabele van datatype toekennen zodat de nieuwe invoer ook hetzelfde datatype is als het origineel
        kolom_datatype = bedrijven[kolom_naam].dtype
        waarde_wijziging = input(f"Voer de nieuwe waarde in voor de kolom '{kolom_naam}': ") 
        df_waarde_wijziging = pd.DataFrame({kolom_naam: [waarde_wijziging]})
        try:
            # Attempt to convert the input value to the same data type as kolom_naam
            bedrijven[kolom_naam].dtype == df_waarde_wijziging[kolom_naam].dtype
            break
        except ValueError:
            print(f"Ongeldige invoer. Voer een waarde van het juiste type ({kolom_datatype}) in.")
    
    '''Hier wordt de wijziging uitgevoerd '''
    bedrijven_modify = Modifier_Bedrijven(bedrijven)
    resultaten_bedrijf_modify = bedrijven_modify.wijzigen_bedrijf(rij_index, kolom_naam, waarde_wijziging)
    
    return resultaten_bedrijf_modify

def optie12(): 
    while True:
        input_icode = input("Voer een inspecteurscode in: ")
        input_icode = input_icode.strip()
        if input_icode.isdigit() and input_icode.startswith('0') and len(input_icode) == 3:
            break
        else:
            print("Ongeldige invoer. Voer alstublieft een code in die begint met een 0 en bestaat uit drie cijfers.")

    while True:
        input_bcode = input("Voer een bedrijfscode in: ")
        if input_bcode.strip().isdigit() and input_bcode.startswith('0') and len(input_bcode) == 4:
            break
        else:
            print("Ongeldige invoer. Voer alstublieft een 0 in volgend met een getal en bestaat uit 4 cijfers.")
    
    while True:
        input_bez_datum = input("Voer de bezoekdatum in (JJJJ-MM-DD): ")
        try:
            date_input_bez_datum  = datetime.strptime(input_bez_datum, '%Y-%m-%d').date()
            print("De ingevoerde datum is:", date_input_bez_datum)
            break
        except ValueError:
            print("De invoer is geen geldige datum (formaat: JJJJ-MM-DD)")
    
    while True:
        try:
            input_rap_datum = input("Voer de rapportagedatum in (JJJJ-MM-DD): ")
            date_input_rap_datum = datetime.strptime(input_rap_datum, '%Y-%m-%d').date()
            print("De ingevoerde datum is:", date_input_rap_datum)
            if date_input_rap_datum <= date_input_bez_datum:
                print("De rapportagedatum moet na de bezoekdatum liggen.")
                continue 
            break
        except ValueError:
         print("De invoer is geen geldige datum (formaat: JJJJ-MM-DD)")

    while True:
        input_status = input("Voer de status in van het rapport: ").strip().lower()  # verwijder whitespace en maak kleine letter
        if input_status in {'v', 'd'}:
            break  # check of input 'v' of 'd' is. Dan wordt de loop verlaten. 
        elif input_status.isdigit():
            print("Fout: Het ingevoerde status is een getal. Voer 'v' voor voltooid of 'd' voor in behandeling.")
        else:
            print("Fout: Ongeldige invoer. Voer 'v' voor voltooid of 'd' voor in behandeling.")
    
    while True:
        input_opm = input("Voer een opmerking in voor het rapport ")
        if input_opm.strip().isalpha():
            break
        else:
            print("Ongeldige invoer. De bedrijfsnaam mag alleen letters bevatten.")
    
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
    
    resultaten_rapporten = resultaten

    return resultaten_rapporten

def optie13():
    while True:
        try:
            rij_index = int(input("Voer in op welke regelnummer een wijziging moet plaatsvinden: ")) - 1
            if rij_index < 0 or rij_index >= len(rapporten):
                raise IndexError(f"De index moet tussen 1 en {len(rapporten)} zijn.")
            
            # print de regel informatie die de gebruiker gekozen heeft
            print("De huidige gegevens van de rij_index die u gekozen heeft")
            print(rapporten.iloc[rij_index])
            
            # sluit de loop als er een geldige waarde is
            break
        
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in voor de rij_index.")
        
        except IndexError as e:
            print(e) 

    while True:
        kolom_naam = input("Voer de kolom naam in waar u de wijziging wilt door voeren ")
        kolom_naam = kolom_naam.strip().title() # Verwijderen van whitespaces en hoofdletter maken
        if kolom_naam not in rapporten.columns:
            print("Ongeldige invoer. Voer een van de volgende namen in.")
            print(rapporten.columns) 
        else:
            break
    
    while True:
        # variabele van datatype toekennen zodat de nieuwe invoer ook hetzelfde datatype is als het origineel
        kolom_datatype = rapporten[kolom_naam].dtype
        waarde_wijziging = input(f"Voer de nieuwe waarde in voor de kolom '{kolom_naam}': ") 
        df_waarde_wijziging = pd.DataFrame({kolom_naam: [waarde_wijziging]})
        try:
            # Attempt to convert the input value to the same data type as kolom_naam
            rapporten[kolom_naam].dtype == df_waarde_wijziging[kolom_naam].dtype
            break
        except ValueError:
            print(f"Ongeldige invoer. Voer een waarde van het juiste type ({kolom_datatype}) in.")
    
    '''Hier wordt de wijziging uitgevoerd '''
    rapporten_modify = Modifier_Rapport(rapporten)
    resultaten_rapporten_modify = rapporten_modify.wijzigen_rapport(rij_index, kolom_naam, waarde_wijziging)
    
    return resultaten_rapporten_modify

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
        x = optie6()
        print(x)
        print(type(x))
        # print(type(bedrijven))
        # clean_bedrijven = bedrijven.fillna('').astype(str).replace('NaT', '').sort_values(by=['Code'])
        # clean_bedrijven = bedrijven.replace(np.nan, '', regex=True, inplace=True)
        # print(type(clean_bedrijven))
    elif keuze == "7":
        optie7()
    elif keuze == "8":
        optie8()
    elif keuze == "9":
        optie9()
    elif keuze == "10":
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        bedrijven = optie10()
        clean_bedrijven = bedrijven.fillna('').astype(str).replace('NaT', '').sort_values(by=['Code']).reset_index(drop=True)
        print(clean_bedrijven)
    elif keuze == "11": 
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        bedrijven= optie11()
        clean_bedrijven = bedrijven.fillna('').astype(str).replace('NaT', '').sort_values(by=['Code']).reset_index(drop=True)
        print(clean_bedrijven)
    elif keuze == "12":
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        rapporten = optie12()
        clean_rapporten = rapporten.fillna('').astype(str).replace('NaT', '').sort_values(by=['Icode']).reset_index(drop=True)
        print(clean_rapporten)
    elif keuze == "13": 
        '''Gezien er wijzigingen plaats vinden wordt de variabele overschreven'''
        rapporten = optie13()
        clean_rapporten = rapporten.fillna('').astype(str).replace('NaT', '').sort_values(by=['Icode']).reset_index(drop=True)
        print(clean_rapporten)
    elif keuze == '14':
        '''Als het programma stopt worden de wijzigingen en toevoegingen opgeslagen'''
        '''Gezien het format afwijkt van de daadwerkelijke txt bestanden wordt er een _update toegevoegd aan de bestanden'''
        export_bedrijven = PandasExporter(bedrijven)
        export_bedrijven.export_to_txt('bedrijven.txt')
        export_rapporten = PandasExporter(rapporten)
        export_rapporten.export_to_txt('rapporten.txt')
        print("Het programma wordt afgesloten. De gewijzigde gegevens worden opgeslagen")
        break
    else:
        print("Uw heeft een ongeldige keuze gemaakt. Kies nogmaals.\n")
