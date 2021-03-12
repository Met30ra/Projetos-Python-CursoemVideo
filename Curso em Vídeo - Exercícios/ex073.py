t = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
     'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 'Coritiba', 'Avai',
     'Ponte preta', 'Atletico-go')
print(f'Os 5 primeiros: {t[:5]}')
print('|'*30)
print(f'Os últimos 4 colocados: {t[16:]}')
print('|'*30)
print(sorted(t))
print('|'*30)
print(f'Chapecoense está {t.index("Chapecoense")+1}º posição')
