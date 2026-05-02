import pandas as pd
 
df = pd.read_csv('tarefas.csv')
total_antes = len(df)
 
def num_inteiro_valido(val):
    try:
        f = float(str(val).strip())
        return f == int(f)
    except:
        return False
 
mask = df['complexidade'].apply(num_inteiro_valido) & df['tempo_horas'].apply(num_inteiro_valido)
removidas = df[~mask].copy()
df = df[mask].copy()
 
df['complexidade'] = df['complexidade'].apply(lambda x: int(float(str(x).strip())))
df['tempo_horas']  = df['tempo_horas'].apply(lambda x: int(float(str(x).strip())))
 
df = df[(df['complexidade'] >= 1) & (df['complexidade'] <= 10)]
 
df.to_csv('tarefas_limpo.csv', index=False)
 
print(f"Antes: {total_antes} linhas | Removidas: {total_antes - len(df)} | Depois: {len(df)} linhas válidas\n")
print("Linhas removidas:")
print(removidas.to_string(index=False))
 