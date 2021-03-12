n = (int(input('1º número: ')), int(input('2º número: ')), int(input('3º número: ')),
     int(input('4º número: ')))
print(f'O 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O 3 apareceu pela primeira vez na {n.index(3)+1}º posição')
else:
    print('O valor 3 não foi informado')
print('Os valores pares são: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
