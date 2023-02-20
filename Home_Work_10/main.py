from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("6001298694:AAGqieRnM0XqinpX6_iJwFoyqVHlBzTrFag").build()
print('start')
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("newyear", newyear))

app.run_polling()