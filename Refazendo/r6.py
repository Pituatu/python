# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a média.
soma = 0
contador = 0
for c in range(1,3):
    nota = float(input(f'Digite a {c}ª nota: '))
    soma = soma + nota
    contador = contador + 1
print(f'A média aritmética do aluno é igual a {soma/contador}')