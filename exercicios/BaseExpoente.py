#Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
# 7² = 7x7/ 7³ = 7x7x7/

base = int(input("Base: "))
expoente = int(input("Expoente: "))
potencia = 1
for contador in range(expoente):
    potencia = potencia*base
    contador += 1
print(base,"^",expoente,"=",potencia)