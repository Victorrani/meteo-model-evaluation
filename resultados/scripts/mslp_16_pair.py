import pandas as pd
from pathlib import Path

# pasta com os arquivos
path = Path("/home/victor/USP/TCC_IC/akara_2024/resultados/v1.0.0/default/2024021600/mslp/")
path2 = Path("/home/victor/USP/TCC_IC/akara_2024/resultados/v1.1.0/default/2024021600/mslp/")

files = sorted(path.glob("*obj.txt"))
files2 = sorted(path2.glob("*obj.txt"))

all_pairs = []

for file in files:
    # lê o arquivo
    df = pd.read_csv(file, sep=r"\s+", header=0)

    # filtra pares Fxxx_Oyyy
    df_pairs = df[df["OBJECT_ID"].str.match(r"^F\d+_O\d+$", na=False)].copy()

    # só adiciona se não estiver vazio
    if df_pairs.empty:
        continue

    # seleciona só as colunas de interesse
    df_pairs = df_pairs[[
        "MODEL", "FCST_VALID", "OBJECT_ID", "OBJECT_CAT", 
        "CENTROID_DIST", "BOUNDARY_DIST", "AREA_RATIO", 
        "INTERSECTION_AREA", "PERCENTILE_INTENSITY_RATIO", "INTEREST"
    ]]

    # adiciona ao conjunto
    all_pairs.append(df_pairs)

# junta tudo em um único DataFrame
if all_pairs:
    df_all = pd.concat(all_pairs, ignore_index=True)
else:
    print("Nenhum par encontrado em nenhum arquivo")

limit_date = "20240217180000"


df_filtrado = df_all[df_all["FCST_VALID"] > limit_date]
df_filtrado = df_filtrado.reset_index(drop=True)

linhas_excluidas = []
df_filtrado = df_filtrado.drop(index=linhas_excluidas).reset_index(drop=True)


print(df_filtrado)

all_pairs2 = []

for file2 in files2:
    # lê o arquivo
    df = pd.read_csv(file2, sep=r"\s+", header=0)

    # filtra pares Fxxx_Oyyy
    df_pairs2 = df[df["OBJECT_ID"].str.match(r"^F\d+_O\d+$", na=False)].copy()

    # só adiciona se não estiver vazio
    if df_pairs2.empty:
        continue

    # seleciona só as colunas de interesse
    df_pairs2 = df_pairs2[[
        "MODEL", "FCST_VALID", "OBJECT_ID", "OBJECT_CAT", 
        "CENTROID_DIST", "BOUNDARY_DIST", "AREA_RATIO", 
        "INTERSECTION_AREA", "PERCENTILE_INTENSITY_RATIO", "INTEREST"
    ]]

    # adiciona ao conjunto
    all_pairs2.append(df_pairs2)

# junta tudo em um único DataFrame
if all_pairs2:
    df_all2 = pd.concat(all_pairs2, ignore_index=True)
else:
    print("Nenhum par encontrado em nenhum arquivo")

limit_date = "20240217180000"


df_filtrado2 = df_all2[df_all2["FCST_VALID"] > limit_date]
df_filtrado2 = df_filtrado2.reset_index(drop=True)

linhas_excluidas = [12, 14, 16, 18]
df_filtrado2 = df_filtrado2.drop(index=linhas_excluidas).reset_index(drop=True)


print(df_filtrado2)

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# saída
outdir = Path("/home/victor/USP/TCC_IC/akara_2024/resultados/comparative/2024021600/mslp")
outdir.mkdir(parents=True, exist_ok=True)

# converte tempo
df_filtrado["datetime"] = pd.to_datetime(df_filtrado["FCST_VALID"], format="%Y%m%d_%H%M%S")
df_filtrado2["datetime"] = pd.to_datetime(df_filtrado2["FCST_VALID"], format="%Y%m%d_%H%M%S")

# ---------- INTEREST ----------
plt.figure(figsize=(12,5))
plt.plot(df_filtrado["datetime"], df_filtrado["INTEREST"], "-o", label="v1.0.0",  color='#f7b538')
plt.plot(df_filtrado2["datetime"], df_filtrado2["INTEREST"], "x", label="v1.1.0",  color='#f7b538', linestyle='--')
plt.tick_params(axis='both', which='major', labelsize=12, width=1.5)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Total Interest", fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(outdir / "interest_comparison.png", dpi=300)
plt.close()
grade = 55
# ---------- CENTROID_DIST ----------
plt.figure(figsize=(12,5))
plt.plot(df_filtrado["datetime"], df_filtrado["CENTROID_DIST"]*grade, "-o", label="v1.0.0", color='#f7b538')
plt.plot(df_filtrado2["datetime"], df_filtrado2["CENTROID_DIST"]*grade, "x", label="v1.1.0", color='#f7b538', linestyle='--')
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Centroid Distance (Km)", fontsize=14, fontweight='bold')
plt.tick_params(axis='both', which='major', labelsize=12, width=1.5)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(outdir / "centroid_dist_comparison.png", dpi=300)
plt.close()

# ---------- AREA_RATIO ----------
plt.figure(figsize=(12,5))
plt.plot(df_filtrado["datetime"], df_filtrado["AREA_RATIO"], "-o", label="v1.0.0", color='#f7b538')
plt.plot(df_filtrado2["datetime"], df_filtrado2["AREA_RATIO"], "x", label="v1.1.0", color='#f7b538', linestyle='--')
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Area Ratio", fontsize=14, fontweight='bold')
plt.tick_params(axis='both', which='major', labelsize=12, width=1.5)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(outdir / "area_ratio_comparison.png", dpi=300)
plt.close()

print(f"✅ Figuras salvas em {outdir}")