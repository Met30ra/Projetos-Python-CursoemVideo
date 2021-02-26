f = str(input('Digite algo: ')).strip().upper()
d = f.split()
j = ''.join(d)
i = j[::-1]
print(f'A string digitada ao contrário é {i}')
if j == i:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
