mi = ihv = mmv = 0
nhv = ''
for c in range(1, 5):
    print(f'{c}º pessoa')
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo[M/F]: ')).upper()
    mi += i
    if s[0] == 'M':
        if i > ihv:
            ihv = i
            nhv = n
    if s[0] == 'F':
        if i < 20:
            mmv += 1
    print('¨'*20)
print(f'A média da idade do grupo é {mi/4:.1f}\nO homem mais velho é {nhv}\n{mmv} mulheres tem menos de 20 anos.')
