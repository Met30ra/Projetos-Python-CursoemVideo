d = float(input('Distância da viagem: '))
'''if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45'''
v = d * 0.50 if d <= 200 else d * 0.45
print(f'Sua viagem de \033[37;1m{d}\033[mKm terá o valor de R$ \033[1;7;46m{v:.2f}\033[m')
