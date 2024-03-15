# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# class HeatmapGassen:
#     def __init__(self, dataframe):
#         self.dataframe = dataframe

#     def create_heatmap(self, column_name):
#         '''Extra beveiliging dat als er een kolom wordt gekozen die niet in de dataframe is dat dit zichtbaar wordt gemaakt voor de gebruiker'''
#         if column_name not in self.dataframe.columns:
#             raise ValueError(f"'{column_name}' column not found in the DataFrame.")

#         '''' Pivot van de dataframe zodat deze compatible is om een heatmap van te maken.'''
#         heatmap_data = self.dataframe.pivot("y-waarde", "x-waarde", column_name)

#         '''Eigenschappen van de heatmap samenstellen'''
#         plt.figure(figsize=(10, 8))
#         sns.heatmap(heatmap_data, cmap='coolwarm', square=True, cbar_kws={'label': column_name})
#         plt.xlabel("x-waarde")
#         plt.ylabel("y-waarde")
#         plt.title(f"Heatmap of {column_name}")
#         plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class HeatmapGassen:
    def __init__(self, df):
        self.df = df

    def create_heatmap(self, x_waarde, y_waarde, col_gas, aggregation_func=np.mean):
        """
        Op basis van aggregatie een heatmap maken voor x_waarde, y_waarde en een geselecteerde gas die voorkomt in het gassen 
        bestand
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
        plt.xticks(np.arange(len(pivot_table.columns)), pivot_table.columns)
        plt.yticks(np.arange(len(pivot_table.index)), pivot_table.index)
        plt.show()





