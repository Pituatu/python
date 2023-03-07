# Faça um programa que leia um número e mostre
# dobro, triplo e sua raiz quadrada.
import math
n1 = int(input("Digite um número: "))
n2 = (2*n1)
n3 = (3*n1)
n4 = (math.sqrt(n1))
print(f'O dobro de \033[1;35m{n1}\033[m é \033[1;31m{n2}\033[m. ')
print(f'O triplo de \033[1;35m{n1}\033[m é \033[1;34m{n3}\033[m.')
print(f'A raiz quadrada de \033[1;35m{n1}\033[m é \033[1;36m{n4}\033[m. ')