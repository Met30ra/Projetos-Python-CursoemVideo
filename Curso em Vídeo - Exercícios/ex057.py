s = str(input('Informe seu sexo[M/F]: ')).upper()
while s[0] not in 'FM':
    print('Informação inválida, tente novamente.')
    s = str(input('Informe seu sexo[M/F]: ')).upper()
print('Sexo masculino registrado' if s[0] == 'M' else 'Sexo feminino registrado.')
