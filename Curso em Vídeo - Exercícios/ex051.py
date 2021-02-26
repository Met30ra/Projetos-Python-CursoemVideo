n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print(n, end=' → ')
    n += r
print('Fim')
