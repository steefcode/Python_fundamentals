import pandas as pd

from Class_lees_rapporten_update import RapportenDataReader 

reader_rapporten = RapportenDataReader()
rapporten = reader_rapporten.lees_rapporten_data()

class DataSubsetter:
    def __init__(self, data):
        self.data = data

    def subset_by_column(self, column_name, value):
        subsetted_data = self.data[self.data[column_name] == value]
        return subsetted_data


subsetter = DataSubsetter(rapporten)

