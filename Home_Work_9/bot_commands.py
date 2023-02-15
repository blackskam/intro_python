from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from calc import *


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/help\n/hello\n/sum\n/calc')
 
async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x +y }')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    items.pop(0)
    await update.message.reply_text(f'{msg} = {calcList(calcPriority(calcBrackets(items)))}')