"""""
Progetto di Francesco Santi 2025

Si scriva un programma python che legge da file csv la matrice di adiacenza di un grafo e:
1) determina se il grafo corrispondente è orientato o non orientato
2) applica sul grafo un algoritmo compatibile non banale scelto fra quelli presentati a lezione (BFS, DFS,
Kruskal, Prim, Dijkstra, Bellman-Ford, … )
3) scrive in output un risultato significativo (predecessori, tempi visita, commini minimi, … ) calcolato
dall’algoritmo

Matrice di adiacenza, utilizzare per effettuare un test:

0,1,0,0,1,1
1,0,1,0,0,0
0,1,0,1,0,0
0,0,1,0,1,0
1,0,0,1,0,1
1,0,0,0,1,0
"""""

import csv
import collections

class Graph:
    """
    Classe che rappresenta un grafo mediante matrice di adiacenza.
    La matrice M[i][j] rappresenta l'arco dal vertice i al vertice j:
    - Se M[i][j] = 0, non c'è arco
    - Se M[i][j] > 0, c'è un arco con peso M[i][j]
    """
    def __init__(self, matrix):
        self.matrix = matrix
        self.V = len(matrix)
        
    def graph_is_oriented(self):
        """Determina se il grafo è orientato confrontando la matrice con la sua trasposta"""
        for i in range(self.V):
            for j in range(self.V):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return True
        return False
        
    def get_neighbors(self, vertex):
        """Restituisce la lista dei vertici adiacenti a un dato vertice"""
        return [j for j in range(self.V) if self.matrix[vertex][j] != 0]
        
    def bfs(self, start):
        """
        Implementa BFS e restituisce varie informazioni sulla visita:
        - predecessori: per ricostruire i cammini
        - tempi di scoperta: quando viene visitato ogni nodo
        - distanze: numero di archi dal nodo sorgente
        - livelli: nodi raggruppati per distanza dalla sorgente
        """
        visited = [False] * self.V
        discovery_time = [-1] * self.V
        predecessors = [-1] * self.V
        distances = [float('inf')] * self.V
        levels = collections.defaultdict(list)
        
        time = 0
        queue = collections.deque([start])
        visited[start] = True
        discovery_time[start] = time
        distances[start] = 0
        levels[0].append(start)
        
        while queue:
            time += 1
            vertex = queue.popleft()
            
            for neighbor in self.get_neighbors(vertex):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    discovery_time[neighbor] = time
                    predecessors[neighbor] = vertex
                    distances[neighbor] = distances[vertex] + 1
                    levels[distances[neighbor]].append(neighbor)
                    queue.append(neighbor)
                    
        return predecessors, discovery_time, distances, levels

    def get_path_to(self, target, predecessors):
        """Ricostruisce il cammino dalla sorgente a un nodo target"""
        path = []
        current = target
        while current != -1:  # -1 è il predecessore della sorgente
            path.append(current)
            current = predecessors[current]
        return list(reversed(path))

def read_adjacency_matrix(filename):
    """Legge la matrice di adiacenza da file CSV"""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [[int(x) for x in row] for row in reader]

def print_matrix(matrix):
    """Stampa la matrice di adiacenza in formato leggibile"""
    print("\nMatrice di adiacenza:")
    for row in matrix:
        print(" ".join(f"{x:2d}" for x in row))

def main():
    # 1. Lettura e stampa della matrice
    print("Lettura della matrice di adiacenza dal file...")
    matrix = read_adjacency_matrix('matrice.csv')
    print_matrix(matrix)
    graph = Graph(matrix)
    
    # 2. Verifica orientamento
    graph_is_oriented = graph.graph_is_oriented()
    print(f"\nIl grafo è {'orientato' if graph_is_oriented else 'non orientato'}")
    
    # 3. Esecuzione BFS e calcolo risultati
    start_vertex = 0
    predecessori, tempi, distanze, livelli = graph.bfs(start_vertex)
    
    # 4. Output dettagliato dei risultati
    print(f"\n{'='*50}")
    print(f"RISULTATI BFS DAL VERTICE {start_vertex}")
    print(f"{'='*50}")
    
    # Stampa struttura dei livelli
    print("\nSTRUTTURA DEI LIVELLI:")
    print(f"{'*'*30}")
    for level, nodes in livelli.items():
        print(f"Livello {level} (distanza {level}): {nodes}")
    
    # Stampa informazioni per ogni vertice
    print("\nINFORMAZIONI PER VERTICE:")
    print(f"{'*'*30}")
    for v in range(graph.V):
        print(f"\nVertice {v}:")
        print(f"  Tempo di scoperta: {tempi[v] if tempi[v] != -1 else 'non raggiunto'}")
        print(f"  Distanza dalla sorgente: {distanze[v] if distanze[v] != float('inf') else 'infinita'}")
        if v != start_vertex and distanze[v] != float('inf'):
            path = graph.get_path_to(v, predecessori)
            print(f"  Cammino dalla sorgente: {' -> '.join(map(str, path))}")

if __name__ == "__main__":
    main()