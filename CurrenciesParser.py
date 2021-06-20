import urllib.request
from bs4 import BeautifulSoup


class CurrenciesParser:
    def get_curr(self, currency, date, month, year):
        url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + date + "." + month + "." + year
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
        currency_data = soup.find("charcode", text=currency.upper()).parent
        curr = float(currency_data.find("value").get_text().replace(",", "."))
        return curr
