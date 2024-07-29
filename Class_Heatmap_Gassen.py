import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')  # Gebruiken van Qt5Agg backend om plot weer te kunnen geven in een Linux omgeving
import matplotlib.pyplot as plt

class HeatmapGassen:
    def __init__(self, df):
        self.df = df

    def create_heatmap(self, x_waarde, y_waarde, col_gas, aggregation_func=np.mean):
        """
        Op basis van een aggregatie een heatmap maken van de x en y waarde en een gas gekozen door de gebruiker. 
        """

        # Pivot van de pandas dataFrame
        pivot_table = pd.pivot_table(self.df, values=col_gas, index=y_waarde, columns=x_waarde, aggfunc="mean")

        # Aanmaken heatmap
        plt.figure(figsize=(10, 8))
        plt.title(f"Heatmap van {col_gas}")
        plt.xlabel(x_waarde)
        plt.ylabel(y_waarde)
        heatmap = plt.imshow(pivot_table, cmap='viridis', interpolation='nearest')
        plt.colorbar(heatmap, label=col_gas)
        
        # Dynamisch weergeven van de x as 
        num_x_ticks = len(pivot_table.columns)
        x_ticks = np.arange(0, num_x_ticks, 10)
        plt.xticks(x_ticks, pivot_table.columns[x_ticks])
        
        # Dynamisch weergeven van de y as
        num_y_ticks = len(pivot_table.index)
        y_ticks = np.arange(0, num_y_ticks, 10)
        plt.yticks(y_ticks, pivot_table.index[y_ticks])
        
        # Omdraaien van de y as zodat de coordinaten met de laagste waarde ook onderin de grafiek staan. 
        plt.gca().invert_yaxis()
        
        plt.show()
