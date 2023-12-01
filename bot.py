import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    name=update['message']['chat']['first_name']
    username=update['message']['chat']['username']
    print(f'Пользователем {username} вызван /start')
    update.message.reply_text(f"Привет, {name}! Ты вызвал команду /start")


def talk_to_me(update, context):
    user_text = update.message.text 
    name=update['message']['chat']['first_name']
    print(user_text)
    update.message.reply_text(f"{name}! {user_text}")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
    
if __name__ == "__main__":
    main()

'''
{'message': {'date': 1701446509, 'delete_chat_photo': False, 'new_chat_members': [], 
'entities': [{'type': 'bot_command', 'offset': 0, 'length': 6}], 'text': '/start', 
'message_id': 10, 'supergroup_chat_created': False, 'new_chat_photo': [], 
'group_chat_created': False, 'channel_chat_created': False, 'caption_entities': [], 
'photo': [], 'chat': {'id': 178392692, 'first_name': 'Eugene', 'type': 'private', 
'username': 'eugenesemin'}, 'from': {'id': 178392692, 
'is_bot': False, 'username': 'eugenesemin', 'first_name': 'Eugene', 'language_code': 'ru'}}, 
'update_id': 149616443}
'''