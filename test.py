import telebot

TOKEN = '7755553902:AAGQaHFSfyrTctGkuL7jbeGj-TcyIiVTk5U'
bot = telebot.TeleBot(TOKEN)

updates = bot.get_updates()
for update in updates:
    print(update.message.chat.id)