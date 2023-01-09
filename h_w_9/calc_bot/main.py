import controller as c
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from logger import *
from spy import *
app = ApplicationBuilder().token('5849683524:AAF4NjMY5L4aPEUmFJh8yT48D6SqppLn7t0').build()

app.add_handler(CommandHandler("menu", menu_command))
app.add_handler(CommandHandler("calc_rac", calc_rac_command))
app.add_handler(CommandHandler("calc_comp", calc_comp_command))

print('server start')
app.run_polling()
app.updater.start_polling()
app.updater.idle()

c.button_click()