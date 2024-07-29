import pandas as pd

class AntiJoinAndSort:
    def __init__(self, bedrijven_data, gassen_data):
        self.bedrijven = pd.DataFrame(bedrijven_data)
        self.gassen = pd.DataFrame(gassen_data)
        self.joined_data = None
        self.sorted_data = None

    def perform_anti_join(self):
        """
        Het uitvoeren van een anti join om op basis van het gassen bestand de bedrijven die al bekend zijn te filteren. Zo zijn alleen x en y coordinaten zichtbaar
        en is dus zichtbaar welke coordinaten onbekend zijn als bedrijf zijnde. 
        """
        self.joined_data = pd.merge(self.bedrijven, self.gassen, left_on=['Xwaarde','Ywaarde'], right_on=['x-waarde','y-waarde'], how='outer', indicator=True)
        self.filtered_data = self.joined_data[self.joined_data['_merge'] == 'right_only']
        self.filtered_data = self.filtered_data[['x-waarde','y-waarde','CO2','CH4', 'NO2', 'NH3', 'tot_uitstoot']]

    def sort_data(self, user_input):
        """
        De gefilterde dataset wordt op basis van user input gesorteerd naar een gas naar keuze. 
        """

        if user_input == 'CO2':
            self.sorted_data = self.filtered_data.sort_values(by='CO2', ascending=False)
        elif user_input == 'CH4':
            self.sorted_data = self.filtered_data.sort_values(by='CH4', ascending=False)
        elif user_input == 'NO2': 
            self.sorted_data = self.filtered_data.sort_values(by='NO2', ascending=False)
        elif user_input == 'NH3': 
            self.sorted_data = self.filtered_data.sort_values(by='NH3', ascending=False)
        elif user_input == 'tot_uitstoot':
            self.sorted_data = self.filtered_data.sort_values(by='tot_uitstoot', ascending=False)
        else:
            print("Vul een geldige naam in CO2, CH4, NO2, NH3 of tot_uitstoot")


