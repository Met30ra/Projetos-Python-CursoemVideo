while True:
    t = int(input('Quer ver a tabuada de qual número?: '))
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {t} = {c*t}')
    print('_~'*18)
