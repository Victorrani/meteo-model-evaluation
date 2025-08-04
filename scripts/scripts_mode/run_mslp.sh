#!/bin/bash

# Script que roda a avaliação para mslp das versões v1.0.0 e v1.1.0

# Diretórios fixos
DIR_MODE="/home/victor/DTC/MET-12.0.0/bin/"
BASE_OBS="/home/victor/USP/TCC_IC/akara_2024/dados/obs/AKARA_ERA5/teste.nc"

# Diretórios para v1.0.0
FCTS_1_0_0="/home/victor/USP/TCC_IC/akara_2024/dados/fcts/v1.0.0/2024021600/saida.nc"
BASE_OUT_1_0_0="/home/victor/USP/TCC_IC/akara_2024/resultados/v1.0.0/2024021600"
BASE_CONFIG_1_0_0="/home/victor/USP/TCC_IC/akara_2024/config_files/2024021600/"

# Diretórios para v1.1.0
FCTS_1_1_0="/home/victor/USP/TCC_IC/akara_2024/dados/fcts/v1.1.0/2024021600/saida1.nc"
BASE_OUT_1_1_0="/home/victor/USP/TCC_IC/akara_2024/resultados/v1.1.0/2024021600"
BASE_CONFIG_1_1_0="/home/victor/USP/TCC_IC/akara_2024/config_files/2024021600/"

# Datas para rodar
DATA_INI="20240216"
DATA_FIM="20240217"

DATA=$DATA_INI
while [ "$DATA" -le "$DATA_FIM" ]; do
    
    # Define quais horas rodar
    if [ "$DATA" = "$DATA_FIM" ]; then
        HORAS=("00")  # Último dia: só 00
    else
        HORAS=("00" "03" "06" "09" "12" "15" "18" "21")
    fi

    for HORA in "${HORAS[@]}"; do
        echo "Rodando para ${DATA} ${HORA}h"

        for VERSAO in "1_0_0" "1_1_0"; do
            if [ "$VERSAO" = "1_0_0" ]; then
                BASE_FCTS=$FCTS_1_0_0
                BASE_OUT=$BASE_OUT_1_0_0
                BASE_CONFIG=$BASE_CONFIG_1_0_0
                CONFIG_FILE="v1.0.0_mslp.config"
            else
                BASE_FCTS=$FCTS_1_1_0
                BASE_OUT=$BASE_OUT_1_1_0
                BASE_CONFIG=$BASE_CONFIG_1_1_0
                CONFIG_FILE="v1.1.0_mslp.config"
            fi

            CONF_TEMP="${BASE_CONFIG}temp_config_${DATA}_${HORA}_${VERSAO}.conf"
            cp "${BASE_CONFIG}/${CONFIG_FILE}" "$CONF_TEMP"
            echo $CONF_TEMP

            # Troca data+hora no campo level
            sed -i "s/@[0-9]\{8\}_[0-9]\{6\}/@${DATA}_$(printf "%02d" $HORA)0000/g" "$CONF_TEMP"

            # Ajusta output_prefix para incluir data+hora e versão
            sed -i "s/^output_prefix.*/output_prefix  = \"${DATA}_${HORA}_${VERSAO}\";/" "$CONF_TEMP"

            # Executa MODE
            ${DIR_MODE}./mode "$BASE_FCTS" "$BASE_OBS" "$CONF_TEMP" -outdir "$BASE_OUT"

            # Remove config temporário
            rm "$CONF_TEMP"
        done
    done

    DATA=$(date -d "${DATA} +1 day" +"%Y%m%d")
done
