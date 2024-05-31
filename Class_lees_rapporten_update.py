# import os
# import pandas as pd

# class RapportenDataReader:
#     def __init__(self):
#         self.update_file2 = "rapporten_update2.txt"
#         self.update_file = "rapporten_update.txt" 
#         self.default_file = "rapporten.txt"

#     '''Omdat het format van een bewaard bestand kan verschillen met de verkregen raporten txt bestand is het noodzakelijk om een andere methode te implenteren'''
#     '''Er wordt gekeken naar de working directory, als het update bestand daar aanwezig is wordt deze ingeladen. Anders wordt het originele bestand ingeladen'''
#     def lees_rapporten_data(self):
#         if os.path.exists(self.update_file2):
#             kolommen = ["Icode", "Bcode", "Bezdat", "Rapdat", "Status", "Opm"]
#             kolomtypes = {"Icode": str, "Bcode": str, "Bezdat": str, "Rapdat": str, "Status": str, "Opm": str}
#             rapporten = df = pd.read_csv(self.update_file2, sep='\t', names = kolommen, dtype = kolomtypes, parse_dates = ["Bezdat", "Rapdat"], header = 0)
#         elif os.path.exists(self.update_file): 
#             rapporten = pd.read_fwf(self.update_file, names=["Icode", 
#                                      "Bcode", 
#                                      "Bezdat", 
#                                      "Rapdat", 
#                                      "Status", 
#                                      "Opm"])
#         else: 
#             colspecs = [(0,3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]
            
#             rapporten = pd.read_fwf("rapporten.txt", header = None, colspecs = colspecs, 
#                             names = ["Icode", 
#                                      "Bcode", 
#                                      "Bezdat", 
#                                      "Rapdat", 
#                                      "Status", 
#                                      "Opm"], 
#                             dtype = {"Icode" : str, 
#                                     "Bcode" : str, 
#                                     "Bezdat" : str, 
#                                     "Rapdat" : str, 
#                                     "Status" : str,
#                                     "Opm" : str}, 
#                             parse_dates = ["Bezdat", "Rapdat"])
         
#         return rapporten


# import pandas as pd

# class RapportenDataReader:
#     """
#     Class to read data about companies from a file.
#     """
#     def __init__(self, default_file="rapporten.txt"):
#         """
#         Initialize the RapportenDataReader with a default file.
        
#         Parameters:
#         - default_file (str): Path to the default file.
#         """
#         self.default_file = default_file

#     def lees_rapporten_data(self):
#         """
#         Read data about companies from a file.
        
#         Returns:
#         - DataFrame: A DataFrame containing company data.
#         """
#         try:
#             column_names = ["Icode", "Bcode", "Bezdat", "Rapdat", "Status", "Opm"]
#             column_types = {"Icode": str, "Bcode": str, "Bezdat": str, "Rapdat": str, "Status": str, "Opm": str}
#             rapporten = pd.read_csv(self.default_file, sep='\t', names=column_names, dtype=column_types, parse_dates=["Bezdat", "Rapdat"], header=0)
#         except FileNotFoundError as e:
#             print(f"Error: File '{self.default_file}' not found.")
#             return None
#         except Exception as e:
#             print(f"An error occurred while reading the file: {e}")
#             print("Reading the default file instead.")
#             colspecs = [(0, 3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]
#             rapporten = pd.read_fwf(self.default_file, header=None, colspecs=colspecs, names=column_names, dtype=column_types, parse_dates=["Bezdat", "Rapdat"])
#         return rapporten

import pandas as pd

class RapportenDataReader:
    """
    Class to read data about reports from a file.
    """

    def __init__(self, default_file="rapporten.txt"):
        """
        Initialize the RapportenDataReader with a default file.
        
        Parameters:
        - default_file (str): Path to the default file.
        """
        self.default_file = default_file

    def lees_rapporten_data(self):
        """
        Read data about reports from a file.
        
        Returns:
        - DataFrame: A DataFrame containing report data.
        """
        try:
            column_names = ["Icode", "Bcode", "Bezdat", "Rapdat", "Status", "Opm"]
            column_types = {"Icode": str, "Bcode": str, "Bezdat": str, "Rapdat": str, "Status": str, "Opm": str}
            rapporten = pd.read_csv(self.default_file, sep='\t', names=column_names, dtype=column_types, parse_dates=["Bezdat", "Rapdat"], header=0)
        except FileNotFoundError as e:
            print(f"Error: File '{self.default_file}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            print("Reading the default file instead.")
            try:
                colspecs = [(0, 3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]
                rapporten = pd.read_fwf(self.default_file, header=None, colspecs=colspecs, names=column_names, dtype=column_types, parse_dates=["Bezdat", "Rapdat"])
            except Exception as e:
                print("The file is corrupt. Please ensure it is a valid file.")
        return rapporten

