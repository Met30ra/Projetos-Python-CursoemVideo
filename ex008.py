m = float(input('Digite o valor em metros: '))
print('A medida \033[4m{}\033[m metros corresponde a: '.format(m))
print('\033[33m{}\033[m km'.format(m/1000))
print('\033[33m{}\033[m hm'.format(m/100))
print('\033[33m{}\033[m dam'.format(m/10))
print('\033[33m{}\033[m dm'.format(m*10))
print('\033[33m{}\033[m cm'.format(m*100))
print('\033[33m{}\033[m mm'.format(m*1000))
