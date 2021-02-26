c = 1
s = ma = me = n = int(input('Digite um número: '))
r = str(input('Quer continuar?[S/N]: ')).upper()
while r[0] != 'N':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar?[S/N]: ')).upper()
    c += 1
    s += n
    if n > ma:
        ma = n
    elif n < me:
        me = n
print(f'Você digitou {c} números, sua média é {s/c:.1f}\nO maior valor digitado foi {ma} e o menor {me}')

'''c = m = ma = me = 0
r = 'S'
while r in 'Ss':
    n = int(input('Digite um número: '))
    c += 1
    m += n
    if c == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        elif n < me:
            me = n
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
print('Você digitou {} números e a média foi {}'.format(c, m/c))
print('O maior valor digitado foi {} e o menor foi {}'.format(ma, me))'''
