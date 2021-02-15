s = float(input('Digite o salário do funcionário:R$ '))
a = (s*15)/100
print('O funcionário que ganhava R$ \033[31m{:.2f}\033[m, com 15% de aumento, passará a ganhar R$ \033[1;36m{:.2f}'
      .format(s, s+a))
