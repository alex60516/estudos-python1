import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("cartas.csv")

print(tabela["custo"].mean)
print(tabela["custo"].median())
print(tabela["custo"].std())
print(tabela["custo"].describe())

tabela["custo"].plot(kind="hist")
plt.title("descriçao do custo das cartas")
plt.xlabel("elixir")
plt.ylabel("quantidade de cartas")
plt.show()

tabela.groupby("tipo")["custo"].median()

tropa = tabela[tabela["tipo"] == "tropa"]
print(tropa["custo"].describe())

