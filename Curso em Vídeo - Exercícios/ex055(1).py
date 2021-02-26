lis = []
for x in range(1, 6):
    p = float(input('Digite o peso da {}º pessoa: '.format(x)))
    lis += [p]
print('O menor peso é {}\nO maior peso é {}'.format(min(lis), max(lis)))
