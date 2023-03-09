# Desenvolva um programa que leia o valor de 3 retas
# e diga se elas podem formar um triângulo.
# Para formar um triângulo, a soma de duas das retas
# precisa ser maior que o valor da terceira.
# Caso seja possível formar uam reta, informe que tipo
# de triângulo será formado:
# Equilátero: 3 lados iguais.
# Isósceles: 2 lados iguais.
# Escaleno: nenhum lado igual.

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('As três retas podem formar um triângulo. ')
    if r1 == r2 and r1 == r3:
        print('O triângulo formado é equilátero. ')
    if r1 == r2 and r1 != r3:
        print('O triângulo formado é isósceles. ')
    if r1 != r2 and r1 == r3:
        print('O triângulo formado é isósceles.')
    if r2 == r3 and r2 != r1:
        print('O triângulo formado é isósceles.')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo formado é escaleno.')
else:
    print('Essas três retas não podem formar um triângulo. ')