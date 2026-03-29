import telebot, hashlib, time, json, os
from datetime import datetime, timedelta
from telebot import types

TOKEN = '8629628720:AAFu73jRo-suRSpl4MD28LzR6NbwQUWSR2k'
ADMIN_ID = 6882089359 
bot = telebot.TeleBot(TOKEN)
DB_DIR = "/data/data/com.termux/files/home/ALIIENKING_MX/db/"
KEYS_FILE = DB_DIR + "keys.json"

if not os.path.exists(DB_DIR): os.makedirs(DB_DIR)
if not os.path.exists(KEYS_FILE): 
    with open(KEYS_FILE, "w") as f: json.dump({}, f)

def load_db():
    with open(KEYS_FILE, "r") as f: return json.load(f)

def save_db(data):
    with open(KEYS_FILE, "w") as f: json.dump(data, f)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🚀 PRUEBA GRATIS (1H)", "💎 VER PLANES")
    bot.send_message(message.chat.id, "👽 *ALIIENKING MX BOT ONLINE* 👽\n¿Listo para dominar?", parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🚀 PRUEBA GRATIS (1H)")
def free(message):
    uid = str(message.from_user.id)
    db = load_db()
    for k in db.values():
        if k.get("uid") == uid:
            bot.reply_to(message, "❌ Ya usaste tu prueba.")
            return
    key = f"AK-DEMO-{hashlib.md5(f'{uid}{time.time()}'.encode()).hexdigest()[:5].upper()}"
    exp = (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
    db[key] = {"uid": uid, "exp": exp, "tipo": "DEMO"}
    save_db(db)
    bot.reply_to(message, f"✅ *DEMO 1H:* `{key}`\n⌛ Expira: {exp}")

@bot.message_handler(func=lambda m: m.text == "💎 VER PLANES")
def planes(message):
    m = types.InlineKeyboardMarkup()
    m.add(types.InlineKeyboardButton("📤 ENVIAR COMPROBANTE", callback_data="pagar"))
    bot.send_message(message.chat.id, "🥉 RECLUTA ($5)\n🥈 ALIIENKING ($10)\n🥇 GALACTICO ($25)", reply_markup=m)

@bot.callback_query_handler(func=lambda c: c.data == "pagar")
def pagar(c): bot.send_message(c.message.chat.id, "📸 Envía foto de tu pago.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    m = types.InlineKeyboardMarkup()
    m.add(types.InlineKeyboardButton("✅ APROBAR", callback_data=f"ok_{message.from_user.id}"))
    bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=f"💰 PAGO: {message.from_user.first_name}", reply_markup=m)
    bot.reply_to(message, "⏳ Enviado al CEO.")

@bot.callback_query_handler(func=lambda c: c.data.startswith("ok_"))
def approve(c):
    if c.from_user.id != ADMIN_ID: return
    uid = c.data.split("_")[1]
    key = f"AK-VIP-{hashlib.md5(f'{uid}{time.time()}'.encode()).hexdigest()[:8].upper()}"
    db = load_db()
    db[key] = {"uid": uid, "tipo": "VIP"}
    save_db(db)
    bot.send_message(uid, f"🎉 ¡PAGO APROBADO!\n🔑 Key VIP: `{key}`")
    bot.answer_callback_query(c.id, "Entregado")

print("--- BOT ALIIENKING MX ACTIVO ---")
bot.polling()
