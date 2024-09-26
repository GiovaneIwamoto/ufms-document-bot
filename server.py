from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context) -> None:
    await update.message.reply_text('Olá! Eu sou um bot básico no Telegram.')

async def help_command(update: Update, context) -> None:
    await update.message.reply_text('Aqui estão os comandos disponíveis:\n/start - Iniciar\n/help - Obter ajuda')

if __name__ == '__main__':
    # Substitua 'YOUR_TOKEN' pelo token do seu bot que você obteve no BotFather
    token = '7852316944:AAHuHKYWD9DhzDrNYgY09HwDQDG_AqCBclo'
    
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    print("Bot running...")
    application.run_polling()
