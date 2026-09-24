import os
import csv

import numpy as np
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

csv_saida = "resultados.csv" 
PASTA_GRAUS = "distribuicoes"
PASTA_FIGURAS = "figuras"

COLUNAS = [
    "modelo", "N", "p", "k", "m", "regime",
    "num_nos", "num_arestas", "grau_medio", "grau_min", "grau_max",
    "densidade", "frac_maior_componente", "conectado",
    "clustering", "distancia_media",
]

LIMITE_DISTANCIA = 10000


def garantir_pastas():
    os.makedirs(PASTA_GRAUS, exist_ok=True)
    os.makedirs(PASTA_FIGURAS, exist_ok=True)


def maior_componente(G):
    maior = max(nx.connected_components(G), key=len)
    return G.subgraph(maior).copy()


def calcular_propriedades(G, modelo, N, p=None, k=None, m=None, regime="-"):
    graus = [grau for _, grau in G.degree()]

    GC = maior_componente(G)
    if GC.number_of_nodes() <= LIMITE_DISTANCIA:
        dist_media = nx.average_shortest_path_length(GC)
    else:
        dist_media = "nao_calculado"

    return {
        "modelo": modelo,
        "N": N,
        "p": p if p is not None else "",
        "k": k if k is not None else "",
        "m": m if m is not None else "",
        "regime": regime,
        "num_nos": G.number_of_nodes(),
        "num_arestas": G.number_of_edges(),
        "grau_medio": sum(graus) / len(graus),
        "grau_min": min(graus),
        "grau_max": max(graus),
        "densidade": nx.density(G),
        "frac_maior_componente": GC.number_of_nodes() / G.number_of_nodes(),
        "conectado": nx.is_connected(G),
        "clustering": nx.average_clustering(G),
        "distancia_media": dist_media,
    }


def salvar_linha_csv(linha, nome_arquivo):
    arquivo_novo = not os.path.exists(nome_arquivo)
    with open(nome_arquivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS)
        if arquivo_novo:
            escritor.writeheader()
        escritor.writerow(linha)


def salvar_distribuicao_graus(G, nome_arquivo):
    garantir_pastas()
    graus = [grau for _, grau in G.degree()]
    valores, contagens = np.unique(graus, return_counts=True)
    with open(os.path.join(PASTA_GRAUS, nome_arquivo + ".csv"), "w",
              newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["grau", "contagem", "fracao"])
        for grau, contagem in zip(valores, contagens):
            escritor.writerow([grau, contagem, contagem / len(graus)])


def plotar_rede_exemplo(G, titulo, nome_arquivo, cor="skyblue"):
    garantir_pastas()
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(7, 7))
    nx.draw(G, pos, node_color=cor, node_size=100, edge_color="gray",
            with_labels=False)
    plt.title(titulo)
    plt.savefig(os.path.join(PASTA_FIGURAS, nome_arquivo), dpi=150, bbox_inches="tight")
    plt.close()


def plotar_distribuicoes(nomes_arquivos, legendas, titulo, nome_saida, loglog=True):
    garantir_pastas()
    plt.figure(figsize=(7, 5))
    for nome, legenda in zip(nomes_arquivos, legendas):
        caminho = os.path.join(PASTA_GRAUS, nome + ".csv")
        if not os.path.exists(caminho):
            continue
        graus, fracoes = [], []
        with open(caminho, encoding="utf-8") as f:
            for linha in csv.DictReader(f):
                graus.append(int(linha["grau"]))
                fracoes.append(float(linha["fracao"]))
        plt.plot(graus, fracoes, "o-", markersize=4, label=legenda)

    if loglog:
        plt.xscale("log")
        plt.yscale("log")
    plt.xlabel("grau k")
    plt.ylabel("fracao de nos")
    plt.title(titulo)
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_FIGURAS, nome_saida), dpi=150)
    plt.close()
    print("  figura salva:", nome_saida)


