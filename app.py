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
        # Обработка различных типов контента
        if request.content_type == 'application/json':
            data = request.json
        elif 'application/x-www-form-urlencoded' in request.content_type:
            data = request.form.to_dict()
        elif 'text/plain' in request.content_type:
            data = request.data.decode('utf-8')
        else:
            data = request.data.decode('utf-8')  # В случае других форматов, преобразуем в строку

        # Логируем входящие данные
        print(f"Полученные данные: {data}")  

        # Отправка данных в Telegram
        message = f"🚨 Уведомление от TradingView:\n{data}"
        bot.send_message(CHAT_ID, message)
        return "Уведомление обработано и отправлено", 200

    except Exception as e:
        # Логируем ошибки
        print(f"Ошибка обработки: {e}")
        return "Ошибка сервера", 500

if __name__ == '__main__':
    # Сервер запускается на 80 порту для работы с TradingView
    app.run(debug=True, host="0.0.0.0", port=80)
