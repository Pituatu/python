# Crie um progama que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando
# os espaços.

frase = str(input('Digite uma frase para saber se ela é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo. ')
else:
    print('Não é um palíndromo. ')

