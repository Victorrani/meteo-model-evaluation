import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

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
    df_pairs = df[df["OBJECT_ID"].str.match(r"^(F|O)\d+$", na=False)].copy()

    # só adiciona se não estiver vazio
    if df_pairs.empty:
        continue

    # seleciona só as colunas de interesse
    df_pairs = df_pairs[[
        "MODEL", "FCST_VALID", "OBJECT_ID","LENGTH",
              "WIDTH", "AREA", "CENTROID_X", "CENTROID_Y",
                "CENTROID_LAT", "CENTROID_LON", "AXIS_ANG", 
                "CURVATURE", "COMPLEXITY"
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

#linhas_excluidas = [44, 41, 38]
#df_filtrado = df_filtrado.drop(index=linhas_excluidas).reset_index(drop=True)

print(df_filtrado)


all_pairs2 = []

for file2 in files2:
    # lê o arquivo
    df = pd.read_csv(file2, sep=r"\s+", header=0)

    # filtra pares Fxxx_Oyyy
    df_pairs2 = df[df["OBJECT_ID"].str.match(r"^(F|O)\d+$", na=False)].copy()

    # só adiciona se não estiver vazio
    if df_pairs2.empty:
        continue

    # seleciona só as colunas de interesse
    df_pairs2 = df_pairs2[[
        "MODEL", "FCST_VALID", "OBJECT_ID","LENGTH",
              "WIDTH", "AREA", "CENTROID_X", "CENTROID_Y",
                "CENTROID_LAT", "CENTROID_LON", "AXIS_ANG", 
                "CURVATURE", "COMPLEXITY"
    ]]

    # adiciona ao conjunto
    all_pairs2.append(df_pairs2)

# junta tudo em um único DataFrame
if all_pairs2:
    df_all2 = pd.concat(all_pairs2, ignore_index=True)
else:
    print("Nenhum par encontrado em nenhum arquivo")

print(df_all2)
limit_date = "20240217180000"


df_filtrado2 = df_all2[df_all2["FCST_VALID"] > limit_date]
df_filtrado2 = df_filtrado2.reset_index(drop=True)

#linhas_excluidas = [30, 33, 36, 39, 42, 46, 47, 50, 53, 54]
#df_filtrado2 = df_filtrado2.drop(index=linhas_excluidas).reset_index(drop=True)


print(df_filtrado2)

outdir = Path("/home/victor/USP/TCC_IC/akara_2024/resultados/comparative/2024021600/mslp")
outdir.mkdir(parents=True, exist_ok=True)

# converte tempo
df_filtrado["datetime"] = pd.to_datetime(df_filtrado["FCST_VALID"], format="%Y%m%d_%H%M%S")
df_filtrado2["datetime"] = pd.to_datetime(df_filtrado2["FCST_VALID"], format="%Y%m%d_%H%M%S")

# separa forecast e obs
df_filtrado_F = df_filtrado[df_filtrado["OBJECT_ID"] == "F001"]
df_filtrado_O = df_filtrado[df_filtrado["OBJECT_ID"] == "O001"]
df_filtrado2_F = df_filtrado2[df_filtrado2["OBJECT_ID"] == "F001"]
df_filtrado2_O = df_filtrado2[df_filtrado2["OBJECT_ID"] == "O001"]

grade = 55
grade1 = 55*55
# ---------- Área ----------
plt.figure(figsize=(10,6))
plt.plot(df_filtrado_F["datetime"], df_filtrado_F["AREA"]*grade1, "-o", label="Forecast v1.0.0", color='#f7b538')
plt.plot(df_filtrado2_F["datetime"], df_filtrado2_F["AREA"]*grade1, "x", label="Forecast v1.1.0", color='#f7b538', linestyle='--')
plt.plot(df_filtrado_O["datetime"], df_filtrado_O["AREA"]*grade1, "-s", label="Obs ERA5", color='black')


plt.legend()
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Área (km²)", fontsize=14, fontweight='bold')

# Ticks maiores
plt.tick_params(axis='both', which='major', labelsize=12, width=1.5)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig(outdir / "area_comparison.png", dpi=300)
plt.close()

# ---------- Length ----------
plt.figure(figsize=(10,6))
plt.plot(df_filtrado_F["datetime"], df_filtrado_F["LENGTH"]*grade, "-o", label="Forecast v1.0.0",  color='#f7b538')
plt.plot(df_filtrado2_F["datetime"], df_filtrado2_F["LENGTH"]*grade, "x", label="Forecast v1.1.0", color='#f7b538', linestyle='--')
plt.plot(df_filtrado_O["datetime"], df_filtrado_O["LENGTH"]*grade, "-s", label="Obs ERA5", color='black')

plt.legend()
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Length (km)", fontsize=14, fontweight='bold')

# Ticks maiores
plt.tick_params(axis='both', which='major', labelsize=12, width=1.5)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig(outdir / "length_comparison.png", dpi=300)
plt.close()

# ---------- Width ----------
plt.figure(figsize=(10,6))
plt.plot(df_filtrado_F["datetime"], df_filtrado_F["WIDTH"]*grade, "-o", label="Forecast v1.0.0", color='#f7b538')
plt.plot(df_filtrado2_F["datetime"], df_filtrado2_F["WIDTH"]*grade, "x", label="Forecast v1.1.0", color='#f7b538', linestyle='--')
plt.plot(df_filtrado_O["datetime"], df_filtrado_O["WIDTH"]*grade, "-s", label="Obs ERA5", color='black')

plt.legend()
plt.xlabel("Time", fontsize=14, fontweight='bold')
plt.ylabel("Width (km)", fontsize=14, fontweight='bold')

# Ticks maiores
plt.tick_params(axis='both', which='major', labelsize=12, width=1.5)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig(outdir / "width_comparison.png", dpi=300)
plt.close()

#posição

reboita_track = 'track_reboita.txt'
df_reboita = pd.read_csv(reboita_track)
master_track = 'track_csv_formatado.csv'
df_master = pd.read_csv(master_track)




plt.figure(figsize=(10,6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-50, -35, -35, -20], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.add_feature(cfeature.STATES)

ax.plot(df_filtrado_F["CENTROID_LON"], df_filtrado_F["CENTROID_LAT"], 
        color='#65a1e6', linewidth=1, alpha=0.7, zorder=1)
ax.scatter(df_filtrado_F["CENTROID_LON"], df_filtrado_F["CENTROID_LAT"], 
           label="Forecast v1.0.0", color='yellow', marker='o', s=20, zorder=2)

# Forecast v1.1.0
ax.plot(df_filtrado2_F["CENTROID_LON"], df_filtrado2_F["CENTROID_LAT"], 
        color='#1f77b4', linewidth=1, alpha=0.7, zorder=1)
ax.scatter(df_filtrado2_F["CENTROID_LON"], df_filtrado2_F["CENTROID_LAT"], 
           label="Forecast v1.1.0", color='#1f77b4', marker='x', s=20, zorder=2)

# Obs ERA5
ax.plot(df_filtrado_O["CENTROID_LON"], df_filtrado_O["CENTROID_LAT"], 
        color='black', linewidth=1, alpha=0.7, zorder=1)
ax.scatter(df_filtrado_O["CENTROID_LON"], df_filtrado_O["CENTROID_LAT"], 
           label="Obs ERA5", color='black', marker='s', s=20, zorder=2)
gl = ax.gridlines(draw_labels=True, linewidth=0.8, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False   # não mostrar no topo
gl.right_labels = False # não mostrar à direita
gl.xlabel_style = {"size": 10, "color": "black"}
gl.ylabel_style = {"size": 10, "color": "black"}

# Legenda
ax.legend(loc='lower left', fontsize=10, markerscale=1.2)


ax.legend()
plt.savefig(outdir / "position_comparison.png", dpi=300, bbox_inches='tight')
plt.close()

print(f"✅ Mapas salvos em {outdir}")