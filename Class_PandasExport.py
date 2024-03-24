# import pandas as pd

# class PandasExporter:
#     def __init__(self, dataframe):
#         self.dataframe = dataframe

#     def export_to_txt(self, file_path):
#         # Pandas dataframe omzetten naar een string
#         df_string = self.dataframe.to_string(index=False, header = False)  # Verwijderen van headers en index rijen 

#         # De regels van de dataframe string wegschrijven in een txt bestand
#         with open(file_path, 'w') as file:
#             file.writelines(df_string)

#         print(f"De gegevens zijn opgeslagen")


import pandas as pd

class PandasExporter:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def export_to_txt(self, file_path):
        # Convert DataFrame to tab-separated string
        df_string = self.dataframe.to_csv(index=False, sep='\t')

        # Write the string to a txt file
        with open(file_path, 'w') as file:
            file.write(df_string)

        print(f"The data has been saved to {file_path}")




# import pandas as pd

# class PandasExporter:
#     def __init__(self, dataframe):
#         self.dataframe = dataframe

#     def export_to_txt(self, file_path):
#         # Convert DataFrame to formatted string
#         df_string = self.dataframe.apply(lambda row: f"{row['Code']:04}{row['Naam']:30}{row['Straat']:30}{row['Huisnr']:5}{row['Postcd']:25}{row['Phone']:20}{row['Contact']:25}\n", axis=1)

#         # Write the string to a txt file
#         with open(file_path, 'w') as file:
#             file.writelines(df_string)

#         print(f"The data has been saved to {file_path}")

# Example usage:
# Assuming df is your DataFrame
# df = pd.DataFrame(...)
# exporter = PandasExporter(df)
# exporter.export_to_txt("output.txt")






# Example usage:
# Assuming df is your DataFrame
# df = pd.DataFrame(...)
# exporter = PandasExporter(df)
# exporter.export_to_txt("output.txt")
