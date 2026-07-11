from telegram.ext import (
        Application,
            CommandHandler,
                MessageHandler,
                    filters,
                    )

                    from utils.config import BOT_TOKEN
                    from bot.handlers import start, help_command, chat


                    def main():
                        app = Application.builder().token(BOT_TOKEN).build()

                            # Commands
                                app.add_handler(CommandHandler("start", start))
                                    app.add_handler(CommandHandler("help", help_command))

                                        # Normal chat messages
                                            app.add_handler(
                                                    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
                                                        )

                                                            print("🚀 AebyshAlphaBot v1.0 is running...")

                                                                app.run_polling()


                                                                if __name__ == "__main__":
                                                                    main()
)