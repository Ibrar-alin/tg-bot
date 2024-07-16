from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, MessageHandler, Filter

TOKEN = 'YOUR_BOT_TOKEN'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

def start(update, context):
    update.message.reply_text('Hello! I am your bot.')

def echo(update, context):
    update.message.reply_text(update.message.text)

dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

if __name__ == '__main__':
    bot.set_webhook(url='https://YOUR_RENDER_APP_NAME.onrender.com/hook')
    app.run(host='0.0.0.0', port=5000)
