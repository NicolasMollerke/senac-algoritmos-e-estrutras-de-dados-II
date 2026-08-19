'''Dado um vetor/lista de inteiros, escreva um algoritmo que retorna uma nova lista
apenas com os números não-negativos.'''

def positivos(vetor: int):
    novoVetor = []
    
    for num in vetor:
        if num > 0:
            novoVetor.append(num)

    return novoVetor

while True:
    vetor = [-1,-2,-3,1,2,3,4,5]
    novoVetor = []
    novoVetor = positivos(vetor)
    print(novoVetor)
    break
