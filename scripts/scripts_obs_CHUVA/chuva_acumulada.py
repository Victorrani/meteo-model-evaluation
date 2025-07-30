import os
import xarray as xr
import pandas as pd

# Caminho do arquivo de entrada e saída
DIR_DADO = "/p1-nemo/victor/dados/chuva_MERGE/obs/"
ARQUIVO_IN = "chuva_AKARA_MERGE.nc"
ARQUIVO_OUT = "chuva_acumulada_3h.nc"

# Abrir o dataset
ds = xr.open_dataset(os.path.join(DIR_DADO, ARQUIVO_IN), engine='netcdf4')

# Verificar as variáveis e dimensões do dataset

# Supondo que 'prec' seja a variável de precipitação no dataset
ds = ds['prec']
print(ds.values)
accu_3h_prec = ds.resample(time='3h').sum(dim='time')
print(accu_3h_prec)

accu_3h_prec['time'] = pd.date_range(start="2024-02-14T00:00:00", periods=accu_3h_prec.sizes['time'], freq='3h')
accu_3h_prec['forecast_reference_time'] = pd.Timestamp("2024-02-14T00:00:00")
# Converter de volta para Dataset para salvar
ds_out = accu_3h_prec.to_dataset(name='prec')

# Salvar no formato NetCDF
ds_out.to_netcdf(os.path.join(DIR_DADO, ARQUIVO_OUT))
