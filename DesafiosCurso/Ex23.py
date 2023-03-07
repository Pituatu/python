# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece "A":
# Em que posição ela aparece pela primeira vez:
# Em que posição ela aparece pela última vez:

frase = str(input("Digite uma frase: ")).upper().strip()
frase = frase.replace('Á', 'A')
frase = frase.replace('Ã', 'A')
frase = frase.replace('À', 'A')
print(f"A letra A aparece {frase.count('A')} vezes. ")
print(f"A letra A aparece pela primeira vez na posição {frase.find('A')+1}. ")
print(f"A Letra A aparece pela primeira vez na posição {frase.rfind('A')+1}. ")

