import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dados = pd.read_csv(r"C:\Users\eliel\Desktop\grupo03\Arquivo-trabalho\Documento-Limpo-grupo03.csv", delimiter=",")

# Agrupar por Ano e Produto e somar a área plantada
area_por_ano_produto = dados.groupby(['Ano', 'Produto'])['ÁreaPlantada (ha)'].sum().reset_index()
print(area_por_ano_produto)

# Calcular a diferença entre a área plantada e a área colhida
dados['Diferença (ha)'] = dados['Área Plantada (ha)'] - dados['ÁreaColhida (ha)']

# Agrupar por Produto e calcular a média da diferença
diferenca_por_produto = dados.groupby(['Produto'])['Diferença(ha)'].mean().reset_index()

# Encontrar o produto com a menor diferença média (maior índice decolheita)
produto_maior_indice_colheita = diferenca_por_produto.loc[diferenca_por_produto['Diferença (ha)'].idxmin(), 'Produto']

# Filtrar apenas os dados de 2024 para a cidade de Manaus
dados_manaus_2024 = dados[(dados['Ano'] == 2024) &(dados['Município'].str.lower() == 'manaus')]

soma_area_plantada_manaus_2024 = dados_manaus_2024['Área Plantada(ha)'].sum()

for produto in zip(dados_manaus_2024['Ano'], dados_manaus_2024['Produto'],dados_manaus_2024['Área Plantada (ha)']):
    print(f"Ano: {produto[0] } ---- Produto {produto[1]} ---- ÁreaPlantada {produto[2]}")

print('----------------------------------------------------------')
print(f"Total da Área Planata em 2024 na cidade de Manaus = {soma_area_plantada_manaus_2024.round(2)}")

amplitude_geral = dados['Produção (ton)'].max() - dados['Produção(ton)'].min()

# Calcular a amplitude por produto
amplitude_por_produto = dados.groupby('Produto')['Produção (ton)'].agg(['max', 'min'])
amplitude_por_produto['Amplitude'] = amplitude_por_produto['max'] -amplitude_por_produto['min']

# Exibir os resultados
print(f"Amplitude Geral da Produção: {amplitude_geral} ton\n")
print("Amplitude de Produção por Produto:")
print(amplitude_por_produto[['max', 'min', 'Amplitude']])