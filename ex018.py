from math import cos, sin, tan, radians
a = float(input('Digite o valor do ângulo: '))
c = cos(radians(a))
s = sin(radians(a))
t = tan(radians(a))
print(f'O ângulo de {a:.2f} tem o coseno de {c:.2f}\nSeno {s:.2f}\nTangente {t:.2f}')
