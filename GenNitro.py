import requests
from threading import Thread
import time 
import itertools
import string

def GenNitro(sstr):
    nitro = "https://discord.gift/{}".format(sstr)
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{sstr}?with_application=false&with_subscription_plan=true"
    response = requests.get(url) 
    if response.status_code == 200: 
        print(f"Successful || {nitro}") 
        exit()
    else:
        print(f'Error || {nitro}')



def generate_combinations(length=16):
    characters = string.ascii_letters + string.digits
    for combination in itertools.product(characters, repeat=length):
        yield ''.join(combination)

combinations_generator = generate_combinations()
print('''
        Made By Wirilless
            
        GenNitro V1
        ''')
time.sleep(1)
input("Pressione Enter para continuar...")

while True:
    try:
        

        current_combination = next(combinations_generator)
        processo = Thread(target=GenNitro(current_combination))
        processo.start()
        processo.join()

    except KeyboardInterrupt:
        print("KeyBoardInterrupt")
        exit()
        
        
