v = h = mn = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo[M/F]: ')).upper().strip()
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar?[S/N]: ')).upper().strip()
    print('='*25)
    if i > 18:
        v += 1
    if s[0] == 'M':
        h += 1
    if s[0] == 'F' and i < 20:
        mn += 1
    if c[0] == 'N':
        break
print(f'{v} pessoas tem mais de 18 anos\nForam cadastrados {h} homens\n{mn} mulher(s) tem menos de 20 anos')
