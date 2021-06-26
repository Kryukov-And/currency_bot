import urllib.request
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import pandas


class CurrenciesParser:
    def get_curr_date(self, currency, date, month, year):
        url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + date + "." + month + "." + year
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
        currency_data = soup.find("charcode", text=currency.upper()).parent
        curr = float(currency_data.find("value").get_text().replace(",", "."))
        return curr

    def get_curr_city(self, currency, city):
        url = "https://www.banki.ru/products/currency/cash/" + currency + "/" + city + "/#bank-rates"
        options = webdriver.ChromeOptions()
        options.binary_location = "D:\Program Files\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        driver.close()
        if soup.select("div[class='notice-popup']"):
            return None

        rows = soup.select("tr[data-test='bank-rates-row']")
        bank = []
        buy = []
        sell = []
        for row in rows:
            bank.append(row.find("a").get_text())
            buy.append(float(row.find_all("td")[1].get_text().replace("\n", "").replace("\t", "").replace(",", ".")))
            sell.append(float(row.find_all("td")[2].get_text().replace("\n", "").replace("\t", "").replace(",", ".")))
        data = pandas.DataFrame(list(zip(bank, buy, sell)), columns=["bank", "buy", "sell"])
        return data
