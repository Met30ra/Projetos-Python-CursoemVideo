from datetime import date
j = v = 0
a = date.today().year
for c in range(1, 8):
    n = int(input(f'Ano de nascimento da {c}º pessoa: '))
    if a - n < 18:
        j += 1
    else:
        v += 1
print(f'{j} pessoas menores de idade e {v} maiores de idade.')
