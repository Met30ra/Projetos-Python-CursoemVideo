e = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
c = ' '
while c != 'N':
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        print('Opção inválida, tente novamente')
        n = int(input('Digite um número entre 0 e 20: '))
    print(f'{n} por extenso é {e[n]}')
    c = str(input('Quer continuar?[S/N]: ')).upper()
