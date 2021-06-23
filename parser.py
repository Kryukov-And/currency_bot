import pandas


class Parser:
    cities_data = pandas.read_csv("cities.csv")
    currencies_data = pandas.read_csv("currencies.csv")
    dates_data = pandas.read_csv("dates.csv")
    months_data = pandas.read_csv("months.scv")
    years_data = pandas.read_csv("years.csv")

    city_name = None
    city_url = None
    currency = None
    date = None
    month = None
    year = None

    def parse_message(self, message):
        self.clear()
        message = message.text.lower()
        message = "*-+" + message + "\n"

        self.parse_city(message)
        self.parse_currency(message)
        self.parse_date(repr(message))
        self.parse_month(repr(message))
        self.parse_year(repr(message))

    def parse_city(self, message):
        for i, curr in enumerate(self.cities_data["city_alias"]):
            if message.find(curr) != -1:
                self.city_name = self.cities_data.iloc[i]["city_name"]
                self.city_url = self.cities_data.iloc[i]["city_url"]
                break

    def parse_currency(self, message):
        for i, curr in enumerate(self.currencies_data["val_alias"]):
            if message.find(curr) != -1:
                self.currency = self.currencies_data.iloc[i]["val_name"]
                break

    def parse_date(self, message):
        for i, curr in enumerate(self.dates_data["date_alias"]):
            if message.find(curr) != -1:
                if self.dates_data.iloc[i]["date_name"] < 10:
                    self.date = "0" + str(self.dates_data.iloc[i]["date_name"])
                else:
                    self.date = str(self.dates_data.iloc[i]["date_name"])
                break

    def parse_month(self, message):
        for i, curr in enumerate(self.months_data["month_alias"]):
            if message.find(curr) != -1:
                if self.months_data.iloc[i]["month_name"] < 10:
                    self.month = "0" + str(self.months_data.iloc[i]["month_name"])
                else:
                    self.month = str(self.months_data.iloc[i]["month_name"])
                break

    def parse_year(self, message):
        for i, curr in enumerate(self.years_data["year_alias"]):
            if message.find(curr) != -1:
                self.year = str(self.years_data.iloc[i]["year_name"])
                break

    def get_city_name(self):
        return self.city_name

    def get_city_url(self):
        return self.city_url

    def get_currency(self):
        return self.currency

    def get_date(self):
        return self.date

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def clear(self):
        self.currency = None
        self.city_name = None
        self.city_url = None
        self.date = None
        self.month = None
        self.year = None
