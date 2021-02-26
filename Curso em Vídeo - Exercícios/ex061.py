print('10 termos de um PA')
n = int(input('Digite um número: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    c += 1
    print(n, end=' → ')
    n += r
print('Fim do programa.')
