import pandas as pd
from sklearn.linear_model import LinearRegression

treino = pd.read_csv('dados_treino.csv')

X_train = treino[['complexidade']]
y_train = treino['tempo_horas']

modelo = LinearRegression()
modelo.fit(X_train, y_train)

print(f"Modelo treinado!")
print(f"Fórmula: tempo = {modelo.coef_[0]:.2f} * complexidade + {modelo.intercept_:.2f}")