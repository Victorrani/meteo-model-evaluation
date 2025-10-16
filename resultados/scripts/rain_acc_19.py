import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

limiar = ['75', '90', '99']

for limiar in limiar:
    
    print(f'Produzindo figura para limiar {limiar}')
    path = f"/home/victor/USP/TCC_IC/akara_2024/resultados/v1.0.0/default/2024021900/rain_acc/{limiar}/"
    path2 = f"/home/victor/USP/TCC_IC/akara_2024/resultados/v1.1.0/default/2024021900/rain_acc/{limiar}/"

    files  = path  + 'mode_000000L_20240219_000000V_000000A_cts.txt'
    files1 = path2 + 'mode_000000L_20240219_000000V_000000A_cts.txt'

    # Leitura dos dados
    df  = pd.read_csv(files,  sep=r"\s+", engine="python", comment="#")
    df1 = pd.read_csv(files1, sep=r"\s+", engine="python", comment="#")

    cols = ['PODY', 'PODN', 'POFD', 'FAR', 'CSI']
    df_sel  = df[cols]
    df_sel1 = df1[cols]

    # ================================
    # Gráfico de barras agrupadas
    # ================================
    labels = cols
    x = np.arange(len(labels))
    width = 0.2   # largura menor para acomodar 4 grupos

    fig, ax = plt.subplots(figsize=(12, 6))

    # 4 conjuntos de barras, deslocados
    ax.bar(x - 1.5*width, df_sel.iloc[0], width, label='v1.0.0 RAW', color='#d62828', alpha=0.5)
    ax.bar(x - 0.5*width, df_sel.iloc[1], width, label='v1.0.0 OBJECT',  color="#860000", alpha=0.5)
    ax.bar(x + 0.5*width, df_sel1.iloc[0], width, label='v1.1.0 RAW',  color='#d62828', alpha=0.5, hatch='//')
    ax.bar(x + 1.5*width, df_sel1.iloc[1], width, label='v1.1.0 OBJECT',  color="#860000", alpha=0.5, hatch='//')

    # ================================
    # Personalização
    # ================================
    ax.set_ylabel('Value', fontsize=16, fontweight='bold')
    ax.set_title('')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, ha='left', fontsize=16, fontweight='bold')
    plt.ylim([0,1])  # definir limite y de 0 a 1
    plt.tick_params(axis='both', which='major', labelsize=12, width=1.5)
    plt.tick_params(axis='both', which='minor', labelsize=10)
    ax.legend(ncol=2, fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    plt.tight_layout()

    outdir = Path(f"/home/victor/USP/TCC_IC/akara_2024/resultados/comparative/2024021900/rain_acc/{limiar}/")
    outdir.mkdir(parents=True, exist_ok=True)

    # Salvar figura
    plt.savefig(outdir / f"rain_acc_19_{limiar}.png", dpi=300)

    df_sel.to_csv(outdir / f'rain_acc_19_{limiar}_v1.0.0.csv', index=False)
    df_sel1.to_csv(outdir / f'rain_acc_19_{limiar}_v1.1.0.csv', index=False)
