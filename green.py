import os, platform;from time import sleep
try:
   import requests
except:
   os.system('pip install requests')


import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    print ('WELCOME 64 BIT USER..!')
    sleep (2)
    from green import main_apv
    main_apv()

elif bit == '32bit':
    os.system('clear')
    print('WELCOME 32 BIT USER..!')
    sleep (2)
    from green32 import main_apv
    main_apv()
