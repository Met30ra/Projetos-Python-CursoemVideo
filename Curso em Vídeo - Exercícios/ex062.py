n = int(input('Digite um número: '))
r = int(input('Razão: '))
m = 10
t = 0
while m != 0:
    for c in range(0, m):
        print(n, end=' → ')
        t += 1
        n += r
    print('Pausa')
    m = int(input('\nQuantos termos a mais?: '))
print(f'Foram mostrados no total {t} termos.')
