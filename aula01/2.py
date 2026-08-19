'''Implemente uma função que recebe uma string e retorna a mesma string com todas
as vogais substituídas por ‘*’'''

def substitui(string: str):
    nova = ""

    for letra in string:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            nova += '*'
        else:
            nova += letra    
    return nova



while True:
    string = input("String: ")
    nova = substitui(string)
    print(nova)