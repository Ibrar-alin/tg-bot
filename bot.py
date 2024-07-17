import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import *
API_KEY = "6929324010:AAFbxZDJXYbcue55pqbxF4s9wZIqibcd33w"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot....')

async def start_commmand(update, context):
    user = update.message.from_user
    username = user.username
    wurl = "http://t.me/SimpleEn_bot/WebMyapp"
    hurl = "http://t.me/Crypt0Xali"
    curl = "http://t.me/Crypt0Xali"
    turl = "http://t.me/Crypt0Xali"
    # Create an inline keyboard with a button that links to the URL
    keyboard = [
        [InlineKeyboardButton("Open Link", url=wurl)],
        [InlineKeyboardButton("Follow Community", url=curl)],
        [InlineKeyboardButton("Need Help", url=hurl)],
        [InlineKeyboardButton("Invite Friends", url=hurl)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
       f"""
        Hey @{username}! Welcome to SimpleEarn!
        Tap on the coin and see your balance rise.
        TapSwap is a cutting-edge financial platform where users
        can earn tokens by leveraging the mining app's various features. 
        The majority of TapSwap Token (TAPS) distribution will occur among 
        the players here. Do you have friends, relatives, or co-workers? 
        Bring them all into the game. More buddies, more coins.
        """, reply_markup=reply_markup,)

async def help_commmand(update, context):
    await update.message.reply_text('How can i help you!')

async def custom_command(update, context):
    await update.message.reply_text('custom command here')

#async def handl_message(update, context):
   # text = str(update.message.text).lower()
  #  logging.info(f'User({update.message.chat.id}) says: {text}')

    # bot response
  #  update.message.reply_text(text)

if __name__ == '__main__':
    application = Application.builder().token(API_KEY).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(CommandHandler('help', help_commmand))
    application.add_handler(CommandHandler('custom', custom_command))

    # Run bot
    application.run_polling(1.0)
