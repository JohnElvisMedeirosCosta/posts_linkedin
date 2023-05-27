import pandas as pd

# Criação de um DataFrame
data = {'Nome': ['João', 'Maria', 'Pedro'],
        'Idade': [25, 30, 35],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']}
df = pd.DataFrame(data)
print(df)
# Saída:
#    Nome  Idade          Cidade
# 0  João     25       São Paulo
# 1 Maria     30  Rio de Janeiro
# 2 Pedro     35  Belo Horizonte

# Seleção de colunas
print(df['Nome'])
# Saída:
# 0     João
# 1    Maria
# 2    Pedro
# Name: Nome, dtype: object

print(df[['Nome', 'Idade']])
# Saída:
#    Nome  Idade
# 0  João     25
# 1 Maria     30
# 2 Pedro     35

# Filtro de linhas
filtro = df['Idade'] > 28
print(df[filtro])
# Saída:
#    Nome  Idade          Cidade
# 1 Maria     30  Rio de Janeiro
# 2 Pedro     35  Belo Horizonte

# Ordenação
df_sorted = df.sort_values('Idade')
print(df_sorted)
# Saída:
#    Nome  Idade          Cidade
# 0  João     25       São Paulo
# 1 Maria     30  Rio de Janeiro
# 2 Pedro     35  Belo Horizonte

# Operações estatísticas
print(df['Idade'].mean())
# Saída: 30.0

print(df['Idade'].max())
# Saída: 35
