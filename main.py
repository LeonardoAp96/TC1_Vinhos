#Manipulação de dados
import pandas as pd
import numpy as np

#Visualização de dados
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Lendo o arquivo
try:
    df = pd.read_csv('csv/Producao.csv')
except FileNotFoundError:
    print("Arquivo não encontrado.")
    exit()

print("Primeiras linhas do DataFrame:")
print(df.head(2))

print(df.info())

print(df.shape)