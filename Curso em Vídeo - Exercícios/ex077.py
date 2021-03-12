letra = ' '
p = ('Cortador', 'Fone', 'Lamina', 'Mesa', 'Cadeado', 'Tela', 'Alma', 'Vazio')
for c in p:
    print(f'\n{c} tem as vogais:', end=' ')
    for letra in c.upper():
        if letra in 'AEIOU':
            print(letra, end=' ')
