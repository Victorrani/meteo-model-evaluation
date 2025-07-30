#!/bin/bash

# Diretório onde os arquivos .grib2 estão localizados
DIR_DADOS='/p1-nemo/victor/dados/chuva_MERGE/obs/'

# Nome do arquivo de saída
NOME_ARQUIVO='chuva_MERGE.nc'

echo 'Juntando todos os arquivos de formato grib2 para formato netCDF'
echo 'Processando...'

# Mudar para o diretório especificado
cd $DIR_DADOS

# Converter todos os arquivos .grib2 para .nc usando cdo
cdo -f nc copy ${DIR_DADOS}*.grib2 ${DIR_DADOS}${NOME_ARQUIVO}

echo 'Processo finalizado!'





