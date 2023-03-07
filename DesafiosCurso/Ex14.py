# Escreva um programa que pergunte a quantidade de
# Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o
# preço a pagar, sabendo que o carro custa R$60
# por dia e R$0.15 por Km rodado.

km = float(input("Digite a quantidade de Km rodados: "))
dia = int(input('Digite a quantidade de dias que ele foi alugado: '))
total_km = (km * 0.15)
total_dia = (dia * 60)
preco = (total_km + total_dia)
print(f'O preço a ser pago vai ser de \033[1;32mR${preco}\033[m. ')