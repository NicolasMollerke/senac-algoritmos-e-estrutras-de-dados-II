from multiprocessing import Pool
import time

def radix(vetor):
    maior = max(vetor)
    listas = [[] for i in range(10)]

    vetorFormatado = formatar_vetor(vetor, maior)

    for num in vetorFormatado:
        digito = int(num[0])
        listas[digito].append(num)

    with Pool() as pool:
        listas_ordenadas = pool.map(merge_sort, listas)

    vetor_ordenado = []
    for lista in listas_ordenadas:
        vetor_ordenado.extend(lista)

    vetor_ordenado = [int(num) for num in vetor_ordenado]

    return vetor_ordenado


def formatar_vetor(vetor, maior):
    vetor_formatado = [0] * len(vetor)
    i = 0
    
    for num in vetor:
        if len(str(num)) <= len(str(maior)):
            num = str(num).zfill(len(str(maior)))
        vetor_formatado[i] = num
        i = i + 1

    return vetor_formatado

        

def merge_sort(vetor):
    if len(vetor) > 1:
        mid = len(vetor) // 2
        left_half = vetor[:mid]  
        right_half = vetor[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
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


def max(vetor):
    maior = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]

    return maior
    

def verificaOrdem(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False

    return True
    


def main():
    tempo_inicial = time.time()

    vetor = []


    with open("numeros_100M_embaralhado.csv", "r") as f:
        for linha in f:
            valor_limpo = linha.strip()
            
            if valor_limpo.isdigit():
                vetor.append(int(valor_limpo))

    vetorOrdenando = radix(vetor)


    tempo_final = time.time()
    duracao = int(tempo_final - tempo_inicial)
    min = duracao / 60

    print(verificaOrdem(vetorOrdenando))
    
    print(f"{duracao} segundos")
    print(f"{min:.2f} minutos")

if __name__ == "__main__":
    main()
    
