import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network


n = 100
m = 15

G = nx.barabasi_albert_graph(n, m)
pos = nx.spring_layout(G)

net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
net.from_nx(G)
net.show_buttons(filter_=['physics'])
net.show("grafo_networkx_barabasi.html", notebook=False)

# nx.draw(
#     G,  
#     pos,
#     with_labels=True,      # Mostra o nome dos nós
#     node_color='orange',   # Cor dos nós
#     node_size=100,         # Tamanho dos nós
#     edge_color='gray',     # Cor das linhas
#     font_size=12,          # Tamanho da fonte do texto
#     font_weight='bold'     # Estilo da fonte
# )

# plt.title("Exemplo de Rede Barabási-Albert")
# plt.show()