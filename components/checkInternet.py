import os
from datetime import date

from telegramBot import telegram_bot_sendtext

current = os.getcwd()
currentDate = date.today() 

os.system("echo 'Internet Speed' > " + current + "/temps/speed.1.log")

os.system("curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python - > " + current + "/temps/speed.log")

os.system("cat " + current + "/temps/speed.log |grep 'Testing from' >> " + current + "/temps/speed.1.log")
os.system("cat " + current + "/temps/speed.log |grep Download >> " + current + "/temps/speed.1.log")
os.system("cat " + current + "/temps/speed.log |grep Upload >>" + current + "/temps/speed.1.log")

send_string = os.system("cat " + current + "/temps/speed.1.log")

f = open(current + "/temps/speed.1.log", "r")
send_string = f.read()

print(send_string)

telegram_bot_sendtext(send_string)
