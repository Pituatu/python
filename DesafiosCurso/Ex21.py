# Crie um programa que leia o nome de uma cidade e diga
# se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade que deseja analisar: ')).upper().strip()
saint = (cidade.split())
if saint[0] == "SANTO":
    print("O nome da cidade começa com SANTO. ")
else:
    print("O nome da cidade não começa com SANTO. ")