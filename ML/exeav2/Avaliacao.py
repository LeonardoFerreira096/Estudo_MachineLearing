import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

treino = pd.read_csv('dados_treino.csv')
teste  = pd.read_csv('dados_teste.csv')

modelo = LinearRegression()
modelo.fit(treino[['complexidade']], treino['tempo_horas'])

y_pred = modelo.predict(teste[['complexidade']])

resultado = teste.copy()
resultado['tempo_previsto'] = y_pred.round(2)
resultado.to_csv('resultado.csv', index=False)

print(f"MAE  : {mean_absolute_error(teste['tempo_horas'], y_pred):.2f} horas")
print(f"RMSE : {np.sqrt(mean_squared_error(teste['tempo_horas'], y_pred)):.2f} horas")
print(f"R²   : {r2_score(teste['tempo_horas'], y_pred):.2f}")