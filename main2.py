#contar quantas consoantes existem no nome da pessoa

nome = input('digite o seu nome')
quantidade = 0

for letra in nome:
    if(not (letra == ' ' or letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u')):
        quantidade = quantidade + 1

print(f'a quantidade de vogais no nome foi {quantidade}')
