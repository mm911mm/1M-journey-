from telegram.ext import Updater, CommandHandler

# دالة الاستجابة لأمر /start
def start(update, context):
    update.message.reply_text("مرحبًا بك في بوت 1M Journey 🚀")

# الدالة الرئيسية لتشغيل البوت
def main():
    # ضع التوكن الخاص بك هنا أو اجعله يُقرأ من environment variable
    import os
    TOKEN = os.getenv("BOT_TOKEN")

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة أمر /start
    dp.add_handler(CommandHandler("start", start))

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
