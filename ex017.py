from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = hypot(co, ca)
'''print('A hipotenusa vai medir \033[30;44m{:.2f}\033[m'.format(h))'''
print(f'A hipotenusa vai medir \033[30;44m{h:.2f}\033[m')
