import pandas as pd

class BedrijvenDataReader:
    """
    Class voor het inlezen van bedrijven data.
    """

    def __init__(self, default_file="bedrijven.txt"):
        """
        Het default bestand zetten op bedrijven.txt
        """
        self.default_file = default_file

    def lees_bedrijven_data(self):
        """
        Data inlezen van het bedrijvenbestand. 
        """
        try:
            column_names = ["Code", "Naam", "Straat", "Huisnr", "Postcd", "Plaats", "Xwaarde", "Ywaarde", "Maxuitst", "Beruitst", "Boete", "Controle", "Freq", "Ctpers"]
            column_types = {"Code": str, "Naam": str, "Straat": str, "Huisnr": str, "Postcd": str, "Plaats": str, "Xwaarde": int, "Ywaarde": int, "Maxuitst": int, "Beruitst": float, "Boete": float, "Controle": str, "Freq": float, "Ctpers": str}
            bedrijven = pd.read_csv(self.default_file, sep='\t', names=column_names, dtype=column_types, header=0)
        except FileNotFoundError as e:
            print(f"Error: Bestand '{self.default_file}' niet gevonden.")
        except Exception as e:
            #print(f"An error occurred while reading the file: {e}")
            #print("Reading the default file instead.")
            try:
                colspecs = [(0, 4), (4, 24), (24, 54), (54, 59), (59, 65), (65, 85), (85, 87), (87, 89), (89, 99), (99, 109), (109, 117), 
                            (117, 118), (118, 120), (120, 140)]
                bedrijven = pd.read_fwf(self.default_file, header=None, colspecs=colspecs,
                                        names=column_names, dtype=column_types)
            except Exception as e:
                print("Het bestand is corrupt. Zorg voor een structuur van de data die overeenkomt met het origineel")
        return bedrijven
