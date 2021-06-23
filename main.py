import telebot
import pandas

from Parser import Parser
from CurrenciesParser import CurrenciesParser

bot = telebot.TeleBot('1805652371:AAH3fV6tl1UEteSjKdYqf788j6KNpk_5vZk')
parser = Parser()
curr_parser = CurrenciesParser()


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Здравствуйте! Данный бот показывает информацию по курсам валют")
    bot.send_message(message.chat.id, "Поддерживаемые валюты: USD, EUR, GBP, CNY, JPY")
    bot.send_message(message.chat.id,
                     "Возможности:\n"
                     "Показать курсы в нескольких банках регионов\n"
                     "Узнать курс ЦБ валюты по дате\n"
                     "Также поддерживается возможность добавить бота в группу\n")


@bot.message_handler()
def handle_any_message(message):
    parser.parse_message(message)
    currency = parser.get_currency()
    city_name = parser.get_city_name()
    city_url = parser.get_city_url()
    date = parser.get_date()
    month = parser.get_month()
    year = parser.get_year()
    if currency is not None and date is not None and month is not None and year is not None:
        price = curr_parser.get_curr_date(currency, date, month, year)
        bot.send_message(message.chat.id, date + "." + month + "." + year + " курс валюты " \
                         + currency.upper() + " был " + str(price) + " RUB")

    if city_name is not None and currency is not None:
        prices = curr_parser.get_curr_city(currency, city_url)
        if prices is None:
            bot.send_message(message.chat.id, "По данному городу и валюте информация не найдена")
        else:
            best_buy = prices.sort_values(by="buy", ascending=False).iloc[:3].reset_index()
            best_sell = prices.sort_values(by="sell").iloc[:3].reset_index()

            msg = "Лучшие цены для " + currency.upper() + " в городе " + city_name + "\n" + "\n"
            msg += "Банк покупает у Вас:" + "\n"
            for i in range(best_buy.shape[0]):
                msg += "По " + str(best_buy.iloc[i]["buy"]) + " в " + best_buy.iloc[i]["bank"] + "\n"
            msg += "\n" + "Банк продает Вам:" + "\n"
            for i in range(best_sell.shape[0]):
                msg += "По " + str(best_sell.iloc[i]["sell"]) + " в " + best_sell.loc[i]["bank"] + "\n"

            bot.send_message(message.chat.id, msg)


bot.polling()
