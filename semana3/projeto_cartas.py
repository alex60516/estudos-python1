import pandas as pd

tabela = pd.read_csv("cartas.csv")

print(tabela)

print(tabela["custo"].mean())

print(tabela[tabela ["custo"] >= 4])

print(tabela.groupby("tipo")["custo"].mean())

print(tabela.groupby("raridade")["custo"].mean())

print(tabela["custo"].max())

print(tabela[tabela["custo"] == tabela["custo"].max()])
