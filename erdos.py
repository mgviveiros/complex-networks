import networkx as nx
import metricas as met
import math
N_LISTA = [10**2, 10**3, 10**4]
REGIMES = ["subcritico", "critico", "supercritico", "conectado"]
 

def p_do_regime(N, regime):
    """<k> = p*(N-1). Cada regime pede um valor diferente de <k>. """
    if regime == "subcritico":
        return 0.5 / (N - 1)
    if regime == "critico":
        return 1.0 / (N - 1)
    if regime == "supercritico":
        return 2.0 / (N - 1)
    if regime == "conectado":
        return 2.0 * math.log(N) / (N - 1)


def main():
    met.garantir_pastas()

    for N in N_LISTA:
        for regime in REGIMES:
            p = p_do_regime(N, regime)
            print(f"[ER] N={N} regime={regime} p={p:.2g}")
            G = nx.erdos_renyi_graph(N, p, seed=42)
            nome_arquivo = f"resultado_er.csv"
            linha = met.calcular_propriedades(G, modelo="erdos_renyi", N=N, p=p, regime=regime)
            met.salvar_linha_csv(linha, nome_arquivo)
            met.salvar_distribuicao_graus(G, f"er_N{N}_{regime}")

    
    G_exemplo = nx.erdos_renyi_graph(60, 0.05, seed=42)
    met.plotar_rede_exemplo(G_exemplo, "Erdos-Renyi (exemplo)", "exemplo_er.png")

    
    for N in N_LISTA:
        met.plotar_distribuicoes(
            [f"er_N{N}_{r}" for r in REGIMES], REGIMES,
            f"Erdos-Renyi - distribuicao de graus (N={N})",
            f"er_dist_N{N}.png",
        )

    print("Pronto. Tabela em", nome_arquivo)

main()