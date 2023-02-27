# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento

salario = float(input("Digite aqui o salário antigo do funcionário: "))
alegria = (salario + (salario*(15/100)))
print(f'O antigo salário do funcionário era {salario}R$, e com o reajuste de ', end="")
print(f'15%, o seu novo salário é de {alegria}R$.')