import time
import os

from telethon import TelegramClient, sync, events, utils
api_id = 682610 
api_hash = '030132b51d598e464419ccee7f20212d' 
client = TelegramClient('mbanurul', api_id, api_hash).start()

for message in client.iter_messages('cekresii', limit=1):
          (utils.get_display_name(message.sender), message.message)
          pesan = (message.message)
          print (pesan)

#seconds = int(0)
#minutes = int(0)

#run = "dia"
#while run.lower()=="dia":
  #if seconds == 59:
    #seconds = 0
    #minutes = minutes+1
    #if minutes == 1:
      #print ("sahal")
      #os.system("python robotgabung.py")
    #if minutes == 5:
      #print ("sahil")
      #minutes = 0
      
  #os.system('clear')
  #seconds = (seconds+1)
  #print (minutes," : ", seconds)
  #time.sleep(1)
