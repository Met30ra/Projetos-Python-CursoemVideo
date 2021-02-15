from random import randint
from time import sleep
c = randint(0, 5)
print('\033[34m.-\033[m'*20)
print('Vou pensar em um número entre 1 e 5, tente adivinhar...')
print('\033[34m_,\033[m'*20)
n = int(input('Em qual número eu pensei? '))
print('\033[37mProcessando...\033[m')
sleep(1.5)
if n == c:
    print('\033[32mCorreto!\033[m Você acertou!')
else:
    print(f'\033[31mErrado!\033[m Eu pensei no número \033[33m{c}\033[m e não no \033[36m{n}\033[m')
