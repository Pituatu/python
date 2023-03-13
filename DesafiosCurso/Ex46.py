# Refaça o desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
# Faça um programa que leia um número inteiro
# e mostre na tela a sua tabuada.

tabuada = int(input('Digite um número para que a sua tabuada seja exibida: '))
for c in range(1, 11 , 1):
    print(f'{tabuada} x {c} = {tabuada*c}')