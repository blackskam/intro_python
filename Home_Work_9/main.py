from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("6149528192:AAG5JjQm7cuRpeYSGpIwgzmDToSpbiwAsjQ").build()
print('start')
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("calc", calc))

app.run_polling()