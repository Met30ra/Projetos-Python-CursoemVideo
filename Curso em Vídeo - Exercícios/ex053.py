f = str(input('Digite algo: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for le in range(len(j)-1, -1, -1):
    i += j[le]
print('O inverso de {} é {}'.format(j, i))
if i == j:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')
