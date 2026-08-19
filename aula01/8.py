'''Crie um dicionário com nome (chave) e telefone (valor). Implemente funções para
buscar telefone pelo nome e listar os contatos em ordem alfabética.'''

def buscar(contatos: dict):
    string = input("Nome: ")
    
    for (nome, telefone) in contatos.items():
        if nome == string:
            print(telefone)
        

def listar(contatos: dict):
    
    ordenado = dict(sorted(contatos.items(), key=lambda contatos: contatos[0]))
    
    print(ordenado)

while True:
    print("1. Buscar telefone")
    print("2. Listar em ordem alfabetica")
    contatos = {"Ana": "123456789",
                "Nicolas": "987654321"}

    opcao = int(input("O que deseja fazer: "))

    if opcao == 1:
        buscar(contatos)
    elif opcao == 2:
        listar(contatos)
    else:
        break