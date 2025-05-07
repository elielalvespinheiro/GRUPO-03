import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
caminho_csv = 'Documento-Limpo-grupo03.csv'

# Leitura do CSV
df = pd.read_csv(caminho_csv, sep=';', decimal=',', encoding='utf-8')
df = df.replace(',', '.', regex=True)

def temperatura(arqui):
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)
    # Converte colunas numéricas
    colunas_numericas = ['Temp. Ins. (C)', 'Temp. Max. (C)', 'Temp. Min. (C)']
    for col in colunas_numericas:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Criação da coluna datetime
    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')
    df['Mes'] = df['Data_Hora'].dt.day

    meses_desejados = [6]  # Altere para o mês que quiser (1 = janeiro, 12 = dezembro)

    # Filtrar apenas os dados do mês escolhido
    df = df[(df['Data_Hora'].dt.month.isin(meses_desejados)) & (df['Data_Hora'].dt.day <= 30)]

    # Calcula as médias
    media_temp_ins = df.groupby('Mes')["Temp. Ins. (C)"].mean()
    media_temp_max = df.groupby('Mes')["Temp. Max. (C)"].mean()
    media_temp_min = df.groupby('Mes')["Temp. Min. (C)"].mean()

    # Gráfico de linhas com as 3 temperaturas ao longo do tempo
    plt.figure(figsize=(10, 6))

    plt.plot(media_temp_ins, label='Temp. Instantânea', color='skyblue')

    plt.plot(media_temp_max, label='Temp. Máxima', color='orange')

    valor_maximo = 30
    valor_minimo = 26
    
    plt.axhline(y=valor_maximo, color='green', linestyle='--', label='Temperatura Máxima Ideal')
    plt.axhline(y=valor_minimo, color='red', linestyle=':', label='Temperatura Mínima Ideal')

    plt.plot(media_temp_min, label='Temp. Mínima', color='lightgreen')

    plt.title('Temperaturas ao Longo do Tempo - Junho')
    plt.xlabel('Dias capturados')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(range(1, 32))

    # Gira os rótulos do eixo x para melhor visualização
    plt.tight_layout()
    plt.show()

    # if(valor_maximo >= 38):
    #     print('O peixe terá redução no apetite e ocasionalmente morrerá')
    # elif(valor_minimo <= 20):
    #     print('O peixe deixará de se alimentar bem e seu crescimento diminuirá')
    # elif(valor_minimo <=14):
    #     print('O peixe terá um crescimento muito lento e baixa tolerância ao manuseio e ás doenças')

def umidade(arqui):
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    # Converte colunas numéricas
    colunas_umidade = ['Umi. Ins. (%)', 'Umi. Max. (%)', 'Umi. Min. (%)']
    for col in colunas_umidade:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Criação da coluna datetime
    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')
    df['Dia'] = df['Data_Hora'].dt.day
    df['Mes'] = df['Data_Hora'].dt.month

    # Filtra apenas o mês desejado
    mes_desejado = 6  # Junho
    df = df[(df['Mes'] == mes_desejado) & (df['Dia'] <= 30)]

    # Agrupamento por dia e cálculo das médias em porcentagem
    media_ur_ins = df.groupby('Dia')["Umi. Ins. (%)"].mean()
    media_ur_max = df.groupby('Dia')["Umi. Max. (%)"].mean() 
    media_ur_min = df.groupby('Dia')["Umi. Min. (%)"].mean() 

  # Junta os dados em um DataFrame para plotagem
    df_umidade = pd.DataFrame({
        'UR Instantânea': media_ur_ins,
        'UR Máxima': media_ur_max,
        'UR Mínima': media_ur_min
    })

    # Gráfico
    valor_maximo = 30
    valor_minimo = 26
    plt.axhline(y=valor_maximo, color='green', linestyle='--', label='Ponto Máximo Ideal')
    plt.axhline(y=valor_minimo, color='red', linestyle=':', label='Ponto Mínimo Ideal')

    df_umidade.plot(kind='area', figsize=(10, 6), color=['dodgerblue', 'green', 'red'], alpha=0.5)

    plt.title('Umidade Relativa do Ar - Junho')
    plt.xlabel('Dia do mês')
    plt.ylabel('Umidade (%)')
    plt.legend()
    plt.grid(True)

    plt.xticks(range(1, 32))
    plt.tight_layout()
    plt.show()

def orvalho(arqui):
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    # Colunas do ponto de orvalho
    colunas_orvalho = ['Pto Orvalho Ins. (C)', 'Pto Orvalho Max. (C)', 'Pto Orvalho Min. (C)']
    for col in colunas_orvalho:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')
    
    # Extraindo o mês para agrupamento
    df['Mes'] = df['Data_Hora'].dt.month
    df['Dia'] = df['Data_Hora'].dt.day

    # Filtrando apenas o mês 6 (junho)
    df_junho = df[df['Mes'] == 6]

    # Agrupando por dia e calculando a média diária para o mês de junho
    media_diaria_junho = df_junho.groupby(['Dia'])[colunas_orvalho].mean().reset_index()

    plt.figure(figsize=(12, 6))

    # Variáveis para controlar a exibição única das legendas
    legend_labels = []
    
    # Plotando os dados para o mês de junho
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pto Orvalho Ins. (C)'], color='skyblue')
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pto Orvalho Max. (C)'], color='orange')
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pto Orvalho Min. (C)'], color='lightgreen')

    # Adicionando os rótulos na legenda apenas uma vez
    if 'Ponto de Orvalho Ins.' not in legend_labels:
        legend_labels.append('Ponto de Orvalho Ins.')
    if 'Ponto de Orvalho Max.' not in legend_labels:
        legend_labels.append('Ponto de Orvalho Max.')
    if 'Ponto de Orvalho Min.' not in legend_labels:
        legend_labels.append('Ponto de Orvalho Min.')

    # Linhas ideais
    plt.axhline(y=20, color='red', linestyle=':', label='Mínimo Ideal (10°C)')
    plt.axhline(y=18, color='green', linestyle='--', label='Máximo Ideal (16°C)')

    # Custom Legend (exibindo cada rótulo apenas uma vez)
    plt.legend(legend_labels + ['Mínimo Ideal (10°C)', 'Máximo Ideal (16°C)'], loc='lower right')

    plt.title('Ponto de Orvalho - Junho')
    plt.xlabel('Dia do mês')
    plt.ylabel('Ponto de Orvalho (°C)')
    plt.grid(True)
    plt.xticks(range(1, 32))  # Ticks para todos os dias do mês
    plt.tight_layout()
    plt.show()

def pressao(arqui):
    # Pressao Ins. (hPa);Pressao Max. (hPa);Pressao Min. (hPa)
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    # Colunas do ponto de orvalho
    colunas_pressao = ['Pressao Ins. (hPa)', 'Pressao Max. (hPa)', 'Pressao Min. (hPa)']

    for col in colunas_pressao:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data-Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')

    df['Mes'] = df['Data-Hora'].dt.month
    df['Dia'] = df['Data-Hora'].dt.day

    df_junho = df[df['Mes'] == 6]

    media_diaria_junho = df_junho.groupby(['Dia'])[colunas_pressao].mean().reset_index()

    plt.figure(figsize=(10, 6))

    legend_labels = []

    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pressao Ins. (hPa)'], color='skyblue')
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pressao Max. (hPa)'], color='orange')
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pressao Min. (hPa)'], color='lightgreen')

    if 'Pressao Ins.' not in legend_labels:
        legend_labels.append('Pressao Ins.')
    if 'Pressao Max.' not in legend_labels:
        legend_labels.append('Pressao Max.')
    if 'Pressao Min.' not in legend_labels:
        legend_labels.append('Pressao Min.')    

    # plt.axhline(y=10, color='red', linestyle=':', label='Minimo Ideal (10 (hPa))')
    # plt.axhline(y=20, color='green', linestyle='--', label='Maximo Ideal (20 (hPa))')

    plt.legend(legend_labels + ['Minimo Ideal (10 (hPa))', 'Maximo Ideal (20 (hPa))'], loc='upper right')

    plt.title('Pressao registrada no mês de Junho')
    plt.xlabel('Dia do mês')
    plt.ylabel('Pressao em (hPa)')
    plt.grid(True)
    plt.xticks(range(1, 32))
    plt.tight_layout()
    plt.show()

pressao(caminho_csv)