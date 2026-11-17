import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("cartas.csv")

media_por_tipo = tabela.groupby("raridade")["custo"].mean()
media_por_tipo.plot(kind="bar")
plt.title("custo medio por tipo")
plt.ylabel("elixir")
plt.show()

tabela.plot(x="nome", y="custo", kind="line")
plt.title("custo de cada carta")
plt.show()