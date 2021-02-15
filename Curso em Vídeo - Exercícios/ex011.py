la = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
print('Sua parede tem uma dimensão de  \033[34m{}\033[m x  \033[34m{}\033[m e sua área é \033[30;47m{:.1f}m²\033[m'
      .format(la, a, la*a))
print('Para pintar essa parede será necessário \033[4;31m{:.1f}l\033[m de tinta.'.format((la*a)/2))
