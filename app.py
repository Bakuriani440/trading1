from flask import Flask, request
import telebot

# Настройки Telegram-бота
TOKEN = 'ВАШ_ТОКЕН_БОТА'
CHAT_ID = 'ВАШ_ЧАТ_ID'  # Замените на ваш Telegram Chat ID
bot = telebot.TeleBot(TOKEN)

# Создаем Flask приложение
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Получаем данные из вебхука TradingView
    if data and 'signal' in data:
        signal = data['signal']
        if signal == 'up':
            bot.send_message(CHAT_ID, "📈 Индикатор P3 указывает ВВЕРХ")
        elif signal == 'down':
            bot.send_message(CHAT_ID, "📉 Индикатор P3 указывает ВНИЗ")
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
