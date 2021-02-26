n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Média: {m:.1f}')
if m < 5:
    print('\033[31mREPROVADO\033[m')
elif 5 <= m <= 6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
elif m >= 7:
    print('\033[32mAPROVADO')
