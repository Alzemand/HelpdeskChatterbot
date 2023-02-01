import pandas as pd
from scipy.stats import ttest_ind

# Lê o arquivo CSV
data = pd.read_csv('dados.csv')

# Seleciona as colunas desejadas e converte para números
coluna1 = pd.to_numeric(data['coluna1'], errors='coerce')
coluna2 = pd.to_numeric(data['coluna2'], errors='coerce')

# Remove valores NaN
coluna1 = coluna1.dropna()
coluna2 = coluna2.dropna()

# Executa o teste T
t, p = ttest_ind(coluna1, coluna2)

print("Valor de t:", t)
print("Valor de p:", p)


'''Aqui, usamos o método to_numeric para converter os valores da coluna para números e o argumento errors='coerce' para forçar o pandas a transformar os valores que não são números em NaN. Em seguida, usamos o método dropna para remover esses valores NaN antes de realizar o teste T. É importante lembrar que é preciso verificar se os dados são normalmente distribuidos antes de realizar teste T, caso contrário, é recomendado utilizar o teste de Wilcoxon.'''