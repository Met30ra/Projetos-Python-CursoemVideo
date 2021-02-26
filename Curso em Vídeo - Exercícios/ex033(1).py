n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
n = [n1, n2, n3]
print(f'Maior valor \033[30;42m{max(n)}\033[m\nMenor valor \033[30;41m{min(n)}\033[m')
