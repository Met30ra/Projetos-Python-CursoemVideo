d = int(input('Dias alugados: '))
km = float(input('Km percorridos: '))
p = (d * 60) + (km * 0.15)
print('O total a pagar é R$: \033[1;35m{:.2f}\033[m'.format(p))
