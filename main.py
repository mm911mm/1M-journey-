from telegram.ext import Updater, CommandHandler
import logging
import os

# إعدادات تسجيل الدخول
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    update.message.reply_text("🚀 مرحباً بك في 1M Journey Reloaded!\nراح توصلك تنبيهات البيع والشراء هنا بناء على خطة المليون.")

def notify_sell(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="📉 وقت البيع! بيع 5000 توكن بسعر 0.02$")

def notify_buy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="📈 وقت الشراء! اشتري 3000 توكن عند السعر 0.008$")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sell", notify_sell))
    dp.add_handler(CommandHandler("buy", notify_buy))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
