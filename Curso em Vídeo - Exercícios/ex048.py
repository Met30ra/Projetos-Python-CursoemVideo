s = co = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        co += 1
        s += c
print(f'A soma dos {co} valores é {s}')

'''s = t = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        t += 1
        s += c
print(f'A soma dos {t} valores é {s}')'''
