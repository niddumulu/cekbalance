import os
import time
from telethon import TelegramClient, sync, events, utils
api_id = 682610 
api_hash = '030132b51d598e464419ccee7f20212d' 
client = TelegramClient('mbanurul', api_id, api_hash).start()
seconds= int(0)
minutes= int(0)
run = "siap"
while run.lower()=="siap":
  if seconds == 2:
      seconds = 0
      minutes = minutes+1
      if minutes == 1:
        print ("ok")
        for message in client.iter_messages('cekresii', limit=1):
          (utils.get_display_name(message.sender), message.message)
          pesan = (message.message)
          print (pesan)
          client.send_message('berlatihbot', pesan)
      if minutes == 9:
        for message in client.iter_messages('berlatihbot', limit=1):
          (utils.get_display_name(message.sender), message.message)
          pesan = (message.message)
          print (pesan)
          client.send_message('niddumulu', pesan)
        minutes = 0  
        run = "off"
  seconds = (seconds+1)
  print (minutes,seconds)
  time.sleep(1)
