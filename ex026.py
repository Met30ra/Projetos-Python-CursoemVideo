f = str(input('Digite uma frase: ')).strip().upper()
print('A letra \033[35mA\033[m aparece \033[34m{}\033[m vezes '.format(f.count('A')))
print('A Letra \033[35mA\033[m aparece pela 1º vez na posição \033[34m{}\033[m'.format(f.find('A')+1))
print('A letra \033[35mA\033[m aparece pela última vez na posição \033[34m{}\033[m'.format(f.rfind('A')+1))
