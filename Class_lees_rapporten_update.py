import pandas as pd

class RapportenDataReader:
    """
    Class voor het inlezen van rapporten data.
    """

    def __init__(self, default_file="rapporten.txt"):
        """
        Het default bestand zetten op rapporten.txt
        """
        self.default_file = default_file

    def lees_rapporten_data(self):
        """
        Data inlezen van het rapportenbestand. 
        """
        try:
            column_names = ["Icode", "Bcode", "Bezdat", "Rapdat", "Status", "Opm"]
            column_types = {"Icode": str, "Bcode": str, "Bezdat": str, "Rapdat": str, "Status": str, "Opm": str}
            rapporten = pd.read_csv(self.default_file, sep='\t', names=column_names, dtype=column_types, parse_dates=["Bezdat", "Rapdat"], header=0)
        except FileNotFoundError as e:
            print(f"Error: Bestand '{self.default_file}' niet gevonden.")
        except Exception as e:
            #print(f"An error occurred while reading the file: {e}")
            #print("Reading the default file instead.")
            try:
                colspecs = [(0, 3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]
                rapporten = pd.read_fwf(self.default_file, header=None, colspecs=colspecs, names=column_names, dtype=column_types, parse_dates=["Bezdat", "Rapdat"])
            except Exception as e:
                print("Het bestand is corrupt. Zorg voor een structuur van de data die overeenkomt met het origineel")
        return rapporten

