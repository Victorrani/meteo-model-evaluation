#!/bin/bash

DIR_DADOS='/p1-nemo/victor/dados/chuva_MERGE/obs/'

# Nome do arquivo de saída
NOME_ARQUIVO_IN='chuva_MERGE.nc'
NOME_ARQUIVO_OUT='AKARA_MERGE.nc'

echo 'Recortando o domínio que será analisado pelo MODE'

cdo sellonlatbox,-60,-20,-45,-15 ${DIR_DADOS}${NOME_ARQUIVO_IN} ${DIR_DADOS}${NOME_ARQUIVO_OUT}

echo 'Processo finalizado'
