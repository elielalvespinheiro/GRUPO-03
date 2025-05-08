import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Documento-Limpo-grupo03.csv', sep=";", decimal=",")

    # Substituir vírgulas por pontos e converter colunas numéricas
df = df.replace(',', '.', regex=True)

colunas_numericas = [
    'Temp. Ins. (C)', 'Temp. Max. (C)', 'Temp. Min. (C)',
    'Umi. Ins. (%)', 'Umi. Max. (%)', 'Umi. Min. (%)'
]

for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['Data'] = df['Data'].astype(str)
df['Hora (UTC)'] = df['Hora (UTC)'].astype(str).str.zfill(4)
df['Data_Hora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M')
df['Hora'] = df['Data_Hora'].dt.hour

    # Agrupamentos
media_por_hora_temperatura_ins = df.groupby('Hora')['Temp. Ins. (C)'].mean()
media_por_hora_temperatura_max = df.groupby('Hora')['Temp. Max. (C)'].mean()
media_por_hora_temperatura_min = df.groupby('Hora')['Temp. Min. (C)'].mean()

mediaUmidadeIdeal = df.groupby('Hora')['Umi. Ins. (%)'].mean()
mediaUmidadeMax = df.groupby('Hora')['Umi. Max. (%)'].mean()
mediaUmidadeMin = df.groupby('Hora')['Umi. Min. (%)'].mean()

    # Gráfico com dois eixos Y
fig, ax1 = plt.subplots(figsize=(14, 6))

    # Umidade (eixo Y da esquerda)
ax1.plot(mediaUmidadeIdeal.index, mediaUmidadeIdeal, label='Umidade Inst.', color='blue', marker='o')
ax1.plot(mediaUmidadeMax.index, mediaUmidadeMax, label='Umidade Máx.', color='green', marker='s')
ax1.plot(mediaUmidadeMin.index, mediaUmidadeMin, label='Umidade Mín.', color='red', marker='x')
ax1.axhline(y=65, color='red', linestyle='--', label='Limite Inf. (65%)')
ax1.axhline(y=85, color='green', linestyle='--', label='Limite Sup. (85%)')
ax1.set_ylabel('Umidade (%)', color='blue')
ax1.set_ylim(0, 100)
ax1.tick_params(axis='y', labelcolor='blue')

    # Temperatura (eixo Y da direita)
ax2 = ax1.twinx()
ax2.plot(media_por_hora_temperatura_ins.index, media_por_hora_temperatura_ins, label='Temp. Inst.', color='brown', linestyle='-')
ax2.plot(media_por_hora_temperatura_max.index, media_por_hora_temperatura_max, label='Temp. Máx.', color='orange', linestyle='--')
ax2.plot(media_por_hora_temperatura_min.index, media_por_hora_temperatura_min, label='Temp. Mín.', color='purple', linestyle='-.')
ax2.set_ylabel('Temperatura (°C)', color='brown')
ax2.tick_params(axis='y', labelcolor='brown')

    # Legendas
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper center', ncol=3)

plt.title('Variação de Umidade e Temperatura por Hora')
plt.xlabel('Hora do Dia')
plt.xticks(range(0, 31))
plt.grid(True)
plt.tight_layout()
plt.show()