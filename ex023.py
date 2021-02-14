from time import sleep
n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número \033[29;40m{}\033[m...'.format(n))
sleep(0.8)
print(f'Unidade: \033[30;45m{u}\033[m')
print(f'Dezena: \033[30;46m{d}\033[m')
print(f'Centena: \033[30;42m{c}\033[m')
print(f'Milhar: \033[30;41m{m}\033[m')
