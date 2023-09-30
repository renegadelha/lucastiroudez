import random

for i in range(3):
    numero = int(input('digite um numero inteiro entre 1 e 10'))

    aleatorio = random.randint(1, 10)

    if(numero == aleatorio):
        print('PARABENS, voce acertou!')
        break
    else:
        print(f'voce errou. O numero aleatorio era {aleatorio}')

print('programa encerrado')