import random

def criar_lista(condicoes):
    i = 0
    resultado = []
    dic_atual = {}

    criar_dicionario(condicoes, i, resultado, dic_atual)

    return resultado

def total_casos(condicoes):
    total = 2 ** len(condicoes)

    return total

def criar_dicionario(condicoes, i, resultado: list, dic_atual):
    if i == len(condicoes):
        resultado.append(dic_atual.copy())
        return

    condicao = condicoes[i]

    dic_atual[condicao] = True
    criar_dicionario(condicoes, i+1, resultado, dic_atual)

    dic_atual[condicao] = False
    criar_dicionario(condicoes, i+1, resultado, dic_atual)

def exibir_resultados(resultado, total):
    numero = random.randint(0, total)

    for i in range(4):
        numero = random.randint(0, total-1)
        print(f"{resultado[numero]}")
        print()
    
def main():
    condicoes = [
        "Possui comprovante de renda",
        "Sem pendências no CPF",
        "E-mail verificado",
        "Endereço residencial confirmado",
        "Aceitou os termos de uso",
        "Possui biometria cadastrada",
        "Telefone celular validado",
        "Histórico de pagamento em dia"
    ]    

    total = total_casos(condicoes)
    print(f"Total de casos: {total}")
    print()

    resultado = criar_lista(condicoes)
    exibir_resultados(resultado, total)

if __name__ == "__main__":
    main()