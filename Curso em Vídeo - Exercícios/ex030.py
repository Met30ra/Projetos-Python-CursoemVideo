n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'O número {n} é\033[36;1m PAR\033[m')
else:
    print(f'O número {n} é\033[36;1m ÍMPAR\033[m')
