from flask import Flask, request
import telegram

TOKEN = "7452161824:AAEWBAS47ziurLCJaQ8gU0upTmnQhapFpTA"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.sendMessage(chat_id=chat_id, text="Welcome to Crypto Signal Bot!")
    else:
        bot.sendMessage(chat_id=chat_id, text=f"You said: {text}")
    
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
