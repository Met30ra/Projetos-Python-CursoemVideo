from datetime import date
a = date.today().year
s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
if s[0] == 'M':
    n = int(input('Ano de nascimento: '))
    i = a - n
    if i < 18:
        print(f'Ainda faltam {18-i} ano(s) para seu alistamento\nSeu alistamento será em {n+18}.')
    elif i == 18:
        print(f'Quem nasceu em {n} tem 18 anos em {a} e deve se alistar imediatamente.')
    elif i > 18:
        print(f'Você já deveria ter se alistado há {i-18} anos\nSeu alistamento foi em {n+18}.')
else:
    print('Você não precisa participar do alistamento militar.')
