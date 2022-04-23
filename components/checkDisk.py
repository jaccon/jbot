import os

current = os.getcwd()

from telegramBot import telegram_bot_sendtext

server01 = "192.168.1.1"

os.system("echo 'Disk Status' > " + current + "/temps/disk.1.log")
os.system("echo 'ARM Server' >> " + current + "/temps/disk.1.log")
os.system("df -h |grep /mnt/disk1 >> " + current + "/temps/disk.1.log")

os.system("echo '' >> " + current + "/temps/disk.1.log")
os.system("echo 'Server4You Server' >> " + current + "/temps/disk.1.log")
os.system("ssh root@"+ server01 + 'df -h |grep sd' >> " + current + "/temps/disk.1.log")


send_string = os.system("cat " + current + "/temps/disk.1.log")
f = open(current + "/temps/disk.1.log", "r")
send_string = f.read()

telegram_bot_sendtext(send_string)


