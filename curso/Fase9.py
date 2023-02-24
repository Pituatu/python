# Manipulando cadeias de textos

frase: str = "Sopre como nunca, Vendaval Eterno!"
print(len(frase))
# função len analisa o comprimento da frase.
print(frase.count('o'))
# função count analisa quantas letras x tem na variável.
print(frase.find('Eterno'))
# função find mostra onde é o início da frase desejada, nesse caso, no espaço 27. Caso o valor retornado seja -1,
# significa que a frase buscada não existe na variável.
print('Vendaval' in frase)
# Mostra se existe a palavra procurada na variável, caso a resposta seja sim, retorna o valor True, e caso não,
# retorna o valor False.
print(frase.replace('Vendaval', 'Fogo'))
# Troca a palavra antiga por outra desejada.

# a função .upper() transforma a frase em maiúscula, e .lower() transforma a frase em minúscula.

# função .capitalize() Transforma todos os caracteres, com exceção do primeiro em minúsculos. E transforma a
# primeira letra em maiúsculo.

# função .title() analisa quantas palavras existem na string e transforma a primeira letra das palavras
# divididas entre espaços em palavras.

# função .strip() remove espaços inúteis no inicío e no final da string.
# função .rstrip() remove somente os espaços inúteis do lado direito da string.
# função .lstrip() remove somente os espaços inúteis do lado esquerdo da string.

# função .split() divide as palavras da frase em uma lista, sendo esses splits definidos pelos espaços
# entre as palavras.

# função '-'.join(frase) juntaria as frases com um - especificado entre aspas.




