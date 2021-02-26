s1 = float(input('Primeiro seguimento: '))
s2 = float(input('Segundo seguimento: '))
s3 = float(input('Terceiro segumiento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('O triângulo será Equilátero.')
    elif s1 != s2 != s3 and s1 != s3:
        print('O triângulo será Escaleno.')
    else:
        print('O triângulo será Isóceles.')
else:
    print('Não é possível formar um triângulo')
