n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
me = n1
ma = n1
if n2 > ma:
    ma = n2
if n3 > ma:
    ma = n3
if n2 < me:
    me = n2
if n3 < me:
    me = n3
print(f'Maior valor digitado \033[1;34m{ma}\033[m\nMenor valor digitado \033[1;34m{me}')
