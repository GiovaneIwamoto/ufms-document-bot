import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

load_dotenv()

token = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context) -> None:
    await update.message.reply_text('Olá! Eu sou um bot básico no Telegram.')

async def help_command(update: Update, context) -> None:
    await update.message.reply_text('Aqui estão os comandos disponíveis:\n/start - Iniciar\n/help - Obter ajuda')

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    print("Bot running...")
    application.run_polling()
