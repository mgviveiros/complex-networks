import networkx as nx
import metricas as met

N_LISTA = [10**2, 10**3, 10**4, 10**5]
M = 3


def main():
    met.garantir_pastas()

    for N in N_LISTA:
        print(f"[BA] N={N} m={M}")

        G = nx.barabasi_albert_graph(N, M)

        linha = met.calcular_propriedades(G, modelo="barabasi_albert", N=N, m=M)
        met.salvar_linha_csv(linha, nome_arquivo="resultado_ba.csv")
        met.salvar_distribuicao_graus(G, f"ba_N{N}_m{M}")

    G_exemplo = nx.barabasi_albert_graph(60, 2)
    met.plotar_rede_exemplo(G_exemplo, "Barabasi-Albert (exemplo)", "exemplo_ba.png", "orange")

   
    met.plotar_distribuicoes(
        [f"ba_N{N}_m{M}" for N in N_LISTA],
        [f"N={N}" for N in N_LISTA],
        f"Barabasi-Albert - distribuicao de graus (m={M})",
        f"ba_dist_m{M}.png",
    )

    print("Pronto. Tabela em", "resultado_ba.csv")


if __name__ == "__main__":
    main()