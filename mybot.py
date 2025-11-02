import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tala import get_price  

TOKEN = '8483516997:AAGtryhOROkFM3oAJoyc4wBaNWriPOlnVvQ'
bot = telebot.TeleBot(TOKEN)

# ---------- Keyboard buttons ----------
def get_name_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("💵 دلار", callback_data="دلار"),
        InlineKeyboardButton("💶 یورو", callback_data="یورو"),
        InlineKeyboardButton("🏅طلا 18 عیار", callback_data="طلا 18 عیار"),
        InlineKeyboardButton("🥇 سکه امامی", callback_data="سکه امامی"),
        InlineKeyboardButton("🪙 نیم سکه", callback_data="نیم سکه"),
        InlineKeyboardButton("🔹 ربع سکه", callback_data="ربع سکه")
    )
    return markup

# ----------/start command ----------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"سلام {message.from_user.first_name} 👋\nیکی از گزینه‌های زیر را انتخاب کنید:\n قیمت لحظه ای را اعلام میکنم .",
        reply_markup=get_name_keyboard()
    )

# ---------- When one of the buttons is clicked----------
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    prices = get_price()  # فرض می‌کنیم تابع get_price() دیکشنری از قیمت‌ها برمی‌گرداند

    if data in prices:
        price = prices[data]
        bot.send_message(call.message.chat.id, f"💰 قیمت {data}: {price} تومان")
    else:
        bot.send_message(call.message.chat.id, f"❌ نتیجه‌ای برای {data} یافت نشد.")

# ---------- Run the robot ----------
print("🤖 ربات فعال شد...")
bot.infinity_polling()