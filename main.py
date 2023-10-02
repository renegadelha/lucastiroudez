#contar quantas vogais existem no nome da pessoa
#asldkaçlskd

nome = input('digite o seu nome MODIF2')
quantidade = 0

for letra in nome:
    if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        quantidade = quantidade + 1

print(f'----------------a quantidade de vogais no nome foi {quantidade}')
