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

  /$$$$$$                                                                       
 /$$__  $$                                                                      
| $$  \ $$ /$$$$$$$   /$$$$$$  /$$$$$$$         /$$$$$$$ /$$$$$$/$$$$   /$$$$$$$
| $$$$$$$$| $$__  $$ /$$__  $$| $$__  $$       /$$_____/| $$_  $$_  $$ /$$_____/
| $$__  $$| $$  \ $$| $$  \ $$| $$  \ $$      |  $$$$$$ | $$ \ $$ \ $$|  $$$$$$ 
| $$  | $$| $$  | $$| $$  | $$| $$  | $$       \____  $$| $$ | $$ | $$ \____  $$
| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$       /$$$$$$$/| $$ | $$ | $$ /$$$$$$$/
|__/  |__/|__/  |__/ \______/ |__/  |__/      |_______/ |__/ |__/ |__/|_______/ 
                                                                                                                                                                                                                                           
                                    @ITS_JUSTHACKED                                                                                                                                                                                                                                                                                            
''') 
recipient = []
message = str(input("Enter  Your message : "))
data = str(input("Enter  Victum number : "))
recipient.append(data)
sender = str(input("Enter The Calle ID : "))
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

