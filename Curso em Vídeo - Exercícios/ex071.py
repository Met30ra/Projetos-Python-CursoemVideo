c = vi = d = u = 0
v = int(input('Informe o valor a ser sacado: '))
print('Você receberá: \n')
while v >= 50:
    v -= 50
    c += 1
print(f'{c} cédulas de R$50' if c > 0 else False)
while v >= 20:
    v -= 20
    vi += 1
print(f'{vi} cédulas de R$20' if vi > 0 else False)
while v >= 10:
    v -= 10
    d += 1
print(f'{d} cédulas de R$10' if d > 0 else False)
while v >= 1:
    v -= 1
    u += 1
print(f'{u} cédulas de R$1' if u > 0 else False)
