import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("♻️ Что куда сдавать?")
    btn2 = types.KeyboardButton("📜 Правила")

    markup.add(btn1, btn2)

    welcome_text = f'Привет! Я помогу тебе быстро разобраться с мусором в быту. Нажми кнопку ниже или просто напиши мне название предмета (например: бутылка, чек, крышка), и я скажу, что с ним делать! {bot.get_me().first_name}!'
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "♻️ Что куда сдавать?":
        bot.send_message(message.chat.id, "Просто напиши мне название предмета (например: батарейка).")
        
    elif message.text == "📜 Правила":
        rules = (
            "1. Сполосни и сожми (чтобы не пахло и занимало меньше места).\n\n"
            "2. Обращай внимание на маркировку (цифры в треугольниках).\n\n"
            "3. Разделяй: пластик отдельно, бумагу отдельно."
        )
        bot.send_message(message.chat.id, rules)

  
    elif "батарейк" in message.text.lower():
        bot.send_message(message.chat.id, "❌ Опасно! Батарейки нельзя кидать в общий мусор. Сдай в спец. бокс в магазине.")
    elif "бутылк" in message.text.lower():
        bot.send_message(message.chat.id, "♻️ Пластик (01 PET). Сполосни, сожми и бросай в желтый бак!")
      
bot.polling(none_stop=True)

