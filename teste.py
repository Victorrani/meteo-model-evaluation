import xarray as xr
import os

# Diretório onde estão os arquivos .grib2
DIR_DADOS = "/p1-nemo/victor/dados/chuva_MERGE/"
DIR_SAIDA = "/p1-nemo/victor/dados/chuva_MERGE/"

# Definir limites de latitude e longitude para recorte
lat_min, lat_max = -60, 15   
lon_min, lon_max = -80, -30  

# Abrir múltiplos arquivos GRIB2
ds = xr.open_mfdataset(os.path.join(DIR_DADOS, "*.grib2"), engine='cfgrib', combine="by_coords")

# Recortar a região desejada
ds_recorte = ds.sel(latitude=slice(lat_max, lat_min), longitude=slice(lon_min, lon_max))

# Nome do arquivo de saída
arquivo_saida = os.path.join(DIR_SAIDA, "recorte.nc")

# Salvar em NetCDF
ds_recorte.to_netcdf(arquivo_saida)

print(f"Processo concluído! Arquivo salvo como {arquivo_saida}")

