# Importeren van benodigde bibliotheken  
import pandas as pd 
import numpy as np 
from tabulate import tabulate
from datetime import date, datetime

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