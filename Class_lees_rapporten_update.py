import os
import pandas as pd

class RapportenDataReader:
    def __init__(self):
        self.update_file2 = "rapporten_update2.txt"
        self.update_file = "rapporten_update.txt" 
        self.default_file = "rapporten.txt"

    '''Omdat het format van een bewaard bestand kan verschillen met de verkregen raporten txt bestand is het noodzakelijk om een andere methode te implenteren'''
    '''Er wordt gekeken naar de working directory, als het update bestand daar aanwezig is wordt deze ingeladen. Anders wordt het originele bestand ingeladen'''
    def lees_rapporten_data(self):
        if os.path.exists(self.update_file2):
            kolommen = ["Icode", "Bcode", "Bezdat", "Rapdat", "Status", "Opm"]
            kolomtypes = {"Icode": str, "Bcode": str, "Bezdat": str, "Rapdat": str, "Status": str, "Opm": str}
            rapporten = df = pd.read_csv(self.update_file2, sep='\t', names = kolommen, dtype = kolomtypes, parse_dates = ["Bezdat", "Rapdat"], header = 0)
        elif os.path.exists(self.update_file): 
            rapporten = pd.read_fwf(self.update_file, names=["Icode", 
                                     "Bcode", 
                                     "Bezdat", 
                                     "Rapdat", 
                                     "Status", 
                                     "Opm"])
        else: 
            colspecs = [(0,3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]
            
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


