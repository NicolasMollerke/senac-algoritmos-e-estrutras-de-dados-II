import time

def radix(vetor):
    maior = max(vetor)
    unidade = 1

    for i in str(maior):
        vetor = merge_sort(vetor, unidade)
        unidade = unidade * 10

    return vetor


def max(vetor):
    maior = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]

    return maior

def merge_sort(vetor, unidade):
    if len(vetor) > 1:
        mid = len(vetor) // 2
        left_half = vetor[:mid]  
        right_half = vetor[mid:]

        merge_sort(left_half, unidade)
        merge_sort(right_half, unidade)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            div1 = left_half[i] / unidade
            digito1 = div1 % 10

            div2 = right_half[j] / unidade
            digito2 = div2 % 10

            if digito1 < digito2:
                vetor[k] = left_half[i]
                i += 1
            else:
                vetor[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            vetor[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            vetor[k] = right_half[j]
            j += 1
            k += 1

        return vetor
        

# def bubble_sort(vetor, unidade):
#     n = len(vetor)

#     for i in range(n-1):
#         swapped = False

#         for j in range(0, n-i-1):
#             div1 = vetor[j] / unidade
#             digito1 = div1 % 10

#             div2 = vetor[j+1] / unidade
#             digito2 = div2 % 10

#             if digito1 > digito2:
#                 vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
#                 swapped = True

#         if not swapped:
#             break

#     return vetor

def verificaOrdem(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False

    return True
    


def main():
    tempo_inicial = time.time()

    vetor = [1, 10, 100]

    with open("numeros_1M_embaralhado.csv", "r") as f:
        for linha in f:
            valor_limpo = linha.strip()
            
            if valor_limpo.isdigit():
               vetor.append(int(valor_limpo))
        
    vetor = radix(vetor)
    ordenado = verificaOrdem(vetor)

    tempo_final = time.time()
    duracao = int(tempo_final - tempo_inicial)
    min = duracao / 60

    print(ordenado)
    print(f"{duracao} segundos")
    print(f"{min:.2f} minutos")
    print(vetor)


if __name__ == "__main__":
    main()
    