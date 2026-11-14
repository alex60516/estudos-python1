import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("cartas.csv")

media_por_tipo = tabela.groupby("tipo")["raridade"].mean()

tabela.plot(x="nome", y="custo", kind="bar")

media_por_tipo.plot(kind="bar")
plt.title("custo medio por tipo")
plt.ylabel("elixir")
plt.show()