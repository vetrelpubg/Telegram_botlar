from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler,Filters
from methods import *


updater = Updater(token='5041227084:AAElAGmtntnSPJKO9p5-Xgy6gCja5Rt4Mqs')

dispatcher=updater.dispatcher

conv_handler=ConversationHandler(
    entry_points=[CommandHandler('start',start)],
    states={
        1:[MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±TOSHKENTð¸ð±ð¸ð±ð¸ð±$"), toshkent),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±SIRDARYOð¸ð±ð¸ð±ð¸ð±$"), sirdaryo),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±JIZZAXð¸ð±ð¸ð±ð¸ð±$"), jizzax),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±SAMARQANDð¸ð±ð¸ð±ð¸ð±$"), samarqand),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±FARGONAð¸ð±ð¸ð±ð¸ð±$"), fargona),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±NAMANGANð¸ð±ð¸ð±ð¸ð±$"), namangan),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±ANDIJONð¸ð±ð¸ð±ð¸ð±$"), andijon),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±QASHQADARYOð¸ð±ð¸ð±ð¸ð±$"), qashqadaryo),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±SURXONDARYOð¸ð±ð¸ð±ð¸ð±$"), surxondaryo),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±BUXOROð¸ð±ð¸ð±ð¸ð±$"), buxoro),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±XORAZMð¸ð±ð¸ð±ð¸ð±$"), xorazm),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±QORAQALPOQð¸ð±ð¸ð±ð¸ð±$"), qoraqalpoq),
           MessageHandler(Filters.regex("^ð¸ð±ð¸ð±ð¸ð±NAVOIYð¸ð±ð¸ð±ð¸ð±$"), navoiy)]



    },
    fallbacks = [MessageHandler(Filters.text, start)]
)
dispatcher.add_handler(conv_handler)



updater.start_polling()


print('Tugadi')