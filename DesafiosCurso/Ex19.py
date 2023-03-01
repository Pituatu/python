# Um professor quer sortear a ordem de apresentação dos
# seus alunos. Faça um programa que leia o nome dos 4
# alunos e leia a ordem sorteada.

from random import shuffle
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto Aluno: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print(f'A ordem de apresentação dos trabalhos é {lista}')