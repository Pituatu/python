## Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de Km percorridos com o carro: '))
dias = int(input('Digite a quantidade de dias pelos quais ele foi alugado: '))
totkm = float(km*0.15)
totdias = int(dias*60)
print(f'Por ter percorrido {km}Km o preço pela corrida é {totdias} reais.')
print(f'Por ter utilizado o carro por {dias} dias o preço da diária ficou em {totdias} reais.')
print(f'Totalizado o valor de {round(totdias + totkm)} reais. ')