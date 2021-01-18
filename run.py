import time
import os

from telethon import TelegramClient, sync, events, utils
api_id = 682610 
api_hash = '030132b51d598e464419ccee7f20212d' 
client = TelegramClient('mbanurul', api_id, api_hash).start()

seconds = int(0)
minutes = int(0)

run = "dia"
while run.lower()=="dia":
  if seconds == 10:
  #print ("cek tanda")
    for message in client.iter_messages('pohonide', limit=1):
      (utils.get_display_name(message.sender), message.message)
      pesan = (message.message)
      print (pesan)
      tanda = pesan
        if tanda == 0:
        print ("do nothing")
        
        if tanda == 1:
        print ("do something")
        
      #os.system("python robotgabung.py")
    #minutes = minutes+1   
  
  if seconds == 20:
    run = "diaa"
  #os.system('clear')
  seconds = (seconds+1)
  print (seconds)
  time.sleep(1)
