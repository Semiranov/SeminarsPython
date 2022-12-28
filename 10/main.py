import logging
from telegram_token import token1
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

candies = 17
step = 15

reply_keyboard = [['/play', '/settings'],
                  ['/rules', '/close']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

TOKEN = token1


def start(update, context):
    name = f"{update.message.from_user.first_name}"
    update.message.reply_text(f"Привет, {name}. Давай поиграем? Выбери пункт", reply_markup=markup)


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(f'Определите общеее колличество конфет, и колличество'
                              f' конфет которое можно взять за раз. Берите конфеты пока не кончатся')


def settings(update, context):
    update.message.reply_text('Введите общее колличество конфет и макс. коллличество на ход')
    return 1


def set_settings(update, context):
    global candies, step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text('Правила установлены')
    return ConversationHandler.END


def play(update, context):
    update.message.reply_text(f'Ваш ход, на кону {candies} конфет, макс берите {step}',
                              reply_markup=ReplyKeyboardRemove())
    return 1


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def play_step(update, context):
    global candies
    candy = int(update.message.text)
    candies -= candy
    if candies <= step:
        update.message.reply_text(f'Ты победил', reply_markup=markup)
        return ConversationHandler.END
    else:
        if candies % (step + 1) == 0:
            update.message.reply_text(f'На кону {candies} конфет, я беру {1} конфет')
            candies -= 1
        else:
            update.message.reply_text(f'На кону {candies} конфет, я беру {candies % (step + 1)} конфет')
            candies -= candies % (step + 1)
            if candies <= step:
                update.message.reply_text(f'Ты проиграл', reply_markup=markup)
                return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    setting_handler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(setting_handler)
    dp.add_handler(play_handler)

    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
