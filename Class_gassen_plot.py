from Class_gassen import Gassen 
import pandas as pd 
import numpy as np 
from tabulate import tabulate   
import matplotlib.pyplot as plt 
import seaborn as sns

gassen = Gassen.lees_gassen()
print(gassen)   

class Gassen_plot: 
         def plot_gassen():
              keuze_gas = input("Kies welk gas u wilt zien ")
              while keuze_gas not in gassen.columns:
                   print(f"Uw invoer is geen geldide keuze deze gassen komen voor {gassen.columns[2:]}")
                   keuze_gas = input("Kies welk gas u wilt zien ")
              else: 
                   select_gas = gassen[["y-waarde", "x-waarde", keuze_gas]]
                   plot_gas = select_gas.pivot(index="y-waarde", columns="x-waarde", values= keuze_gas)
                   sns.heatmap(plot_gas, cmap='coolwarm', square=True)
                   plt.title(keuze_gas)
                   plt.show() 

Gassen_plot.plot_gassen() 

print(gassen)


# Assuming you already have a pandas DataFrame called 'df'
# with columns x_waarde, y_waarde, CO2, CH4, NO2, NH3

# Create an instance of HeatmapGenerator with your DataFrame
heatmap_gen = HeatmapGenerator(df)

# Create a heatmap for the 'CO2' column
heatmap_gen.create_heatmap("CO2")

