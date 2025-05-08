import pandas as pd
import matplotlib.pyplot as plt

caminho_csv = 'Documento-Limpo-grupo03.csv'

# Importância: Temperaturas elevadas podem aquecer a água, 
# reduzir o oxigênio dissolvido e estressar os peixes. 
# Baixas temperaturas podem diminuir o metabolismo e o apetite.

# Importância: Umidade influencia a taxa de evaporação da água dos tanques. 
# Menor umidade = mais evaporação → maior concentração de substâncias → possível estresse hídrico.

# Importância: Pode indicar mudanças climáticas rápidas e formação de neblina, 
# que afeta radiação solar e temperatura da água, influenciando o comportamento dos peixes.

# Importância: Mudanças bruscas na pressão afetam o comportamento dos peixes. 
# Queda de pressão costuma deixar os peixes menos ativos e menos propensos a se alimentar.

# Importância: Vento pode causar agitação da água (aerando-a naturalmente) ou, 
# em excesso, provocar ondas que prejudicam estruturas ou estressam os peixes.

df = pd.read_csv(caminho_csv, sep=';', decimal=',', encoding='utf-8')
df = df.replace(',', '.', regex=True)

def temperatura(arqui):
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    colunas_numericas = ['Temp. Ins. (C)', 'Temp. Max. (C)', 'Temp. Min. (C)']
    for col in colunas_numericas:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')
    df['Mes'] = df['Data_Hora'].dt.day

    meses_desejados = [6]

    df = df[(df['Data_Hora'].dt.month.isin(meses_desejados)) & (df['Data_Hora'].dt.day <= 30)]

    media_temp_ins = df.groupby('Mes')["Temp. Ins. (C)"].mean()
    media_temp_max = df.groupby('Mes')["Temp. Max. (C)"].mean()
    media_temp_min = df.groupby('Mes')["Temp. Min. (C)"].mean()

    plt.figure(figsize=(10, 6))

    plt.plot(media_temp_ins, label='Temp. Instantânea', color='#0000CD')
    plt.plot(media_temp_max, label='Temp. Máxima', color='red')

    valor_maximo = 30
    valor_minimo = 26
    plt.axhline(y=valor_maximo, color='green', linestyle='--', label='Temperatura Máxima Ideal')
    plt.axhline(y=valor_minimo, color='red', linestyle=':', label='Temperatura Mínima Ideal')

    plt.plot(media_temp_min, label='Temp. Mínima', color='#FFD700')

    plt.title('Temperaturas ao Longo do Tempo - Junho')
    plt.xlabel('Dias capturados')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(range(1, 32))

    plt.tight_layout()
    plt.show()

def umidade(arqui):
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    colunas_umidade = ['Umi. Ins. (%)', 'Umi. Max. (%)', 'Umi. Min. (%)']
    for col in colunas_umidade:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')
    df['Dia'] = df['Data_Hora'].dt.day
    df['Mes'] = df['Data_Hora'].dt.month

    meses_desejados = [6] 
    df = df[df['Mes'].isin(meses_desejados)]

    df['Mes-Dia'] = df['Data_Hora'].dt.strftime('%m-%d')

    media_ur_ins = df.groupby('Mes-Dia')["Umi. Ins. (%)"].mean()
    media_ur_max = df.groupby('Mes-Dia')["Umi. Max. (%)"].mean() 
    media_ur_min = df.groupby('Mes-Dia')["Umi. Min. (%)"].mean() 

    df_umidade = pd.DataFrame({
        'UR Instantânea': media_ur_ins,
        'UR Máxima': media_ur_max,
        'UR Mínima': media_ur_min
    })

    ax = df_umidade.plot(kind='line', figsize=(12, 6), color=['dodgerblue', 'green', 'red'], linewidth=2)

    valor_maximo = 58
    valor_minimo = 53
    ax.axhline(y=valor_maximo, color='green', linestyle='--', label='Ponto Máximo Ideal')
    ax.axhline(y=valor_minimo, color='red', linestyle=':', label='Ponto Mínimo Ideal')

    ax.set_title('Umidade Relativa do Ar - Junho')
    ax.set_xlabel('Data (Mês-Dia)')
    ax.set_ylabel('Umidade (%)')
    ax.set_xticks(range(len(df_umidade.index)))
    ax.set_xticklabels(df_umidade.index, rotation=90)
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

def orvalho(arqui):
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    colunas_orvalho = ['Pto Orvalho Ins. (C)', 'Pto Orvalho Max. (C)', 'Pto Orvalho Min. (C)']
    for col in colunas_orvalho:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')
    
    df['Mes'] = df['Data_Hora'].dt.month
    df['Dia'] = df['Data_Hora'].dt.day

    df_junho = df[df['Mes'] == 6]

    media_diaria_junho = df_junho.groupby(['Dia'])[colunas_orvalho].mean().reset_index()

    plt.figure(figsize=(12, 6))

    legend_labels = []
    
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pto Orvalho Ins. (C)'], color='#00FF00')
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pto Orvalho Max. (C)'], color='orange')
    plt.plot(media_diaria_junho['Dia'], media_diaria_junho['Pto Orvalho Min. (C)'], color='#4B0082')

    if 'Ponto de Orvalho Ins.' not in legend_labels:
        legend_labels.append('Ponto de Orvalho Ins.')
    if 'Ponto de Orvalho Max.' not in legend_labels:
        legend_labels.append('Ponto de Orvalho Max.')
    if 'Ponto de Orvalho Min.' not in legend_labels:
        legend_labels.append('Ponto de Orvalho Min.')

    plt.axhline(y=18, color='red', linestyle=':', label='Mínimo Ideal (18°C)')
    plt.axhline(y=20, color='green', linestyle='--', label='Máximo Ideal (20°C)')
    plt.legend(legend_labels + ['Mínimo Ideal (18°C)', 'Máximo Ideal (20°C)'], loc='lower left')
    plt.title('Ponto de Orvalho - Junho')
    plt.xlabel('Dia do mês')
    plt.ylabel('Ponto de Orvalho (°C)')
    plt.grid(True)
    plt.xticks(range(1, 32))
    plt.tight_layout()
    plt.show()

def pressao(arqui):
    df = pd.read_csv(arqui, sep=';', decimal=',', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    colunas_pressao = ['Pressao Ins. (hPa)', 'Pressao Max. (hPa)', 'Pressao Min. (hPa)']
    for col in colunas_pressao:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'],format='%d/%m/%Y %H%M', errors='coerce')

    df['Mes'] = df['Data_Hora'].dt.month
    df['Dia'] = df['Data_Hora'].dt.day

    df = df[(df['Mes'] == 6) & (df['Dia'] <= 31)]

    plt.figure(figsize=(12, 6))

    plt.scatter(df['Dia'], df['Pressao Ins. (hPa)'], color='#000000', label='Pressao Ins.', s=10)
    plt.scatter(df['Dia'], df['Pressao Max. (hPa)'], color='orange', label='Pressao Max.', s=10)
    plt.scatter(df['Dia'], df['Pressao Min. (hPa)'], color='lightgreen', label='Pressao Min.', s=10)

    plt.axhline(y=1010, color='red', linestyle=':', label='Minimo Ideal (1010 hPa)')
    plt.axhline(y=1020, color='green', linestyle='--', label='Maximo Ideal (1020 hPa)')

    plt.legend(loc='upper right', bbox_to_anchor=(1.0, 0.9))
    plt.title('Pressão registrada em Junho (valores reais por dia)')
    plt.xlabel('Dia do mês')
    plt.ylabel('Pressão em (hPa)')
    plt.grid(True)
    plt.xticks(range(1, 32)) 
    plt.tight_layout()
    plt.show()

def vento(arqui):
    df = pd.read_csv(arqui, sep=";")

    df["Vel. Vento (m/s)"] = df["Vel. Vento (m/s)"].astype(str).str.replace(",", ".").astype(float)
    df["Raj. Vento (m/s)"] = df["Raj. Vento (m/s)"].astype(str).str.replace(",", ".").astype(float)
    df["Dir. Vento (m/s)"] = df["Dir. Vento (m/s)"].astype(str).str.replace(",", ".").astype(float)

    df["Data_Hora"] = pd.to_datetime(
        df["Data"] + " " + df["Hora (UTC)"].astype(str).str.zfill(4), format="%d/%m/%Y %H%M"
    )

    df_junho = df[df["Data_Hora"].dt.month == 6].copy()
    df_junho["Dia"] = df_junho["Data_Hora"].dt.day

    dados_agrupados = df_junho.groupby("Dia").agg({
        "Vel. Vento (m/s)": "mean",
        "Raj. Vento (m/s)": "mean",
        "Dir. Vento (m/s)": "mean"
    }).reset_index()

    plt.figure(figsize=(10, 6))

    plt.plot(dados_agrupados["Dia"], dados_agrupados["Vel. Vento (m/s)"], label="Vel. Vento (m/s)", color="blue")
    plt.plot(dados_agrupados["Dia"], dados_agrupados["Raj. Vento (m/s)"], label="Raj. Vento (m/s)", color="green")
    plt.plot(dados_agrupados["Dia"], dados_agrupados["Dir. Vento (m/s)"], label="Dir. Vento (m/s)", color="red")

    plt.title("Média de Velocidade, Rajada e Direção do Vento em Junho")
    plt.xlabel("Dia do Mês")
    plt.ylabel("Média (m/s) / Direção (m/s)")
    plt.legend(loc='lower right', bbox_to_anchor=(1.0, 0.1))

    plt.grid(True)
    plt.show()

def analisar_radiacao_e_energia(arquivo, area_painel, eficiencia):
    
    df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
    df = df.replace(',', '.', regex=True)

    df['Radiacao (KJ/m²)'] = pd.to_numeric(df['Radiacao (KJ/m²)'], errors='coerce')
    df['Radiacao (kWh/m²)'] = df['Radiacao (KJ/m²)'] * 0.0002778

    df['Data'] = df['Data'].astype(str)
    df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
    df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M', errors='coerce')
    df['Dia'] = df['Data_Hora'].dt.day

    media_radiacao = df.groupby('Dia')['Radiacao (KJ/m²)'].mean()
    df_diario = df.groupby('Dia')['Radiacao (kWh/m²)'].sum().reset_index()

    df_diario['Energia Gerada (kWh/dia)'] = df_diario['Radiacao (kWh/m²)'] * area_painel * eficiencia

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(media_radiacao.index, media_radiacao.values, color='orange', linewidth=2, label='Radiação Média (kJ/m²)')
    ax1.set_title('Radiação Solar e Energia Gerada por Dia', fontsize=16)
    ax1.set_xlabel('Dia do Mês')
    ax1.set_ylabel('Radiação Média (kJ/m²)', color='orange')
    ax1.tick_params(axis='y', labelcolor='orange')

    ax2 = ax1.twinx()
    ax2.plot(df_diario['Dia'], df_diario['Energia Gerada (kWh/dia)'], color='green', linewidth=2, label='Energia Gerada (kWh/dia)')
    ax2.set_ylabel('Energia Gerada (kWh/dia)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.xticks(range(1, 32))
    fig.tight_layout()
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.grid(True)
    plt.show()

    print(df_diario[['Dia', 'Energia Gerada (kWh/dia)']])

temperatura(caminho_csv)
umidade(caminho_csv)
orvalho(caminho_csv)
pressao(caminho_csv)
vento(caminho_csv)
analisar_radiacao_e_energia(caminho_csv, area_painel=20, eficiencia=80)