from random import randint
from time import sleep
c = randint(0, 2)
o = ('Pedra', 'Papel', 'Tesoura')
j = int(input('[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\nFaça sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
print('¨|'*20)
if c == j:
    print('Empate')
elif c == 0 and j == 1:
    print('Jogador venceu!')
elif c == 0 and j == 2:
    print('Computador venceu!')
elif c == 1 and j == 0:
    print('Jogador venceu!')
elif c == 1 and j == 2:
    print('Jogador venceu!')
elif c == 2 and j == 0:
    print('Jogador  venceu!')
elif c == 2 and j == 1:
    print('Computador venceu!')
print(f'Jogador jogou {o[j]} e computador jogou {o[c]}')
print(',:'*20)



'''from time import sleep
from random import randint
i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
print('[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura')
j = int(input('Faça sua jogada: '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO')
print('¨¬' * 20)
print('Computador jogou {}'.format(i[c]))
print('Jogador jogou {}'.format(i[j]))
print('¨¬' * 20)
if c == 0:
    if j == 0:
        print('Empate')
    elif j == 1:
        print('Jogador vence')
    elif j == 2:
        print('Computador vence')
    else:
        print('Opção inválida')
elif c == 1:
    if j == 0:
        print('Computador vence')
    elif j == 1:
        print('Empate')
    elif j == 2:
        print('Jogador venceu')
    else:
        print('Opção inválida.')
elif c == 2:
    if j == 0:
        print('Jogador venceu')
    elif j == 1:
        print('Computador venceu')
    elif j == 2:
        print('Empate')
    else:
        print('Opção inválida.')
else:
    print('Opção inválida.')'''
