import threading
import time

def radix(vetor):
    maior = max(vetor)
    listas = [[] for _ in range(10)]

    vetorFormatado = formatar_vetor(vetor, maior)

    for num in vetorFormatado:
        digito = int(num[0])
        listas[digito].append(num)

    unidade = "1" + ("0" * (len(str(maior)) - 1))

    threads = []

    for i in range(10):
        t = threading.Thread(target=merge_sort, args=(listas[i], unidade))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    vetor_ordenado = []
    for lista in listas:
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

        

def merge_sort(vetor, unidade):
    if len(vetor) > 1:
        mid = len(vetor) // 2
        left_half = vetor[:mid]  
        right_half = vetor[mid:]

        merge_sort(left_half, unidade)
        merge_sort(right_half, unidade)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            div1 = int(left_half[i]) / int(unidade)
            digito1 = div1 % 10

            div2 = int(right_half[j]) / int(unidade)
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


    with open("numeros_1M_embaralhado.csv", "r") as f:
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
    