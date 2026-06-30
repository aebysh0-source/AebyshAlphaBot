from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello Aebysh 👋\n\n"
        "I'm AebyshAlphaBot Version 1.0\n\n"
        "Your Personal AI Trading Partner 📈"
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")

app.run_polling()
