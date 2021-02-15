c = float(input('Digite a temperatura em ºC: '))
f = (c * 9/5) + 32
print('\033[31m{}ºC\033[m = \033[4;33m{}ºF'.format(c, f))
