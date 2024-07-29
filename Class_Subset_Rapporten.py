import pandas as pd

class Subset_Rapporten:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def subset_icode(self, icode):
        subset = self.dataframe[self.dataframe["Icode"] == icode]
        return subset
    
    def subset_bcode(self, bcode):
        subset = self.dataframe[self.dataframe["Bcode"] == bcode]
        return subset


