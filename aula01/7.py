'''Dada uma frase, escreva um algoritmo que conte quantas vezes cada palavra
aparece, retornando um dicionário com o resultado'''

def conta(string: str):
    partes = string.split(" ")

    dicionario = {}
    for parte in partes:
        palavra = parte
        
        dicionario[palavra] = dicionario.get(palavra, 0) + 1

    return dicionario

while True:
    string = input("String: ")
    dicionario = conta(string)
    print(dicionario)