import telepot  # Importing the telepot library to send and receive telegram messages
from telepot.loop import MessageLoop # Library function to communicate with telegram bot
from time import sleep # Importing the time library to provide the delays in program

personal = <personal_chat_id>

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text'] # Getting text from the message

    print ('Received:')
    print(command)
    print(chat_id)
    # Comparing the incoming message to send a reply according to it
    
    if command == '/start':
        bot.sendMessage(chat_id, str("Welcome to message forwarder. Send me a random message and I will forward it to the Owner of the bot.")
    else:
        bot.forwardMessage(personal, chat_id, message_id)
        bot.sendMessage(chat_id, str("Message Forwarded")
# Insert your telegram token below
bot = telepot.Bot('your_token_here')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
