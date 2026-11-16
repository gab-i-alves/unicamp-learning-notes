# Gera a arte da capa: linhas coloridas que entram pela esquerda e contornam
# uma esfera, no fundo índigo. Página A4 inteira, para ficar alinhada à capa.
# Só escreve os arquivos de saída indicados na linha de comando.
# Uso: uv run --no-project --with matplotlib --with numpy python images/capa-arte.py images/capa-arte.pdf [previa.png]
# A semente fixa (615) faz a arte sair sempre igual.
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

W, H = 21.0, 29.7  # A4 em cm
FUNDO = "#26245A"
FAIXA = 3.6  # altura da faixa branca dos logos
TOPO_ARTE = 21.0
MEDIA = [0.0, 1.0, 0.0]  # direção média das normais dos grandes círculos
ESPALHAMENTO = 0.8
SORTEIOS = 750

CORES = [
    "#5B3CC4",
    "#7B5CF0",
    "#9D86FF",
    "#C9B8FF",
    "#2F6FD6",
    "#4F8FF0",
    "#7FB2FF",
    "#39C2E0",
    "#A6E1FA",
    "#ECE7FB",
    "#6FE3F5",
]
PESOS = [8, 12, 12, 8, 10, 12, 10, 9, 7, 4, 6]


def linhas(rng, n, centro, raio):
    cx, cy = centro
    t = np.linspace(0, 2 * np.pi, 720)
    # grandes círculos com normais sorteadas em torno de uma direção média:
    # as curvas variam, mas seguem um mesmo sentido ao contornar a esfera
    media = np.array(MEDIA)
    media /= np.linalg.norm(media)
    for _ in range(n):
        nrm = media + rng.normal(scale=ESPALHAMENTO, size=3)
        nrm /= np.linalg.norm(nrm)
        u = np.cross(nrm, [0, 0, 1.0])
        u /= np.linalg.norm(u)
        v = np.cross(nrm, u)
        p = raio * (np.outer(np.cos(t), u) + np.outer(np.sin(t), v))
        frente = p[:, 2] >= 0
        if not frente.any() or frente.all():
            continue
        # trecho visível contínuo, começando no limbo
        i0 = np.argmax(~frente[:-1] & frente[1:]) + 1
        idx = (np.arange(len(t)) + i0) % len(t)
        vis = frente[idx]
        fim = np.argmin(vis) if not vis.all() else len(vis)
        arco = p[idx[:fim]]
        if len(arco) < 10:
            continue
        # só as curvas que entram pela esquerda
        if arco[0, 0] > 0:
            arco = arco[::-1]
        if arco[0, 0] > -0.15 * raio:
            continue
        xs, ys = arco[:, 0] + cx, arco[:, 1] + cy
        # prolonga a entrada em linha reta, tangente ao arco
        d = np.array([xs[0] - xs[3], ys[0] - ys[3]])
        d /= np.linalg.norm(d)
        if d[0] > -0.3 or d[1] > 0.45:
            continue
        comp = rng.uniform(12, 30)
        xs = np.concatenate([[xs[0] + d[0] * comp], xs])
        ys = np.concatenate([[ys[0] + d[1] * comp], ys])
        # parte do arco some atrás da esfera, como no desenho de referência
        corte = rng.uniform(0.6, 1.0)
        k = max(3, int(len(xs) * corte))
        yield xs[:k], ys[:k]


def main(saida_pdf, previa=None):
    fig = plt.figure(figsize=(W / 2.54, H / 2.54))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), W, H, fc=FUNDO, ec="none", zorder=0))

    rng = np.random.default_rng(615)
    pesos = np.array(PESOS) / sum(PESOS)
    for xs, ys in linhas(rng, SORTEIOS, (14.6, 10.0), 7.4):
        if ys.max() > TOPO_ARTE or len(xs) < 40:
            continue
        cor = CORES[rng.choice(len(CORES), p=pesos)]
        lw = rng.uniform(0.6, 2.2)
        ax.plot(xs, ys, color=cor, lw=lw, alpha=0.9, solid_capstyle="round", zorder=2)

    fig.savefig(saida_pdf)
    if previa:
        # prévia com os textos e a faixa da capa, só para conferir a composição
        ax.add_patch(Rectangle((0, 0), W, FAIXA, fc="white", zorder=5))
        ax.plot([1.8, 19.2], [27.4, 27.4], color="#ECE7FB", lw=0.8, zorder=5)
        ax.text(
            1.8,
            26.0,
            "Caderno da Especialização",
            color="#ECE7FB",
            fontsize=36,
            family="serif",
            va="center",
            zorder=5,
        )
        ax.text(
            1.8,
            24.4,
            "Engenharia e Administração de Sistemas de Banco de Dados",
            color="white",
            fontsize=14,
            family="serif",
            va="center",
            zorder=5,
        )
        fig.savefig(previa, dpi=60)


if __name__ == "__main__":
    main(*sys.argv[1:])
