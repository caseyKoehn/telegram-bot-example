import datetime # Importing the datetime library to get date and time
import telepot  # Importing the telepot library to send and receive telegram messages
from telepot.loop import MessageLoop # Library function to communicate with telegram bot
from time import sleep # Importing the time library to provide the delays in program

print('Starting Bot')

# Defining the message handler and printing out some information

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    print('Received:')
    print(chat_id)
    print(content_type)
    
# Comparing the incoming message to send a reply according to it
    
    if content_type == 'document':
        uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
        path = "C:/Users/casey/OneDrive/Casey's Folder/Thonny Code/Song Stash Bot/theFile/"
        bot.download_file(msg['document']['file_id'], path + uniq_filename + '.pdf')
    else:
        bot.sendMessage(chat_id, str("Please send file."))
        
# Insert your telegram token below
bot = telepot.Bot('INSERT BOT TOKEN HERE')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
