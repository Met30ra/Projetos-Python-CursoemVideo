from datetime import date
a = date.today().year
n = int(input('Ano de nascimento: '))
i = a - n
if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:
    print('Classificação: INFANTIL')
elif i <= 19:
    print('Classsificação: JÚNIOR')
elif i <= 25:
    print('Classificação: SÊNIOR')
elif i > 25:
    print('Classificação: MASTER')
