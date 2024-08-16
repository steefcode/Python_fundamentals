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
            
            # Use parse_dates to automatically parse date columns
            parse_dates = ["Bezdat", "Rapdat"]
            date_parser = lambda x: pd.to_datetime(x, format='%Y%m%d', errors='coerce')

            rapporten = pd.read_csv(self.default_file, sep='\t', names=column_names, dtype=column_types, 
                                     header=0)
            rapporten['Bezdat'] = pd.to_datetime(rapporten['Bezdat'], format='%Y-%m-%d')
            rapporten['Rapdat'] = pd.to_datetime(rapporten['Rapdat'], format='%Y-%m-%d')
        except FileNotFoundError as e:
            print(f"Error: Bestand '{self.default_file}' niet gevonden.")
            return None
        except Exception as e:
            try:
                colspecs = [(0, 3), (3, 7), (7, 15), (15, 23), (23, 24), (24, 124)]
                
                rapporten = pd.read_fwf(self.default_file, header=None, colspecs=colspecs, names=column_names, 
                                        dtype=column_types, parse_dates=parse_dates, date_parser=date_parser)
            except Exception as e:
                print("Het bestand is corrupt. Zorg voor een structuur van de data die overeenkomt met het origineel")
                return None
        
        return rapporten
