a = cp = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        a += n
        cp += 1
print(f'Foram digitados {cp} números pares e sua soma é {a}')
