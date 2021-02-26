from random import randint
c = randint(0, 10)
t = 1
j = int(input('Pensei em um número de 0 a 10, tente adivinhar...\nEm qual número eu pensei?: '))
while j != c:
    if j > c:
        j = int(input('Menos...\nTente denovo: '))
    elif j < c:
        j = int(input('Mais...\nTente denovo: '))
    t += 1
print(f'Acertou! Após {t} tentativas.')
