# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto para vê-lo com um desconto de 5%: "))
newpreco = preco - (preco*(5/100))
print(f'O valor original do produto era de {round((preco) , 2)}R$, e com o desconto de 5% o preço ficou', end=" ")
print(f'em {round((newpreco) , 2)}R$. ')