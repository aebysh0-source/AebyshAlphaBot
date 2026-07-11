from telegram import Update
from telegram.ext import ContextTypes

from services.gemini_service import ask_gemini


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            "👋 Hello Aebysh!\n\n"
                    "Welcome to AebyshAlphaBot v1.0\n\n"
                            "Your Personal AI Trading Partner 📈"
                                )


                                async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                    await update.message.reply_text(
                                            "Available Commands:\n\n"
                                                    "/start - Start the bot\n"
                                                            "/help - Show this help\n\n"
                                                                    "You can also send me any trading question."
                                                                        )


                                                                        async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                                            user_message = update.message.text

                                                                                reply = ask_gemini(user_message)

                                                                                    await update.message.reply_text(reply)