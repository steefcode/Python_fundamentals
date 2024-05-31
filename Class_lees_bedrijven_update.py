# import os
# import pandas as pd

# class BedrijvenDataReader:
#     def __init__(self):
#         self.update_file2 = "bedrijven_update2.txt"   
#         self.update_file = "bedrijven_update.txt" 
#         self.default_file = "bedrijven.txt"

#     '''Omdat het format van een bewaard bestand kan verschillen met de verkregen bedrijven txt bestand is het noodzakelijk om een andere methode te implenteren'''
#     '''Er wordt gekeken naar de working directory, als het update daar aanwezig is wordt deze ingeladen. Anders wordt het originele bestand ingeladen'''
#     def lees_bedrijven_data(self):
#         if os.path.exists(self.update_file2): 
#             column_names = ["Code", "Naam", "Straat", "Huisnr", "Postcd", "Plaats", "Xwaarde", "Ywaarde", "Maxuitst", "Beruitst", "Boete", "Controle", "Freq", "Ctpers"]
#             column_types = {"Code": str, "Naam": str, "Straat": str, "Huisnr": str, "Postcd": str, "Plaats": str, "Xwaarde": int, "Ywaarde": int, "Maxuitst": int, "Beruitst": float, "Boete": float, "Controle": str, "Freq": float, "Ctpers": str}
#             bedrijven = pd.read_csv(self.update_file2, sep='\t', names=column_names, dtype=column_types, header = 0)
#         else: 
#             colspecs = [(0, 4), (4, 24), (24, 54), (54, 59), (59, 65), (65, 85), (85, 87), (87, 89), (89, 99), (99, 109), (109, 117), 
#                         (117, 118), (118, 120), (120, 140)]
            
#             bedrijven = pd.read_fwf("bedrijven.txt", header=None, colspecs=colspecs,
#                                 names=["Code", 
#                                        "Naam", 
#                                        "Straat", 
#                                        "Huisnr", 
#                                        "Postcd", 
#                                        "Plaats", 
#                                        "Xwaarde", 
#                                        "Ywaarde", 
#                                        "Maxuitst", 
#                                        "Beruitst", 
#                                        "Boete", 
#                                        "Controle", 
#                                        "Freq", 
#                                        "Ctpers"], 
#                                 dtype={"Code": str, 
#                                        "Naam": str, 
#                                        "Straat": str, 
#                                        "Huisnr": str, 
#                                        "Postcd": str, 
#                                        "Plaats": str, 
#                                        "Xwaarde": int, 
#                                        "Ywaarde": int, 
#                                        "Maxuitst": int, 
#                                        "Beruitst": float, 
#                                        "Boete": float, 
#                                        "Controle": str, 
#                                        "Freq": float,  
#                                        "Ctpers": str})
         
#         return bedrijven

# # Usage
# # reader = BedrijvenDataReader()
# # data = reader.lees_bedrijven_data()

# # # Now you can use the 'data' DataFrame as needed
# # print(data)

# import pandas as pd

# class BedrijvenDataReader:
#     """
#     Class to read data about companies from a file.
#     """
#     def __init__(self, default_file="bedrijven.txt"):
#         """
#         Initialize the BedrijvenDataReader with a default file.
        
#         Parameters:
#         - default_file (str): Path to the default file.
#         """
#         self.default_file = default_file

#     def lees_bedrijven_data(self):
#         """
#         Read data about companies from a file.
        
#         Returns:
#         - DataFrame: A DataFrame containing company data.
#         """
#         try:
#             column_names = ["Code", "Naam", "Straat", "Huisnr", "Postcd", "Plaats", "Xwaarde", "Ywaarde", "Maxuitst", "Beruitst", "Boete", "Controle", "Freq", "Ctpers"]
#             column_types = {"Code": str, "Naam": str, "Straat": str, "Huisnr": str, "Postcd": str, "Plaats": str, "Xwaarde": int, "Ywaarde": int, "Maxuitst": int, "Beruitst": float, "Boete": float, "Controle": str, "Freq": float, "Ctpers": str}
#             bedrijven = pd.read_csv(self.default_file, sep='\t', names=column_names, dtype=column_types, header=0)
#         except FileNotFoundError as e:
#             print(f"Error: File '{self.default_file}' not found.")
#             return None
#         except Exception as e:
#             print(f"An error occurred while reading the file: {e}")
#             print("Reading the default file instead.")
#             colspecs = [(0, 4), (4, 24), (24, 54), (54, 59), (59, 65), (65, 85), (85, 87), (87, 89), (89, 99), (99, 109), (109, 117), 
#                         (117, 118), (118, 120), (120, 140)]
#             bedrijven = pd.read_fwf(self.default_file, header=None, colspecs=colspecs,
#                                     names=column_names, dtype=column_types)
#         return bedrijven

import pandas as pd

class BedrijvenDataReader:
    """
    Class to read data about companies from a file.
    """

    def __init__(self, default_file="bedrijven.txt"):
        """
        Initialize the BedrijvenDataReader with a default file.
        
        Parameters:
        - default_file (str): Path to the default file.
        """
        self.default_file = default_file

    def lees_bedrijven_data(self):
        """
        Read data about companies from a file.
        
        Returns:
        - DataFrame: A DataFrame containing company data.
        """
        try:
            column_names = ["Code", "Naam", "Straat", "Huisnr", "Postcd", "Plaats", "Xwaarde", "Ywaarde", "Maxuitst", "Beruitst", "Boete", "Controle", "Freq", "Ctpers"]
            column_types = {"Code": str, "Naam": str, "Straat": str, "Huisnr": str, "Postcd": str, "Plaats": str, "Xwaarde": int, "Ywaarde": int, "Maxuitst": int, "Beruitst": float, "Boete": float, "Controle": str, "Freq": float, "Ctpers": str}
            bedrijven = pd.read_csv(self.default_file, sep='\t', names=column_names, dtype=column_types, header=0)
        except FileNotFoundError as e:
            print(f"Error: File '{self.default_file}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            print("Reading the default file instead.")
            try:
                colspecs = [(0, 4), (4, 24), (24, 54), (54, 59), (59, 65), (65, 85), (85, 87), (87, 89), (89, 99), (99, 109), (109, 117), 
                            (117, 118), (118, 120), (120, 140)]
                bedrijven = pd.read_fwf(self.default_file, header=None, colspecs=colspecs,
                                        names=column_names, dtype=column_types)
            except Exception as e:
                print("The file is corrupt. Please ensure it is a valid file.")
        return bedrijven
