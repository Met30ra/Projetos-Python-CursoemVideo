n = str(input('Digite seu nome completo: ')).strip()
d = n.split()
print(f'Primeiro nome: \033[32m{d[0]}\033[m')
print(f'Último nome: \033[32m{d[len(d)-1]}\033[m')
