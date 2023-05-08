import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
import logging
import config




BOT_TOKEN = config.BOT_TOKEN
stripe_secret_key = config.STRIPE_SECRET_KEY

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Инициализация бота
bot = telegram.Bot(token=BOT_TOKEN)


# Обработка команды /start
def start_command_handler(update: Update, context: CallbackContext):
    # Получение имени пользователя
    user_name = update.message.from_user.first_name
    # Получение ID чата
    chat_id = update.message.chat_id

    # Отправка приветственного сообщения
    message = f"Привет, {user_name}, дай денег СУКА!"
    context.bot.send_message(chat_id=chat_id, text=message)

    # Добавляем отладочное сообщение для проверки
    print(f"Обработана команда /start от пользователя {user_name} в чате {chat_id}")


def start_command_handler(update: Update, context: CallbackContext):
    # Получение имени пользователя
    user_name = update.message.from_user.first_name
    # Получение ID чата
    chat_id = update.message.chat_id

    # Отправка приветственного сообщения
    message = f"Привет, {user_name}, дай денег СУКА!"
    context.bot.send_message(chat_id=chat_id, text=message)


    # Отправка кнопки оплаты
    prices = [LabeledPrice(label='Подписка на 2 дня', amount=0),
              LabeledPrice(label='Подписка на неделю', amount=2900)]
    keyboard = [[InlineKeyboardButton(text="Деньги кидай сюда, мразь", pay=True)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_invoice(chat_id=chat_id, title='Подписка на контент', description='Описание подписки',
                             provider_token=STRIPE_SECRET_KEY, currency='RUB', prices=prices,
                             start_parameter='subscribe', reply_markup=reply_markup)


# Обработка оплаты
@run_async
def process_payment(update: Update, context: CallbackContext):
    # Получение объекта платежа
    successful_payment = update.message.successful_payment
    # Получение ID чата
    chat_id = update.message.chat_id

    # Отправка сообщения об успешной оплате
    message = f"Спасибо за оплату!"
    context.bot.send_message(chat_id=chat_id, text=message)

    # Отправка видео
    context.bot.send_video(chat_id=chat_id, video='<видео-файл>')

    # Отправка кнопки отмены подписки
    keyboard = [[InlineKeyboardButton(text="Отменить подписку", callback_data="cancel")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=chat_id, text="Вы подписаны на контент. Нажмите на кнопку, чтобы отменить подписку.",
                             reply_markup=reply_markup)


# Обработка нажатия на кнопку отмены подписки
def cancel_subscription(update: Update, context: CallbackContext):
    # Получение ID чата
    chat_id = update.callback_query.message.chat_id
    # Получение ID подписки по ID чата
    subscription
