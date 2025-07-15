from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import os

TOKEN = "8145115338:AAFuoZSR7XvQTCdkXIg6p6M9pT1R2C-3BM8"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("أهلًا بك في بوت 1M Journey 🚀")

def send_file(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    file_path = "example.txt"
    with open(file_path, "w") as f:
        f.write("هذا ملف تجريبي من البوت.")
    with open(file_path, "rb") as f:
        context.bot.send_document(chat_id=chat_id, document=f)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("file", send_file))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
