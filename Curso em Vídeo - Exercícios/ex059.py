from time import sleep
o = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while o != 5:
    print('´.'*15)
    o = int(input('[ 1 ]Somar\n[ 2 ]Multiplicar\n[ 3 ]Maior\n[ 4 ]Novos números\n[ 5 ]Sair\nEscolha uma opção: '))
    print('_,'*15)
    if o == 1:
        print(f'{v1} + {v2} = {v1+v2}')
    elif o == 2:
        print(f'{v1} x {v2} = {v1*v2}')
    elif o == 3:
        if v1 > v2:
            print(f'O maior valor é {v2}')
        elif v2 > v1:
            print(f'O maior valor é {v2}')
        else:
            print('Os valores são iguis.')
    elif o == 4:
        v1 = int(input('Novos valores\nPrimeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif o == 5:
        sleep(1.3)
        print('Fim do programa.')
    else:
        print('Opção inválida, tente novamente.')
