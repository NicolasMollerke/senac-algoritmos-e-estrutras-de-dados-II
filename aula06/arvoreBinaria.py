valores = [10,5,2,7,15,12,20]

class Node():
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

    def inserir(self, raiz, valor):
        if raiz is None:
            return Node(valor)
        if valor < raiz.valor:
            raiz.esq = self.inserir(raiz.esq, valor)
        else:
            raiz.dir = self.inserir(raiz.dir, valor)
        return raiz


    def preOrdem(self):
        print(self.valor)
        if self.esq:
            self.esq.preOrdem()    
        if self.dir:
            self.dir.preOrdem()
            

    def posOrdem(self):
        if self.esq:
            self.esq.posOrdem()    
        if self.dir:
            self.dir.posOrdem()

        print(self.valor)

    def emOrdem(self):
        if self.esq:
            self.esq.emOrdem()    
        print(self.valor)
        if self.dir:
            self.dir.emOrdem()

def main():
    valores = [10,5,2,7,15,12,20]

    tree = Node(valores[0])

    for valor in valores[1:]:
        tree = tree.inserir(tree, valor)

    print("--Pré Ordem---")
    tree.preOrdem()

    print("--Pós Ordem---")
    tree.posOrdem()

    print("---Em Ordem---")
    tree.emOrdem()
    


if __name__ == "__main__":
    main()


# print(f"Raiz: {tree.valor}, Valor da Esquerda da Raiz {tree.esq.valor}, Valor da Direita da Raiz {tree.dir.valor}")