import pandas as pd
import glob
import matplotlib.pyplot as plt

# Lista todos os arquivos que terminam com cts.txt
arquivos = sorted(glob.glob('*cts.txt'))

colunas_desejadas = [
    'MODEL', 'FMEAN', 'ACC', 'FBIAS', 'PODY', 'PODN',
    'POFD', 'FAR', 'CSI', 'GSS', 'HK', 'HSS'
]

df_final = pd.DataFrame(columns=colunas_desejadas)

for arquivo in arquivos:
    data_hora = arquivo.split('_')[1] + arquivo.split('_')[2]
    col_name = pd.to_datetime(data_hora, format='%Y%m%d%H')
    df = pd.read_csv(arquivo, sep='\s+', )
    print(df.T)


