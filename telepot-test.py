import telepot  # Importing the telepot library to send and receive telegram messages
from telepot.loop import MessageLoop # Library function to communicate with telegram bot
from time import sleep # Importing the time library to provide the delays in program

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text'] # Getting text from the message

    print ('Received:')
    print(command)
    print(chat_id)
    # Comparing the incoming message to send a reply according to it
    
    if command == '/start':
        bot.sendMessage(chat_id,str("Hello! I am a bot!"))
    elif command =='/hello':
        bot.sendMessage(chat_id, str("Hello World!"))
    else:
        bot.sendMessage(chat_id, str("Invalid Entry"))

# Insert your telegram token below
bot = telepot.Bot('<your_token_here>')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
