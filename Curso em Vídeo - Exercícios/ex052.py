d = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    print(c, end=' ')
    if n % c == 0:
        d += 1
print(f'\nO número {n} é divisível {d} vezes,', end=' ')
if d == 2:
    print('logo, é primo')
else:
    print('logo não é primo')
