import octopush
import uuid
import sys  , time
from octopush import SMS
from config import config
from balance import balance
from colorama import Fore, init
from os import system, name 
import sys  , time


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
    	_ = system('clear') 


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)

clear()
print_slow(Fore.RED + '''
      .o.                                                                                                    
     .888.                                                                                                   
    .8"888.     ooo. .oo.    .ooooo.  ooo. .oo.    .oooo.o ooo. .oo.  .oo.   ooo. .oo.  .oo.    .oooo.o      
   .8' `888.    `888P"Y88b  d88' `88b `888P"Y88b  d88(  "8 `888P"Y88bP"Y88b  `888P"Y88bP"Y88b  d88(  "8      
  .88ooo8888.    888   888  888   888  888   888  `"Y88b.   888   888   888   888   888   888  `"Y88b.       
 .8'     `888.   888   888  888   888  888   888  o.  )88b  888   888   888   888   888   888  o.  )88b      
o88o     o8888o o888o o888o `Y8bod8P' o888o o888o 8""888P' o888o o888o o888o o888o o888o o888o 8""888P' 
     
                                           @ITS_JUSTHACKED                                                                  
                                                                                                                                                                                                                          
''') 
recipient = []
message = str(input("Enter  Your message : "))
data = str(input("Enter  Victum number : "))
recipient.append(data)
sender = 'Idowu'
sms = SMS(config['user_login'], config['api_key'])
sms.set_sms_text(message)
sms.set_sms_recipients(recipient)
sms.set_sms_type(octopush.SMS_PREMIUM)
sms.set_sms_sender(sender)
sms.set_sms_request_id(str(uuid.uuid1))
sent_result = sms.send()
print(sent_result)
time.sleep(2)
print(Fore.GREEN + "Message sent Scuccessfully !!")
print(Fore.RED + "Your Left Balance is :" + balance.text )

