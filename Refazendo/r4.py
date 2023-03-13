# Faça um programa que leia um número inteiro e mostre seu antecessor e o seu sucessor.

numero = int(input('Digite um número para descobrir o seu antecessor e o seu sucessor: '))
print(f'O antecessor de \033[32m{numero}\033[m é \033[34m{numero - 1}\033[m. ')
print(f'O sucessor de \033[32m{numero}\033[m é \033[36m{numero + 1}\033[m. ')