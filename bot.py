from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN", "7452161824:AAEWBAS47ziurLCJaQ8gU0upTmnQhapFpTA")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        text = update.message.text

        if text == "/start":
            bot.send_message(chat_id=chat_id, text="Bot is live and working!")
        elif text == "/help":
            bot.send_message(chat_id=chat_id, text="Send /start to test the bot.")

        return "ok", 200

if __name__ == "__main__":
    app.run(debug=True)
