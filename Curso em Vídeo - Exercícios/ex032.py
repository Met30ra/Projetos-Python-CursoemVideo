from datetime import date
a = int(input('Qual ano quer analisar? Digite 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano \033[32;1;1m{a} é Bissexto\033[0m')
else:
    print(f'O ano \033[31;1;1m {a} não é Bissexto\033[0m')
