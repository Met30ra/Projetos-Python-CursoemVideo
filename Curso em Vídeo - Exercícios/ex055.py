g = m = p = float(input('Peso da 1º pessoa: '))
for c in range(2, 6):
    p = float(input(f'Peso da {c}º pessoa: '))
    if p > g:
        g = p
    elif p < m:
        m = p
print(f'A pessoa mais magra pesa {m:.1f} e a mais gorda pesa {g:.1f}')
