import os
import sys
import time
import requests

rq = requests
server = sys.argv[2]

cwd = os.getcwd()

def reader(server):
	while True:
		print("Loading messages from "+server)
		print(rq.get(server).text)
		os.system("clear")
		time.sleep(5)

def sender(server):
	username = sys.argv[1]
	while True:
		msg = input("> ")
		fullMsg = username + " : " + msg
		rq.get(server + "process.php/d=" + fullMsg)
		time.sleep(1)

if sys.argv[1] != "reader":
	os.system('xterm -title "Reader" -e "python3 airtalk.py reader '+server+'"')
	sender(server)
else:
	reader(server)