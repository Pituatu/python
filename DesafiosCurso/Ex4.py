# Faça um programa que leia um número, e mostre
# o seu sucessor e o seu antecessor.

n1 = int(input("Digite um número para descobrir seu antecessor e o seu sucessor: "))
n2 = (n1 + 1)
n3 = (n1 - 1)
print(f'O antecessor de \033[1;32m{n1}\033[m é \033[1;33m{n3}\033[m. ')
print(f'O sucessor de \033[1;32m{n1}\033[m é \033[1;34m{n2}\033[m. ')