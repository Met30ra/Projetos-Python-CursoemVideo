n = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas: \033[32m{n.upper()}\033[m')
print(f'Seu nome em minúsculas: \033[32m{n.lower()}\033[m')
print('Seu nome tem no total \033[32m{}\033[m letras'.format(len(n)-n.count(' ')))
d = n.split()
print(f'Seu 1º nome é \033[32m{d[0]}\033[m e possúi \033[32m{len(d[0])}\033[m letras')
