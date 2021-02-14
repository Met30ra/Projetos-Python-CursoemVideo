from random import randint
from time import sleep
v = randint(10, 180)
print('Seu carro passou no radar 🚗...')
print('Aguarde...')
sleep(2)
if v > 80:
    print(f'\033[31mMultado!\033[m Você exedeu o limite de \033[32m80Km\033[m.\n'
          f'Total a pagar: R$ \033[33m{(v-80)*7:.2f}\033[m')
print('Tenha um bom dia, dirija com segurança')
