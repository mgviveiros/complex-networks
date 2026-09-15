import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

n, p, k = 100, 0.2, 10

W = nx.watts_strogatz_graph(n, k, p) 
pos = nx.spring_layout(W)

net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
net.from_nx(W)
net.show_buttons(filter_=['physics'])
net.show("grafo_networkx_pyvis.html", notebook=False)

# nx.draw(
#     W,
#     pos,
#     with_labels=True,      # Mostra o nome dos nós
#     node_color='lightgreen',  # Cor dos nós
#     node_size=100,         # Tamanho dos nós
#     edge_color='gray',     # Cor das linhas
#     font_size=12,          # Tamanho da fonte do texto
#     font_weight='bold'     # Estilo da fonte
# )

# plt.title("Exemplo de Rede Watts-Strogatz")
# plt.show()