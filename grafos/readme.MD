# Solucionador de Labirintos: DFS, BFS e Busca Gulosa

---

## O Labirinto

* `I`: Ponto de Início (Origem)
* `F`: Ponto Final (Destino/Saída)
* `#`: Paredes (Obstáculos intransponíveis)
* `.`: Caminhos livres
* `*`: Rastro deixado pelo algoritmo ao encontrar a saída

---

## Algoritmos Implementados

Neste projeto, o labirinto é modelado como um grafo (lista de adjacências), onde cada coordenada livre é um vértice e suas conexões são as coordenadas vizinhas válidas (Norte, Sul, Leste, Oeste).

Foram implementados três métodos de busca:

### 1. Busca em Profundidade (DFS - Depth-First Search)
A DFS ou Busca em Profundidade funciona através da estrutura de uma pilha. De forma geral, ela escolhe um vizinho e segue pela rota o máximo que conseguir, indo cada vez mais "fundo" no labirinto. Dessa forma, o algoritmo interrompe a busca e recua para o próximo vizinho livre apenas nas seguintes situações: quando encontra a saída, quando bate em uma parede ou quando percebe que todos os vizinhos já foram visitados.

### 2. Busca em Largura (BFS - Breadth-First Search)
Diferente da DFS, a BFS faz uso de uma fila para realizar uma busca em camadas (ou níveis). Basicamente, ao visitar um nó, o algoritmo o retira da fila e adiciona todos os seus vizinhos válidos. Dessa forma, ele consegue fazer uma varredura de forma mais uniforme e abrangente no grafo, garantindo sempre que o primeiro caminho encontrado até o destino seja o menor possível.

### 3. Busca Gulosa (Greedy Search)
Um Algoritmo Guloso é aquele que realiza sempre a melhor escolha local, buscando encontrar a melhor solução global. Nesse aspecto, a Busca Gulosa funciona de forma semelhante à BFS, porém a grande diferença é o uso de uma fila de prioridade, na qual é calculada a distância (heurística) da coordenada de cada vizinho até a saída. Com isso, o algoritmo tenta sempre "cortar caminho" na direção do alvo, podendo sofrer penalidades de desempenho e ficar preso em falsos corredores devido ao fato de não enxergar paredes.

---

## Resultados e Comparações

Ao executar os algoritmos em nossos cenários de teste, obtivemos as seguintes métricas:

| Algoritmo   | Casas Visitadas (Custo) | Tamanho do Caminho |
|-------------|-------------------------|--------------------|
| **DFS**     | 43          | 43                             |
| **BFS**     | 107         | 41                             |
| **Gulosa**  | 107         | 41                             |

### Análise de Desempenho
Como é possível analisar pela tabela, embora a DFS tenha visitado bem menos casas (43), ela não encontrou o menor caminho. Isso ocorre porque a sua estrutura encontra sempre a primeira rota viável com base na ordem dos vizinhos escolhidos, e não necessariamente a rota mais curta. Enquanto isso a BFS e a Busca Gulosa, por fazerem uma varredura maior acabam encontrando o caminho mais curto ao custo de um maior número de casas visitadas.