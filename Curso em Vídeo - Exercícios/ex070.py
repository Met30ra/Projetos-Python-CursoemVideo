t = mm = pb = 0
con = 1
nb = ' '
while True:
    np = str(input('Nome do produto: ')).strip().title()
    p = float(input('Valor do produto R$: '))
    c = ' '
    t += p
    while c not in 'SN':
        c = str(input('Há mais produtos?[S/N]: ')).upper()
    print('+'*20)
    if con == 1 or p < pb:
        pb = p
        nb = np
        con += 1
    if p > 1000:
        mm += 1
    if c[0] == 'N':
        break
print(f'Total gasto na compra R$: {t:.2f}\n{mm} produtos custam mais de R$ 1000,00\nNome do produto mais barato: {nb}')
