import pandas


class Parser:
    cities_data = pandas.read_csv('cities.csv')
    currencies_data = pandas.read_csv("currencies.csv")
    city_name = None
    currency = None

    def parse_message(self, message):
        message = message.text.lower()
        self.parse_city(message)
        self.parse_currency(message)

    def parse_city(self, message):
        for i, curr in enumerate(self.cities_data['city_part']):
            if message.find(curr) != -1:
                self.city_name = self.cities_data.iloc[i]['city_name']
                break

    def parse_currency(self, message):
        for i, curr in enumerate(self.currencies_data['val_alias']):
            if message.find(curr) != -1:
                self.currency = self.currencies_data.iloc[i]['val_name']
                break

    def get_city(self):
        return self.city_name

    def get_currency(self):
        return self.currency
