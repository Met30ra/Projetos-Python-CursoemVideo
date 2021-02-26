n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
n = [n1, n2, n3]
sorted(n)
print(f'Maior valor \033[31m{n[0]}\033[m\nMenor valor \033[34m{n[2]}\033[m')
