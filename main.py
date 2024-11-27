import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
from time import sleep

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] # Cria uma matriz quadrada com a quantidade de vértices informados onde todos os campos são zero
        self.edges = []

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1
        self.grafo[v-1][u-1] = 1
        self.edges.append((u, v))

    def mostra_grafo(self):
        print('A matriz de adjacências é: ')
        for i in range(self.vertices):
            print(self.grafo[i])

quantidadeVertices = int(input('Digite a quantidade de vértices: ')) # Recebe o input do usuário

G = nx.Graph()
G.add_nodes_from(range(1, quantidadeVertices+1)) # Adiciona os vértices ao grafo
pos = nx.circular_layout(G) # ANIMAÇÃO: cria um layout circular
fig, ax = plt.subplots(figsize=(6, 6)) # ANIMAÇÃO: define o tamanho da figura

quantidadeArestas = int(input('Digite a quantidade de arestas: '))
for i in range(quantidadeArestas):
    u = int(input("De qual vertice parte esta aresta: "))
    v = int(input("Em qual vertice chega esta aresta: "))
    G.add_edge(u, v) # Adiciona uma aresta
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='black', node_size=700, font_size=12) # ANIMAÇÃO: desenha o grafo
    plt.title(f'Adding Edge: {u} -> {v}') # ANIMAÇÃO: define o título da figura
    plt.pause(1) # ANIMAÇÃO: pausa a animação, precisa disso se não não mostra nada