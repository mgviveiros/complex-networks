import networkx as nx
import metricas as met

N_LISTA = [10**2, 10**3, 10**4]
K = 10 
P_LISTA = [0.0, 0.001, 0.01, 0.1, 0.5, 1.0]


def main():
    met.garantir_pastas()

    for N in N_LISTA:
        for p in P_LISTA:
            print(f"[WS] N={N} k={K} p={p}")

            G = nx.watts_strogatz_graph(N, K, p, seed=42)

            linha = met.calcular_propriedades(G, modelo="watts_strogatz", N=N, p=p, k=K)
            met.salvar_linha_csv(linha, nome_arquivo="resultado_ws.csv")
            met.salvar_distribuicao_graus(G, f"ws_N{N}_k{K}_p{p}")

    G_exemplo = nx.watts_strogatz_graph(60, 4, 0.1, seed=42)
    met.plotar_rede_exemplo(G_exemplo, "Watts-Strogatz (exemplo)", "exemplo_ws.png", "lightgreen")

    for N in N_LISTA:
        met.plotar_distribuicoes(
            [f"ws_N{N}_k{K}_p{p}" for p in P_LISTA],
            [f"p={p}" for p in P_LISTA],
            f"Watts-Strogatz - distribuicao de graus (N={N}, k={K})",
            f"ws_dist_N{N}.png",
            loglog=False,   
        )

    print("Pronto. Tabela em", "resultado_ws.csv") 



main()