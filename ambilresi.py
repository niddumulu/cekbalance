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
  if seconds == 59:
      seconds = 0
      minutes = minutes+1
      if minutes == 1:
        print ("ok")
        for message in client.iter_messages('niddumulu', limit=1):
          (utils.get_display_name(message.sender), message.message)
          pesan = (message.message)
          print (pesan)
          if pesan == 1:
             print ("lanjut ambil resi")
             for message in client.iter_messages('cekresii', limit=1):
                (utils.get_display_name(message.sender), message.message)
                pesanchannel = (message.message)
                print (pesanchannel)
                client.send_message('cekresijnt', pesanchannel)
      if minutes == 2:
        minutes = 0  
  seconds = (seconds+2)
  print (minutes,seconds)
  time.sleep(1)
