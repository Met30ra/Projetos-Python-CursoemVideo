'''n = int(input('Digite um número para caucular seu fatorial: '))
c = n
f = 1
print(f'Cauculando {n}!= ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f, end='')'''

f = 1
n = int(input('Digite um número para caucular se fatorial: '))
c = n
print(f'Cauculando {n}!= ', end='')
for c in range(c, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)
