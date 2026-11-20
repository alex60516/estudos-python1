import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("cartas.csv")

contagem = tabela["tipo"].value_counts()
print(contagem)

contagem.plot(kind="pie", autopct="%1.0f%%")
plt.title("cartas por tipo")
plt.ylabel("")
plt.show()

contagem = tabela["raridade"].value_counts()
print(contagem)

contagem.plot(kind="pie", autopct="%1.0f%%")
plt.title("cartas por raridade")
plt.ylabel("")
plt.show()

contagem.plot(kind="bar")
plt.title("cartas por raridade")
plt.ylabel("quantidades de cartas")
plt.show()



