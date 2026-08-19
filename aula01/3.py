def inverte(string: str):
    inverso = ""
    pilha = []
   
    for letra in string:
        pilha.append(letra)

    for letra in string:
        caracatere = pilha.pop()
        inverso += caracatere

    return inverso

while True:
    string = input("String: ")
    nova = []
    nova = inverte(string)
    invertida = "".join(nova)
    print(invertida)