import pandas as pd
df = pd.read_csv(r'C:\Users\aluno noturno\Desktop\grupo03\Arquivo-trabalho\Documento-grupo03.csv', delimiter=';', encoding='UTF-8')
df = df.dropna()
df.to_csv('aleatoriozao1.csv', index=False)