from flask import Flask, request
import telebot

# Настройки Telegram-бота
TOKEN = '7755553902:AAGQaHFSfyrTctGkuL7jbeGj-TcyIiVTk5U'
CHAT_ID = '6276946287'  # Ваш Telegram Chat ID
bot = telebot.TeleBot(TOKEN)

# Создаем Flask приложение
app = Flask(__name__)

# Корневой маршрут для проверки работы сервера
@app.route('/')
def home():
    return "Сервер работает! Добро пожаловать!"

# Маршрут для вебхука
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Проверяем тип контента и обрабатываем данные
        if request.content_type == 'application/json':
            data = request.json  # JSON-данные из TradingView
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.form.to_dict()  # Данные form-urlencoded
        elif request.content_type == 'text/plain':
            data = request.data.decode('utf-8')  # Текстовые данные
        else:
            return "Unsupported Media Type", 415  # Ошибка для неподдерживаемого типа данных

        print(f"Полученные данные: {data}")  # Логируем входящие данные

        # Обработка и отправка данных в Telegram
        if isinstance(data, dict):
            # Если это JSON или form-urlencoded, преобразуем в строку для отправки
            message = f"🚨 Уведомление от TradingView:\n{data}"
        elif isinstance(data, str):
            # Если это текст, отправляем напрямую
            message = f"🚨 Уведомление от TradingView:\n{data}"
        else:
            message = "⚠️ Получены неизвестные данные"

        # Отправка сообщения в Telegram
        bot.send_message(CHAT_ID, message)
        return "Уведомление обработано и отправлено", 200

    except Exception as e:
        # Логируем ошибки
        print(f"Ошибка обработки: {e}")
        return "Ошибка сервера", 500

if __name__ == '__main__':
    # Сервер запускается на 80 порту для работы с TradingView
    app.run(debug=True, host="0.0.0.0", port=80)
