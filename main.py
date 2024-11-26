import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        # Cria uma matriz quadrada com a quantidade de vértices informados onde todos os campos são zero
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        self.edges = []

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1
        self.grafo[v-1][u-1] = 1
        self.edges.append((u, v))

    def mostra_grafo(self):
        print('A matriz de adjacências é: ')
        for i in range(self.vertices):
            print(self.grafo[i])


quantidadeVertices = int(input('Digite a quantidade de vértices: '))
g = Grafo(quantidadeVertices)

quantidadeArestas = int(input('Digite a quantidade de arestas: '))
for i in range(quantidadeArestas):
    u = int(input("De qual vertice parte esta aresta: "))
    v = int(input("Em qual vertice chega esta aresta: "))
    g.adiciona_aresta(u, v)

g.mostra_grafo()

# Animation
def update(frame):
    edge = g.edges[frame]
    G.add_edge(edge[0], edge[1])
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            edge_color='black', node_size=700, font_size=12)
    plt.title(f'Adding Edge: {edge}')


G = nx.Graph()
G.add_nodes_from(range(1, quantidadeVertices+1))

pos = nx.circular_layout(G)

fig, ax = plt.subplots(figsize=(6, 6))
ani = FuncAnimation(fig, update, frames=len(g.edges), repeat=False, interval=1000)

# Start the animation
plt.show()