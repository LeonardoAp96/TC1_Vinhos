import pandas as pd

# Lendo o arquivo
try:
    df = pd.read_csv('csv/Producao.csv')
except FileNotFoundError:
    print("Arquivo não encontrado.")
    exit()

print("Primeiras linhas do DataFrame:")
print(df.head(2))

print(df.info())