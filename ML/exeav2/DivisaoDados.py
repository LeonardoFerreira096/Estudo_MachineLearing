import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('tarefas_limpo.csv')

X = df[['complexidade']]
y = df['tempo_horas']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pd.concat([X_train, y_train], axis=1).to_csv('dados_treino.csv', index=False)
pd.concat([X_test,  y_test],  axis=1).to_csv('dados_teste.csv',  index=False)
print(f"Treino: {len(X_train)} linhas | Teste: {len(X_test)} linhas")