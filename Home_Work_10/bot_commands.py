from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from calc import *
from datetime import datetime


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/help\n/hello\n/sum\n/calc\n/newyear')
 
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

async def newyear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    newyear = datetime(day=1, month=1, year=(int(datetime.now().year) + 1))
    timedelta = newyear - now
    await update.message.reply_text(f'До нового года {timedelta.days} дней')
    await update.message.reply_text(f'{int(timedelta.seconds) // 3600} часов')
    await update.message.reply_text(f'{(int(timedelta.seconds) % 3600) // 60} минут')
    await update.message.reply_text(f'{(int(timedelta.seconds) % 3600) % 60} секунд')


