import pandas as pd

tabela = pd.read_csv("notas.csv")

print(tabela)
print(tabela["nota"].mean())
print(tabela[tabela["nota"] >= 6])