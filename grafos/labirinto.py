from collections import deque
import heapq


DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))

def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo

def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))

def imprimir_grafo(grafo):
    for origem in sorted(grafo.keys()):
        vizinhos = grafo[origem]
        print(f"{origem} -> {vizinhos}")

def dfs(grafo, inicio, saida):
    visitados = set()
    caminho = []

    return busca_dfs(grafo, inicio, saida, visitados, caminho)

def busca_dfs(grafo, atual, saida, visitados: set, caminho: list):
    caminho.append(atual)
    visitados.add(atual)

    if atual == saida:
        return caminho, len(visitados)

    for v in grafo[atual]:
        if v not in visitados:
            resultado = busca_dfs(grafo, v, saida, visitados, caminho)

            if resultado is not None:
                return resultado

def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = deque([inicio])
    origem = {}
    caminho = []

    while fila:
        v = fila.popleft()
        if v == saida:
            caminho = []
            atual = saida
            
            while atual != inicio:
                caminho.append(atual)    
                atual = origem[atual]   
                
            caminho.append(inicio)      
            caminho.reverse()       
            return caminho, len(visitados)
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                fila.append(w)
                origem[w] = v

def gulosa(grafo, inicio, saida):
    visitados = {inicio}
    origem = {}
    fila = []
    heapq.heappush(fila, (distancia(inicio, saida), inicio))

    while fila:
        num_distancia, v = heapq.heappop(fila)

        if v == saida:
            caminho = []
            atual = saida
                    
            while atual != inicio:
                caminho.append(atual)    
                atual = origem[atual]   
                        
            caminho.append(inicio)      
            caminho.reverse()       
            return caminho, len(visitados)
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                heapq.heappush(fila, (distancia(w, saida), w))
                origem[w] = v

def distancia(atual, saida):
    return abs(atual[0] - saida[0]) + abs(atual[1] - saida[1])

def main():
    labirinto = [
        "I..................#", 
        ".#################.#", 
        ".###############...#", 
        "...###############.#", 
        ".#################.#",
        ".################..#",
        ".#################.#", 
        "..################.#", 
        "#.################.#", 
        "...........#######.#", 
        ".#########.#######.#",
        ".#########.#######.#", 
        ".#########.#####...#", 
        "...#######.#######.#", 
        ".#########......##.#", 
        ".##############.##.#", 
        ".###############...#", 
        ".###############.###", 
        "...................#", 
        "##################.F"  
    ]

    grafo = montar_grafo(labirinto)

    inicio = achar(labirinto, 'I')
    saida = achar(labirinto, 'F') 

    caminho, casas_visitadas = dfs(grafo, inicio, saida)
    funcoes = [('DFS', dfs(grafo, inicio, saida)), ('BFS', bfs(grafo, inicio, saida)), ('Gulosa', bfs(grafo, inicio, saida))]

    resultados = {}

    # desenhar(labirinto, caminho)

    for nome_algoritmo, (caminho, casas_visitadas) in funcoes:
        resultados[nome_algoritmo] = { 'caminho': caminho, 'casas_visitadas': casas_visitadas}

    print()

    print(f"{'Algoritmo':<12} | {'Casas Visitadas':<15} | {'Tamanho do Caminho'}")
    print("-" * 50)

    for algoritmo, dados in resultados.items():
        tamanho_caminho = len(dados['caminho'])
        casas = dados['casas_visitadas']
    
        print(f"{algoritmo:<12} | {casas:<15} | {tamanho_caminho}")

if __name__ == "__main__":
    main()
    