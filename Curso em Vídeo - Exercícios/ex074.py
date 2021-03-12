from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Valores sorteados: ', end='')
for c in n:
    print(c, end=' ')
print(f'\nMaior valor: {max(n)}\nMenor valor: {min(n)}')
