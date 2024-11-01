import telebot
import requests

# Класс для обработки ошибок
class APIException(Exception):
    def __init__(self, message):
        self.message = message

# Статический метод для отправки запросов к API и получения цены валюты
class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        url = f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}'
        response = requests.get(url)
        data = response.json()
        if "error" in data:
            raise APIException("Неверно указаны валюты")
        if quote not in data['rates']:
            raise APIException("Неверно указаны валюты")
        price = float(data['rates'][quote]) * float(amount)
        return price

# Создание бота
bot = telebot.TeleBot("5745310177:AAHfeVWjrYduNeCml3pwp12L8Zjwhh7FN0Y")

# Функции обработки команд
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Введите запрос в формате: <имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>")

@bot.message_handler(commands=['values'])
def handle_values(message):
    bot.send_message(message.chat.id, "Доступные валюты: USD, EUR, RUB")

# Функция для обработки текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        values = message.text.split(' ')

        # Проверка на количество параметров
        if len(values) != 3:
            raise APIException("Неверное количество параметров")

        # Получение цены валюты и отправка сообщения
        amount = float(values[2])
        result = CurrencyConverter.get_price(values[0].upper(), values[1].upper(), amount)
        bot.send_message(message.chat.id, f"{amount} {values[0].upper()} = {result} {values[1].upper()}")

    # Обработка ошибок
    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Неизвестная ошибка: {e}")

# Функция для запуска бота
def main():
    bot.polling()
