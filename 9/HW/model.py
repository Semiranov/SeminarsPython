from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import sqlite3


def start(update, context):
    update.message.reply_text(
        'Привет, что будем делать? \n'
        '/view - отобразить список всех сотрудников \n'
        '/add - добавить сотрудника \n'
        # '/change - изменить данные сотрудника \n'
        '/dell - удалить сотрудника \n'
        "Вы можете прервать опрос, послав команду /stop.\n")


def view(update, context):
    conn = sqlite3.connect('Peoples.db')
    cursor = conn.cursor()
    update.message.reply_text('Список всех сотрудников:')
    cursor.execute('select * from workers')
    rezults = cursor.fetchall()
    for i in rezults:
        update.message.reply_text(" ".join([str(i)]))
    conn.close()


def add(update, context):
    update.message.reply_text("Введите имя:")
    return 1


def add_name(update, contex):
    global isname
    isname = update.message.text
    update.message.reply_text("Введите телефон:")
    return 2


def add_tel(update, contex):
    global tel
    tel = int(update.message.text)
    update.message.reply_text("Введите должность:")
    return 3


def add_posicion(update, contex):
    pos = update.message.text
    conn = sqlite3.connect('Peoples.db')
    cursor = conn.cursor()
    cursor.execute(
        f"insert into workers(name, phone, position)"
        f"values ('{isname}',{tel},'{pos}')"
    )
    conn.commit()
    conn.close()


# def change(update, context):


def dell(update, context):
    update.message.reply_text('Введите id который нужно удалить')
    return 1


def delete(update, context):
    conn = sqlite3.connect('Peoples.db')
    cursor = conn.cursor()
    id_dell = update.message.text
    cursor.execute(f"delete from workers where id={id_dell}")
    conn.commit()
    conn.close()


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END
