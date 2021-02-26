v = float(input('Valor do prouduto: '))
print('[ 1 ] À vista/Cheque\n[ 2 ] À vista no cartão\n[ 3 ] Em até 2x nor cartão\n[ 4 ] 3x ou mais no cartão')
p = int(input('Selecione a forma de pagamento: '))
if p == 1:
    d = (v*10)/100
    print(f'Valor final do produto com 10% de desconto: R$ {v-d:.2f}')
elif p == 2:
    d = (v*5)/100
    print(f'O valor final do produto 5% de desconto: R$ {v-d:.2f}')
elif p == 3:
    print(f'O valor final do produto: R$ {v:.2f}')
elif p == 4:
    j = (v*20)/100
    pa = int(input('Número de parcelas: '))
    print(f'O valor final do produto parcelado em {pa}x com 20% de juros: R$ {v+j:.2f}')
else:
    print('Opção inválida, tente novamente.')


'''v = float(input('Informe o valor da compra R$: '))
print('[ 1 ] À vista/Cheque\n[ 2 ] À vista no cartão\n''[ 3 ] Em até 2x no cartão\n[ 4 ] 3x ou mais no cartão')
p = int(input('Informe a forma de pagamento: '))
if p == 1:
    print('Valor final da compra com 10% de desconto: R$ {:.2f}'.format(v - (v * 10 / 100)))
elif p == 2:
    print('O valor final da compra com 5% desconto: R$ {:.2f}'.format(v - (v * 5 / 100)))
elif p == 3:
    print('O valor final em até 2x no cartão: R$ {}'.format(v))
elif p == 4:
    n = int(input('Número de parcelas: '))
    print('O valor final da compra parcelado em {} vezes com 20% de juros: R$ {:.2f}'.format(n, v + (v * 20 / 100)))
else:
    print('Opção inválida. Tente novamente.')'''
