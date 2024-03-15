# Importeren van benodigde bibliotheken  
import pandas as pd 
import numpy as np 
from tabulate import tabulate
from datetime import date, datetime
from Class_gassen import Gassen  

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