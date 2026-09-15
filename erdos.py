import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

n = 100
p = 0.2

G = nx.erdos_renyi_graph(n, p)
pos = nx.spring_layout(G)

net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
net.from_nx(G)
net.show_buttons(filter_=['physics'])
net.show("grafo_networkx_erdos.html", notebook=False)


# nx.draw(
#     G, 
#     pos, 
#     with_labels=True,      # Mostra o nome dos nós
#     node_color='skyblue',  # Cor dos nós
#     node_size=100,         # Tamanho dos nós
#     edge_color='black',     # Cor das linhas
#     font_size=12,          # Tamanho da fonte do texto
#     font_weight='bold'     # Estilo da fonte
# )

# plt.title("Exemplo de Rede Simples")
# plt.show()