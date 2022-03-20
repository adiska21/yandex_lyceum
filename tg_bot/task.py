# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time

TOKEN = "5164212571:AAEpN2sgFEFqDRNytmpxNlBqvR9ZokEexU4"


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(f"Я получил сообщение: '{update.message.text}'")


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("date", date_get))
    dp.add_handler(CommandHandler("time", time_get))

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


def date_get(update, context):
    time_ = time.asctime()
    time_ = time_.split(" ")
    w_day, month, m_day, time_send, year = time_
    date = f"{m_day} {month} {year}"
    print(time_)
    update.message.reply_text(date)


def time_get(update, context):
    time_ = time.asctime()
    time_ = time_.split(" ")
    time_send = time_[-2]
    print(time_)
    update.message.reply_text(time_send)


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()