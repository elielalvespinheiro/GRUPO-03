import pandas as pd

# abrir arquivo
df = pd.read_csv(r'C:\Users\aluno noturno\Desktop\grupo03\Arquivo-trabalho\Documento-grupo03.csv', delimiter=';', encoding='UTF-8')

# verificar valores vazios
valoresVazios = df.isnull().sum()
print(valoresVazios)

# apagar valores vazios
df.fillna(0, inplace=False)

# apaga as linhs vazias
df = df.dropna()

#excluir duplicados
if (df.drop_duplicates(inplace=True)):
    print("\n\n Funcionou \n\n")
else:
    print('\n \n nao funcionou \n \n')


# varificar novamente se esta nulo
print(df.isnull().sum())

# criar arquivo limpo
df.to_csv(r'C:\Users\aluno noturno\Desktop\grupo03\Arquivo-trabalho\Documento-Limpo-grupo03.csv', index=False)