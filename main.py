import os
import google.generativeai as genai

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
        CommandHandler,
            MessageHandler,
                ContextTypes,
                    filters,
                    )

                    BOT_TOKEN = os.getenv("BOT_TOKEN")
                    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

                    if not BOT_TOKEN:
                        raise ValueError("BOT_TOKEN environment variable is missing.")

                        if not GEMINI_API_KEY:
                            raise ValueError("GEMINI_API_KEY environment variable is missing.")

                            genai.configure(api_key=GEMINI_API_KEY)
                            model = genai.GenerativeModel("gemini-2.5-flash")


                            async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                await update.message.reply_text(
                                        "🚀 Welcome to AebyshAlphaBot!\n\n"
                                                "I'm your AI Stock Trading Assistant.\n"
                                                        "Ask me anything about stocks, investing, or the market."
                                                            )


                                                            async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                                await update.message.reply_text(
                                                                        "/start - Start the bot\n"
                                                                                "/help - Show this help message\n\n"
                                                                                        "Just send me any stock or investing question."
                                                                                            )


                                                                                            async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                                                                user_message = update.message.text

                                                                                                    try:
                                                                                                            response = model.generate_content(user_message)
                                                                                                                    await update.message.reply_text(response.text)
                                                                                                                        except Exception as e:
                                                                                                                                await update.message.reply_text(f"❌ Error: {e}")


                                                                                                                                def main():
                                                                                                                                    app = ApplicationBuilder().token(BOT_TOKEN).build()

                                                                                                                                        app.add_handler(CommandHandler("start", start))
                                                                                                                                            app.add_handler(CommandHandler("help", help_command))
                                                                                                                                                app.add_handler(
                                                                                                                                                        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
                                                                                                                                                            )

                                                                                                                                                                print("🚀 AebyshAlphaBot is running...")

                                                                                                                                                                    app.run_polling()


                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                        main()