import telebot

from Parser import Parser

bot = telebot.TeleBot('1805652371:AAH3fV6tl1UEteSjKdYqf788j6KNpk_5vZk')
parser = Parser()


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
    print(parser.get_city())
    print(parser.get_currency())

    bot.send_message(message.chat.id, "#TODO")


bot.polling()
