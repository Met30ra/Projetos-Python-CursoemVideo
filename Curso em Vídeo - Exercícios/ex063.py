t1 = 0
t2 = 1
t3 = 0
c = 2
print('¨¬'*15)
print('Sequência de fibonnacci')
print('-_'*15)
n = int(input('Quantidade de termos: '))
print(f'{t1} → {t2}', end=' → ')
while c < n:
    c += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3} → ', end='')
print('Fim do programa.')
