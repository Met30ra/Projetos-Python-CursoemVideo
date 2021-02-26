s = float(input('Salário do funcionário: '))
if s > 1250:
    a = (s * 10) / 100
else:
    a = (s * 15) / 100
print(f'Quem ganhava R$: {s:.2f} passará a ganhar R$: {s+a:.2f}')
