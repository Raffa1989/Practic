import telebot
TOKEN = "5030984361:AAEgqPlES5ORzFcc8ecnPkahZzIL4DoxONM"
bot = telebot.TeleBot(TOKEN) #Чтобы запустить бота, нужно воспользоваться методом polling.

@bot.message_handler(filters) #filters — фильтры, определяющие, следует ли вызывать декорированную
# функцию для соответствующего сообщения или нет. У одного обработчика может быть несколько фильтров.
#Для обработчиков сообщений разрешено любое имя функции, поэтому function_name может принимать любое значение.
# Функция должна принимать не более одного аргумента — сообщения, которое функция должна обработать
def function_name(message):
    bot.reply_to(message, "This is a message handler")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

#обработчик берет из сообщения username и выдает приветственное сообщение с привязкой к пользователю
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")

#на сообщения с фотографией будет отвечать сообщением «Nice meme XDD»
@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass