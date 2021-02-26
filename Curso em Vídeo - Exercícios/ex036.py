c = float(input('Valor da casa: '))
s = float(input('Informe seu salário: '))
a = int(input('Em quantos anos pretende pagar?: '))
p = c / (a*12)
if p <= (s * 30) / 100:
    print(f'Empréstimo concedido. Você pagará R$ {p:.2f} mensais.')
else:
    print(f'Pagando uma casa de R$ {c:.2f} em {a} anos, a prestação custará {p}, que exede 30% de seu salário.\n'
          f'Empréstimo negado.')
