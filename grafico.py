import matplotlib.pyplot as plt


def preparar_eixo(bits, sinal):
    sinal_plot = sinal.copy()
    sinal_plot.append(sinal_plot[-1])

    if len(sinal) == len(bits) * 2:
        eixo_x = [i / 2 for i in range(len(sinal_plot))]
    elif len(sinal) * 2 == len(bits) or len(sinal) * 2 == len(bits) + 1:
        eixo_x = [i * 2 for i in range(len(sinal_plot))]
    else:
        eixo_x = list(range(len(sinal_plot)))

    return eixo_x, sinal_plot


def desenhar_sinal(ax, bits, sinal, titulo):
    eixo_x, sinal_plot = preparar_eixo(bits, sinal)

    menor_nivel = min(sinal_plot)
    maior_nivel = max(sinal_plot)
    posicao_bits = maior_nivel + 0.5

    ax.step(eixo_x, sinal_plot, where="post", linewidth=2)

    for i in range(len(bits) + 1):
        ax.axvline(x=i, linestyle="--", linewidth=1, color="gray")

    for i, bit in enumerate(bits):
        ax.text(i + 0.5, posicao_bits, bit, ha="center", fontsize=12)

    ax.set_title(titulo)
    ax.set_ylabel("Nivel")
    ax.set_ylim(menor_nivel - 1, maior_nivel + 1)
    ax.set_xlim(0, len(bits))
    ax.set_yticks(sorted(set(sinal_plot + [-1, 0, 1])))
    ax.grid(axis="y", linestyle=":")


def exibir_grafico(bits, sinal, titulo):
    fig, ax = plt.subplots(figsize=(12, 4))

    desenhar_sinal(ax, bits, sinal, titulo)

    ax.set_xlabel("Intervalos de bit")

    plt.tight_layout()
    plt.show()


def exibir_grafico_comparacao(bits, sinal_1, titulo_1, sinal_2, titulo_2, metricas_1, metricas_2):
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), gridspec_kw={"height_ratios": [3, 3, 1]})

    desenhar_sinal(axs[0], bits, sinal_1, titulo_1)
    desenhar_sinal(axs[1], bits, sinal_2, titulo_2)

    axs[1].set_xlabel("Intervalos de bit")

    axs[2].axis("off")

    texto_metricas = (
        f"{titulo_1}: transicoes = {metricas_1[0]}, media = {round(metricas_1[1], 2)}\n"
        f"{titulo_2}: transicoes = {metricas_2[0]}, media = {round(metricas_2[1], 2)}"
    )

    axs[2].text(0.01, 0.7, texto_metricas, fontsize=12, va="top")

    plt.tight_layout()
    plt.show()
