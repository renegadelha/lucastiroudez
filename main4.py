#faça um algoritmo em python para repor as perdas com inflação anual (IPCA=4,5%) por 10 anos. Ao final de cada ano,
#o programa deve dizer quanto foi o valor total de salários recebidos pelo funcionário.
#aumenta de 4 em 4 anos

salario = float(input('digite seu salario'))


for ano in range(2024, 2035, 4):
    novo_salario = round((salario * 13) * 1.045, 2)
    mensal = round(novo_salario / 13, 2)

    print(f'no ano de {ano} eu recebi ao total {novo_salario}, ao mês fiquei recebendo {mensal}')
    salario = mensal


