import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Token-ا تە یا بوت فازەری
TOKEN = "8287119446:AAG-Dv-KsaYdDCIUG5wEhIJ-VPd6mL9Fr_Y"

# لینکا یارییا تە یا نوو ل سەر GitHub Pages
WEB_APP_URL = "https://mustafaduski.github.io/aviator-pro-ton/"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """فرێکرنا دوگمەیا یارییا پرۆ ب وەلێتێ TON"""
    keyboard = [
        [InlineKeyboardButton("🚀 Launch Aviator PRO", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to Aviator PRO!\n\nConnect your TON wallet and start playing.",
        reply_markup=reply_markup
    )

if name == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.run_polling()
