import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

# Lê o arquivo CSV
data = pd.read_csv('dados.csv')

# Seleciona as colunas desejadas
X = data[['coluna1']]
y = data[['coluna2']]

kf = KFold(n_splits=5) # Cria o objeto k-fold com 5 folds

scores = []
for train_index, val_index in kf.split(X):
    X_train, X_val = X.iloc[train_index], X.iloc[val_index]
    y_train, y_val = y.iloc[train_index], y.iloc[val_index]
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    score = model.score(X_val, y_val)
    scores.append(score)
    
print("Média das métricas de desempenho:", sum(scores) / len(scores))



##Aqui, a função pd.read_csv("dados.csv") é usada para ler o arquivo CSV 
# e armazená-lo em um DataFrame do pandas. Em seguida, as colunas 
# "coluna_entrada" e "coluna_saida" são extraídas do DataFrame e convertidas em 
# arrays numpy, que são usados como entrada e saída