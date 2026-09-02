def InterpolationSearch(vetor: list, target: int) -> int:
    low = 0
    high = len(vetor) - 1

    while low <= high and target >= vetor[low] and target <= vetor[high]:
        if vetor[low] == vetor[high]:
            if vetor[low] == target:
                return vetor[low]
            else:
                return -1

        pos = low + ((target - vetor[low]) * (high - low)) // (vetor[high] - vetor[low])

        if vetor[pos] == target:
            return pos
        elif vetor[pos] < target:
            low = pos + 1
        elif vetor[pos] > target:
            high = pos -1

def Teste(valor: int, target: int):
    if valor == target:
        return True
    return False


def main():
    vetor = [10, 20, 30, 40, 1000]
    pos = 0
    target = 30

    
    pos = InterpolationSearch(vetor, target)
    print(Teste(vetor[pos], target))


if __name__ == "__main__":
    main()

#a) Ela não procura no meio pois através de uma fórmula matemática ela consegue calcular se o numero esta mais perto do extremo menor ou maior.
#b) Ela funciona melhor quando os dados crecem de forma igual, por exemplo [10, 20, 30].
#c) O pior caso ocorre quando o crescimento é muito desigual entre os número, resultando em um High muito grande. Isso faz com que o cálculo de posições avance de 1 em 1 fazendo com que todo vetor seja percorrido.
    