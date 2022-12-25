from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram_token import token1
import model
import sqlite3

TOKEN = token1

updater = Updater(TOKEN)
dp = updater.dispatcher


def main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', model.add)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model.add_name)],
            2: [MessageHandler(Filters.text & ~Filters.command, model.add_tel)],
            3: [MessageHandler(Filters.text & ~Filters.command, model.add_posicion)]
        },
        fallbacks=[CommandHandler('stop', model.stop)]
    )

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('dell', model.dell)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model.delete)],
        },
        fallbacks=[CommandHandler('stop', model.stop)]
    )
    dp.add_handler(conv_handler)
    dp.add_handler(delete_handler)

    start_handler = CommandHandler('start', model.start)
    view_handler = CommandHandler('view', model.view)
    add_handler = CommandHandler('add', main)
    # change_handler = CommandHandler('change', model.change)

    dp.add_handler(start_handler)
    dp.add_handler(view_handler)
    dp.add_handler(add_handler)
    # dp.add_handler(change_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
