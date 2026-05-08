import pandas as pd

df = pd.read_csv('tarefas.csv')

def numero_inteiro_valido(val):
    try:
        f = float(str(val).strip())
        return f == int(f)
    except:
        return False

def para_inteiro(val):
    return int(float(str(val).strip()))

mask = df['complexidade'].apply(numero_inteiro_valido) & df['tempo_horas'].apply(numero_inteiro_valido)
df = df[mask].copy()
df['complexidade'] = df['complexidade'].apply(para_inteiro)
df['tempo_horas']  = df['tempo_horas'].apply(para_inteiro)
df = df[(df['complexidade'] >= 1) & (df['complexidade'] <= 10)]

df.to_csv('tarefas_limpo.csv', index=False)
print(f"Dados limpos: {len(df)} linhas salvas em tarefas_limpo.csv")