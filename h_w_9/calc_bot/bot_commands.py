from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

# async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Time {datetime.datetime.now().time()}')

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!\n' +'Добро пожаловать в бота калькулятор. Введи команду и цифры со знаком через пробел\n'+ '/menu\n/calc_rac\n/calc_comp\n')

async def calc_rac_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum  123 543433
    x = float(items[1])
    y = float(items[3])
    z = (items[2])
    if z == '+':
        await update.message.reply_text(f'{x} + {y} = {x + y}')
    elif z == '-':
        await update.message.reply_text(f'{x} - {y} = {x - y}') 
    elif z == '*':
        await update.message.reply_text(f'{x} * {y} = {x * y}')
    elif z == '/':
        await update.message.reply_text(f'{x} / {y} = {x / y}')



async def calc_comp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum  123 543433
    x = complex(items[1])
    y = complex(items[3])
    z = (items[2])
    if z == '+':
        await update.message.reply_text(f'{x} + {y} = {x + y}')
    elif z == '-':
        await update.message.reply_text(f'{x} - {y} = {x - y}') 
    elif z == '*':
        await update.message.reply_text(f'{x} * {y} = {x * y}')
    elif z == '/':
        await update.message.reply_text(f'{x} / {y} = {x / y}')