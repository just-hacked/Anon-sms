import octopush
from octopush import SMS
from config import config
sms = SMS(config['user_login'], config['api_key'])
sms_balance = sms.get_balance()
for balance in sms_balance.findall('balance'):
    pass