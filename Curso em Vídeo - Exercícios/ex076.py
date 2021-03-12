p = ('Notebook', 2200,
     'Garrafa', 31.90,
     'Dualshock', 250,
     'Headset', 100,
     'Ventilador', 79.90,
     'AirDots', 139.90,
     'Livro: 1984', 36.70,
     'Cortina', 89.90)
for c in range(0, len(p)):
    if c % 2 == 0:
        print(f'{p[c]:.<20}', end='')
    else:
        print(f'R$: {p[c]:>5.2f}')
