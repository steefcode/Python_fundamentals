import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')  # Use Qt5Agg backend
import matplotlib.pyplot as plt

class HeatmapGassen:
    def __init__(self, df):
        self.df = df

    def create_heatmap(self, x_waarde, y_waarde, col_gas, aggregation_func=np.mean):
        """
        Based on aggregation, create a heatmap for x_waarde, y_waarde, and a selected gas that occurs in the gas file.
        """

        # Pivot the DataFrame
        pivot_table = pd.pivot_table(self.df, values=col_gas, index=y_waarde, columns=x_waarde, aggfunc=aggregation_func)

        # Create heatmap
        plt.figure(figsize=(10, 8))
        plt.title(f"Heatmap van {col_gas}")
        plt.xlabel(x_waarde)
        plt.ylabel(y_waarde)
        heatmap = plt.imshow(pivot_table, cmap='viridis', interpolation='nearest')
        plt.colorbar(heatmap, label=col_gas)
        
        # Dynamically set x-axis ticks
        num_x_ticks = len(pivot_table.columns)
        x_ticks = np.arange(0, num_x_ticks, 10)
        plt.xticks(x_ticks, pivot_table.columns[x_ticks])
        
        # Dynamically set y-axis ticks
        num_y_ticks = len(pivot_table.index)
        y_ticks = np.arange(0, num_y_ticks, 10)
        plt.yticks(y_ticks, pivot_table.index[y_ticks])
        
        # Reverse the order of y-axis labels
        plt.gca().invert_yaxis()
        
        plt.show()
