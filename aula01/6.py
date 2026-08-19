'''Implemente uma função que recebe uma lista de números e retorna uma nova lista
sem elementos repetidos, usando conjuntos (set)'''

def removerRepetidos(vetor: int):
    conjunto = set(vetor)

    return conjunto

while True:
    vetor = [1,1,1,2,3,4,5]
    conjunto = removerRepetidos(vetor)
    print(conjunto)
    break