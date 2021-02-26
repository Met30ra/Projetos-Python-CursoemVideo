n = int(input('Digite um número inteiro: '))
print('[ 1 ]Binário\n[ 2 ]Octal\n[ 3 ]Hexadecimal')
c = int(input('Escolha a base de conversão: '))
if c == 1:
    print(f'{n} em Binário é {bin(n)[2:]}')
elif c == 2:
    print(f'{n} em Octal é {oct(n)[2:]}')
elif c == 3:
    print(f'{n} em Hexadecimal é {hex(n)[2:]}')
else:
    print('Opção inválida')
