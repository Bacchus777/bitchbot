import telebot
import requests

TOKEN = '404504606:AAHDaomduHTsjP0UDSDKa2dMygv9n_65wuU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text", "photo", "sticker"])
def repeat_all_messages(message): 
#    bot.send_message(303428461, message.from_user.first_name + ' ' + message.from_user.last_name + ': ' + message.text)
    bot.forward_message(chat_id = 303428461, from_chat_id = message.chat.id, message_id = message.message_id)
##@bot.message_handler(commands=['nikpidor'])
##def nikpidor(message):
##   bot.send_message(message.chat.id, 'Пидор дня опять <b>Nikita Losev</b>!', parse_mode = 'HTML')
###   bot.send_message(message.chat.id, message.chat.id)
##
##@bot.message_handler(commands=['say'])
##
##def say(message):
##   bot.send_message(-185388024, 'я твой кепка на хую вертел!', parse_mode = 'HTML')
##   #bot.send_message(message.chat.id, message.chat.id)
##
##@bot.message_handler(commands=['nikpidorall'])
##def nikpidorall(message):
##    msg = 'Топ 10 <b>пидоров</b>: \n'
##    msg = msg + '1. <b>Nikita Losev</b> \n'
##    msg = msg + '2. <b>Nikita Losev</b> \n'
##    msg = msg + '3. <b>Nikita Losev</b> \n'
##    msg = msg + '4. <b>Nikita Losev</b> \n'
##    msg = msg + '5. <b>Nikita Losev</b> \n'
##    msg = msg + '6. <b>Nikita Losev</b> \n'
##    msg = msg + '7. <b>Nikita Losev</b> \n'
##    msg = msg + '8. <b>Nikita Losev</b> \n'
##    msg = msg + '9. <b>Nikita Losev</b> \n'
##    msg = msg + '10. <b>Nikita Losev</b>'
##    bot.send_message(message.chat.id, msg, parse_mode = 'HTML')
###-185388024

bot.polling(none_stop=True)

