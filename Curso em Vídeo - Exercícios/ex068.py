from random import randint
cv = 0
while True:
    c = randint(0, 11)
    pi = str(input('Par ou Ímpar?[P/I]: ')).upper()
    j = int(input('Sua jogada: '))
    v = c + j
    print(f'Você jogou {j} e o computador jogou {c}')
    if pi[0] == 'I' and v % 2 != 0:
        cv += 1
        print('Você venceu!\nVamos jogar novamente...')
    elif pi[0] == 'P' and v % 2 == 0:
        cv += 1
        print('Você venceu!\nVamos jogar novamente...')
    elif pi[0] == 'I' and v % 2 == 0:
        break
    elif pi[0] == 'P' and v % 2 != 0:
        break
    print('_'*20)
print('-'*20)
print(f'Computador venceu!\nVocê venceu {cv} vez(s)')
