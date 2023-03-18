from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from tokens import tg_bot_token
from weather import get_weather


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Бот працює!!!"
    )


async def get_weather_from_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city_name = update.message.text
    try:
        result = get_weather(city_name)
    except Exception as exc:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Введіть назву міста!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=result)

if __name__ == '__main__':
    application = ApplicationBuilder().token(tg_bot_token).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), get_weather_from_bot)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
