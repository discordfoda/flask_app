import random
import string
import requests
from threading import Thread
import time 


def GenNitro():
    nitro = "https://discord.gift/{}".format(String())
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
    response = requests.get(url) 
    if response.status_code == 200: 
        print(f"Successful || {nitro}")
        exit()
    else:
        print(f'Error || {nitro}')

def String():
    letras = string.ascii_letters + string.digits
    return ''.join(random.choice(letras) for _ in range(16))




try:
    print('''
    Made By Wirilless
          
    GenNitro V1
    ''')
    time.sleep(1)
    input("Pressione Enter para continuar...")
    while True:  
        processo = Thread(target=GenNitro())
        processo.start()

except KeyboardInterrupt:
    print("KeyBoardInterrupt")
    exit()