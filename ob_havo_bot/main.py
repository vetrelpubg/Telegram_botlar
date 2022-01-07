from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler,Filters
from methods import *


updater = Updater(token='5041227084:AAElAGmtntnSPJKO9p5-Xgy6gCja5Rt4Mqs')

dispatcher=updater.dispatcher

conv_handler=ConversationHandler(
    entry_points=[CommandHandler('start',start)],
    states={
        1:[MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱TOSHKENT🇸🇱🇸🇱🇸🇱$"), toshkent),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱SIRDARYO🇸🇱🇸🇱🇸🇱$"), sirdaryo),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱JIZZAX🇸🇱🇸🇱🇸🇱$"), jizzax),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱SAMARQAND🇸🇱🇸🇱🇸🇱$"), samarqand),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱FARGONA🇸🇱🇸🇱🇸🇱$"), fargona),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱NAMANGAN🇸🇱🇸🇱🇸🇱$"), namangan),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱ANDIJON🇸🇱🇸🇱🇸🇱$"), andijon),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱QASHQADARYO🇸🇱🇸🇱🇸🇱$"), qashqadaryo),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱SURXONDARYO🇸🇱🇸🇱🇸🇱$"), surxondaryo),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱BUXORO🇸🇱🇸🇱🇸🇱$"), buxoro),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱XORAZM🇸🇱🇸🇱🇸🇱$"), xorazm),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱QORAQALPOQ🇸🇱🇸🇱🇸🇱$"), qoraqalpoq),
           MessageHandler(Filters.regex("^🇸🇱🇸🇱🇸🇱NAVOIY🇸🇱🇸🇱🇸🇱$"), navoiy)]



    },
    fallbacks = [MessageHandler(Filters.text, start)]
)
dispatcher.add_handler(conv_handler)



updater.start_polling()


print('Tugadi')