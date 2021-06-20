import telebot

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
    city = parser.get_city()
    date = parser.get_date()
    month = parser.get_month()
    year = parser.get_year()
    if currency is not None and date is not None and month is not None and year is not None:
        price = curr_parser.get_curr(currency, date, month, year)
        bot.send_message(message.chat.id, date + "." + month + "." + year + " курс валюты " \
                         + currency.upper() + " был " + str(price) + " RUB")

    if city is not None and currency is not None:
        bot.send_message(message.chat.id, "#TODO")


bot.polling()
