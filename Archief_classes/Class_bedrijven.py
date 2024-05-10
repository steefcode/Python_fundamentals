# Importeren van benodigde bibliotheken  
import pandas as pd 
import numpy as np 
from tabulate import tabulate
from datetime import date, datetime
from Class_gassen import Gassen  

gassen = Gassen.lees_gassen()
print(gassen)

class Bedrijven:

    def lees_bedrijven():
        colspecs = [(0, 4), (4, 24), (24, 54), (54, 59), (59, 65), (65, 85), (85, 87), (87, 89), (89, 99), (99, 109), (109, 117), 
                (117, 118), (118, 120), (120, 140)]
        
        bedrijven = pd.read_fwf("bedrijven.txt", header = None, colspecs = colspecs,
                                names = ["Code", 
                                    "Naam", 
                                    "Straat", 
                                    "Huisnr", 
                                    "Postcd", 
                                    "Plaats", 
                                    "Xwaarde", 
                                    "Ywaarde", 
                                    "Maxuitst", 
                                    "Beruitst", 
                                    "Boete", 
                                    "Controle", 
                                    "Freq", 
                                    "Ctpers"], 
                                    dtype = {"Code" : str, 
                                    "Naam" : str, 
                                    "Straat": str , 
                                    "Huisnr": str , 
                                    "Postcd": str , 
                                    "Plaats": str , 
                                    "Xwaarde": int , 
                                    "Ywaarde": int , 
                                    "Maxuitst": int , 
                                    "Beruitst": float , 
                                    "Boete": float, 
                                    "Controle": str, 
                                    "Freq": float,  
                                    "Ctpers": str})
         
        return bedrijven
        
    def toon_bedrijven():
        print(bedrijven)

    def zoek_bedrijven_naam():
        zoek_naam_bedrijf = input("Hoe heet het bedrijf waar u naar opzoek bent? ")
        selectie_bedrijven_naam = bedrijven[bedrijven["Naam"].str.contains(zoek_naam_bedrijf)].head(1)

        if selectie_bedrijven_naam.empty:
            print("Er zijn geen bedrijven met deze naam")
        else:
             print(selectie_bedrijven_naam)
    
    def zoek_bedrijven_locatie():
        zoek_locatie_x_bedrijven = int(input("Geef het x coordinaat "))
        while zoek_locatie_x_bedrijven > 99 or zoek_locatie_x_bedrijven < 0:
            print("Het door u opgegeven x coordinaat is hoger dan 99 of lager dan 0, vul een coordinaat van 0 t/m 99 in") 
            zoek_locatie_x_bedrijven = int(input("Geef het x coordinaat "))
        else: 
            print(zoek_locatie_x_bedrijven)
        
        '''Zoeken naar Y coordinaat'''
        zoek_locatie_y_bedrijven = int(input("Geef het y coordinaat ")) 
        while zoek_locatie_y_bedrijven > 99 or zoek_locatie_y_bedrijven < 0:
            print("Het door u opgegeven x coordinaat is hoger dan 99 of lager dan 0, vul een coordinaat van 0 t/m 99 in") 
            zoek_locatie_y_bedrijven = int(input("Geef het x coordinaat "))
        else: 
            print(zoek_locatie_y_bedrijven)
        
        selectie_bedrijven_locatie = bedrijven
        selectie_bedrijven_locatie["verschilx"] = selectie_bedrijven_locatie["Xwaarde"] - zoek_locatie_x_bedrijven
        selectie_bedrijven_locatie["verschily"] = selectie_bedrijven_locatie["Ywaarde"] - zoek_locatie_y_bedrijven
        selectie_bedrijven_locatie["verschil_locatie"] = selectie_bedrijven_locatie["verschilx"] + selectie_bedrijven_locatie["verschily"]
        
        '''Correctie voor negatieve waardes en sorteren van klein naar groot'''
        selectie_bedrijven_locatie["verschil_locatie"] = abs(selectie_bedrijven_locatie["verschil_locatie"])
        selectie_bedrijven_locatie = selectie_bedrijven_locatie.sort_values(by=['verschil_locatie'])
        selectie_bedrijven_locatie  = selectie_bedrijven_locatie.drop(['verschily', 'verschilx', "verschil_locatie"], axis=1).head(1)
        # print(selectie_bedrijven_locatie)
        return selectie_bedrijven_locatie 
    
    def bepalen_boetes(): 
        gassen_bedrijven = bedrijven.copy(deep=True) 
        gassen_bedrijven_gebieden = bedrijven.copy(deep=True)

        gassen_bedrijven = gassen.head(0)
        gassen_bedrijven_gebieden = gassen.head(0)

        print(gassen_bedrijven)
        print(gassen_bedrijven_gebieden)

        for index, bedrijf in bedrijven.iterrows():
                    x_bedrijf = bedrijf["Xwaarde"]
                    y_bedrijf = bedrijf["Ywaarde"]
                    x_bedrijf_list = [*range(x_bedrijf - 2, x_bedrijf + 3, 1)]
                    y_bedrijf_list = [*range(y_bedrijf - 2, y_bedrijf + 3, 1)]

                    df = gassen[gassen["x-waarde"].isin(x_bedrijf_list)]
                    df2 = df[df["y-waarde"].isin(y_bedrijf_list)] 
                    df2 = df2.reset_index()

                    df2["berek_uitstoot"] = 0
                    
                    """Uitstoot berekening met afstand 2 tot bedrijf"""
                    df2["berek_uitstoot"] = np.where((df2["x-waarde"].isin(range(x_bedrijf -2, x_bedrijf + 3))) &
                                        (df2["y-waarde"].isin(range(y_bedrijf -2, y_bedrijf + 3))), 
                                        df2["tot_uitstoot"] * 0.25, df2["berek_uitstoot"]) 
                    
                    """Uitstoot berekening met afstand 1 tot bedrijf"""
                    df2["berek_uitstoot"] = np.where((df2["x-waarde"].isin(range(x_bedrijf -1, x_bedrijf + 2))) &
                                        (df2["y-waarde"].isin(range(y_bedrijf -1, y_bedrijf + 2))), 
                                        df2["tot_uitstoot"] * 0.5, df2["berek_uitstoot"]) 
                    
                    """Uitstoot berekening bedrijf"""
                    df2["berek_uitstoot"] = np.where((df2["x-waarde"] == x_bedrijf) & (df2["y-waarde"] == y_bedrijf), df2["tot_uitstoot"], 
                                        df2["berek_uitstoot"])
                    
                    df2["gemiddelde_berek_uitstoot"] = df2["berek_uitstoot"].mean() 
                    
                    df3 = df2.copy(deep=True)
                    df3 = df3[(df3["x-waarde"] == x_bedrijf) & (df3["y-waarde"] == y_bedrijf)]

                    gassen_bedrijven = pd.concat([gassen_bedrijven, df3], ignore_index=True, sort=False)
                    
        bedrijven_gassen = pd.merge(bedrijven, gassen_bedrijven[['berek_uitstoot', 'gemiddelde_berek_uitstoot', 'x-waarde', 'y-waarde']], 
                                        how = 'left', left_on = ['Xwaarde','Ywaarde'], 
                                        right_on = ['x-waarde','y-waarde']) 

        bedrijven_gassen["Beruitst"] = bedrijven_gassen["berek_uitstoot"]
        bedrijven_gassen["Boete"] = np.where(bedrijven_gassen["Maxuitst"] - bedrijven_gassen["gemiddelde_berek_uitstoot"] < 0, 
                                            bedrijven_gassen["Maxuitst"] - bedrijven_gassen["gemiddelde_berek_uitstoot"] * 1000,
                                            "Nan")

        bedrijven_gassen = bedrijven_gassen.iloc[:, 0:14].copy()
        return bedrijven_gassen
    
    def analyse(): 
        gassen_bedrijven = bedrijven.copy(deep=True) 
        gassen_bedrijven_gebieden = bedrijven.copy(deep=True)

        gassen_bedrijven = gassen.head(0)
        gassen_bedrijven_gebieden = gassen.head(0)

        print(gassen_bedrijven)
        print(gassen_bedrijven_gebieden)

        for index, bedrijf in bedrijven.iterrows():
                    x_bedrijf = bedrijf["Xwaarde"]
                    y_bedrijf = bedrijf["Ywaarde"]
                    x_bedrijf_list = [*range(x_bedrijf - 2, x_bedrijf + 3, 1)]
                    y_bedrijf_list = [*range(y_bedrijf - 2, y_bedrijf + 3, 1)]

                    df = gassen[gassen["x-waarde"].isin(x_bedrijf_list)]
                    df2 = df[df["y-waarde"].isin(y_bedrijf_list)] 
                    df2 = df2.reset_index()

                    df2["berek_uitstoot"] = 0
                    
                    """Uitstoot berekening met afstand 2 tot bedrijf"""
                    df2["berek_uitstoot"] = np.where((df2["x-waarde"].isin(range(x_bedrijf -2, x_bedrijf + 3))) &
                                        (df2["y-waarde"].isin(range(y_bedrijf -2, y_bedrijf + 3))), 
                                        df2["tot_uitstoot"] * 0.25, df2["berek_uitstoot"]) 
                    
                    """Uitstoot berekening met afstand 1 tot bedrijf"""
                    df2["berek_uitstoot"] = np.where((df2["x-waarde"].isin(range(x_bedrijf -1, x_bedrijf + 2))) &
                                        (df2["y-waarde"].isin(range(y_bedrijf -1, y_bedrijf + 2))), 
                                        df2["tot_uitstoot"] * 0.5, df2["berek_uitstoot"]) 
                    
                    """Uitstoot berekening bedrijf"""
                    df2["berek_uitstoot"] = np.where((df2["x-waarde"] == x_bedrijf) & (df2["y-waarde"] == y_bedrijf), df2["tot_uitstoot"], 
                                        df2["berek_uitstoot"])
                    
                    df2["gemiddelde_berek_uitstoot"] = df2["berek_uitstoot"].mean() 

                    gassen_bedrijven_gebieden = pd.concat([gassen_bedrijven_gebieden, df2], ignore_index=True, sort=False)

                    analyse = pd.merge(gassen,gassen_bedrijven_gebieden[['x-waarde', 'y-waarde']], how='outer', 
                                left_on=['x-waarde','y-waarde'], 
                                right_on=['x-waarde','y-waarde'], indicator = True)
                    
                    analyse = analyse[analyse["_merge"] == "left_only"]
                    analyse = analyse.iloc[:, 0:7].copy()

                    analyse = analyse.sort_values(by=['tot_uitstoot'], ascending= False)    

                    return analyse 
    
def bedrijf_wijzigen():
    opties_wijzigingen_bedrijf = bedrijven.columns[[1, 6, 7, 8, 10, 11, 12]]
    print(opties_wijzigingen_bedrijf) 
    onderdeel_wijziging_bedrijf = input("Welke inhoud wilt u wijzigen van de hierboven genoemde kolommen? ") 


    waarde_wijziging = input(f"Voer de waarde in die u wilt toepassen voor {onderdeel_wijziging_bedrijf} ")
    print(bedrijven["Naam"])
    bedrijf_wijziging = input(f"Voor welk bedrijf wilt u de wijziging doorvoeren? ")

    print(bedrijven[onderdeel_wijziging_bedrijf]) 

    bedrijven_test = bedrijven.copy(deep=True)

    bedrijven_test[onderdeel_wijziging_bedrijf] = np.where(bedrijven_test["Naam"] == bedrijf_wijziging, 
                                                        waarde_wijziging, bedrijven_test[onderdeel_wijziging_bedrijf])
    print(bedrijven_test["Xwaarde"])     

def bedrijf_toevoegen():
    bedrijven_leeg = bedrijven.copy(deep=True)
    bedrijven_leeg = bedrijven_leeg.head(0)
    print(bedrijven_leeg)
    print(bedrijven_leeg.dtypes) 

    toevoegen_code = input("Voer een bedrijfscode in ")
    while len(toevoegen_code) != 4:
        print("De code die u opvoerde is te lang of te kort, maak een code aan met 4 letters")
        toevoegen_code = input("Voer een bedrijfscode in ")

    toevoegen_naam = input("Voer de naam in van het bedrijf ")

    toevoegen_straat = input("Voer de straat van het bedrijf ")

    while True:
        try:
            print('open')    
            toevoegen_huisnr = int(input("Voer het huisnummer in "))
            break 
        except ValueError:
            print("Voer een getal in en geen letters ") 
            continue

    toevoegen_postcode_getallen = input("Voer de getallen van de postcode is ")
    while len(toevoegen_postcode_getallen) != 4 :
        print("De code die u opvoerde is te lang of te kort of niet numeriek. Voor een nummer is met 4 getallen")
        toevoegen_postcode_getallen = input("Voer de getallen van de postcode is ")
        if toevoegen_postcode_getallen == "Stop": 
            break

    toevoegen_postcode_letters = input("Voer de letters van de postcode in ")
    while len(toevoegen_postcode_letters) != 2 and not toevoegen_postcode_letters.isalpha(): 
        print("De letters die u opgaf zijn of geen letters of groter of korter dan 2 letter. Vul aub 2 letters in")
        toevoegen_postcode_letters = input("Voer de letters van de postcode in ")
        if toevoegen_postcode_getallen == "Stop": 
            break

    toevoegen_plaats = input("Voer de plaats in van het bedrijf ")

    while True:
        try:
            print('open')    
            toevoegen_xwaarde = int(input("Voer de Xwaarde in "))
            break 
        except ValueError:
            print("Voer een getal in van de Xwaarde ") 
            continue


    while True:
        try:
            print('open')    
            toevoegen_ywaarde = int(input("Voer de Ywaarde in "))
            break 
        except ValueError:
            print("Voer een getal in van de Ywaarde ") 
            continue


    while True:
        try:
            print('open')    
            toevoegen_maxuitst = int(input("Voer de Maxuitst in "))
            break 
        except ValueError:
            print("Voer een getal in voor de Maxuitst ") 
            continue


    toevoegen_controle = input("Voer in of er controle is uitgevoerd ")

    while True:
        try:
            print('open')    
            toevoegen_freq = int(input("Voer de frequentie in "))
            break 
        except ValueError:
            print("Voer een getal in voor de frequentie ") 
            continue

    toevoegen_Ctpers = input("Voer de inspecteur in ")

    # Toevoegen van data aan dataset 
    bedrijven_leeg.at[0, "Code"] = toevoegen_postcode_getallen
    bedrijven_leeg.at[0, "Naam"] = toevoegen_naam
    bedrijven_leeg.at[0, "Straat"] = toevoegen_straat
    bedrijven_leeg.at[0, "Huisnr"] = toevoegen_huisnr
    bedrijven_leeg.at[0, "Postcd"] = toevoegen_postcode_getallen + toevoegen_postcode_letters
    bedrijven_leeg.at[0, "Plaats"] = toevoegen_plaats
    bedrijven_leeg.at[0, "Xwaarde"] = toevoegen_xwaarde
    bedrijven_leeg.at[0, "Ywaarde"] = toevoegen_ywaarde
    bedrijven_leeg.at[0, "Maxuitst"] = toevoegen_maxuitst
    bedrijven_leeg.at[0, "Controle"] = toevoegen_controle
    bedrijven_leeg.at[0, "Freq"] = toevoegen_freq
    bedrijven_leeg.at[0, "Ctpers"] = toevoegen_Ctpers

    print(bedrijven_leeg)

    # Samenvoegen nieuwe regel aan bestaande dataset
    bedrijven_test = pd.concat([bedrijven, bedrijven_leeg], ignore_index=True, sort=False)
    print(bedrijven_test)
    return bedrijven_test 
        
    
bedrijven = Bedrijven.lees_bedrijven()
Bedrijven.toon_bedrijven()
Bedrijven.zoek_bedrijven_naam()
Bedrijven.zoek_bedrijven_locatie()






















