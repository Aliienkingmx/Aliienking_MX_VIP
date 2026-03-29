import telebot
import hashlib
import time

TOKEN = '8629628720:AAFu73jRo-suRSpl4MD28LzR6NbwQUWSR2k'
ADMIN_ID = 6882089359
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['setup'])
def setup(message):
    msg = (
        "👽 *GUÍA DE INSTALACIÓN ALIIENKING MX* 👽\n\n"
        "👉 *MÉTODO 1: TERMUX (Recomendado)*\n"
        "`pkg install curl -y && curl -sL https://raw.githubusercontent.com/Aliienkingmx/Aliienking_MX_VIP/main/install.sh | bash` \n\n"
        "👉 *MÉTODO 2: BREVENT / SHIZUKU*\n"
        "1. Descarga el archivo `aliien_fast.sh` de nuestro canal.\n"
        "2. Ejecuta: `sh /sdcard/Download/aliien_fast.sh` \n\n"
        "🔗 *CANAL DE WHATSAPP:* [ENTRAR AQUÍ](https://whatsapp.com/channel/0029VbCcFzILY6d7SA9jhL1A)"
    )
    bot.send_message(message.chat.id, msg, parse_mode="Markdown")

# (Mantiene el resto de funciones /gen y /start que ya programamos)
print("--- BOT ACTUALIZADO CON MÉTODOS UNIVERSALES ---")
bot.polling()
