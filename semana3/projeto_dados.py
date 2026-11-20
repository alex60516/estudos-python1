import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("biomes.csv")

print(tabela.shape)
print(tabela.head())
print(tabela.info())
print(tabela.isna().sum())

# quantos biomas existe em cada dimensao?
print(tabela["dimensionID"].value_counts())
contagem1 = tabela["dimensionID"].value_counts()

contagem1.plot(kind="bar")
plt.title("qtd de biomas por dimensao")
plt.ylabel("biomas")
plt.show()


#que tipo de precipitacao aparece mais
tabela["precipitation"] = tabela["precipitation"].fillna("nenhuma")
print(tabela["precipitation"].value_counts())

contagem2 =tabela["precipitation"].value_counts()

contagem2.plot(kind="pie", autopct="%1.0f%%")
plt.title("tipo de pecipitaçao")
plt.ylabel("")
plt.show()



#que proporcao dos biomas tem arvore ou grama, por dimensao?
print(tabela.groupby("dimensionID")["treesOrGrass"].mean())

contagem3 = tabela.groupby("dimensionID")["treesOrGrass"].mean()

contagem3.plot(kind="bar")
plt.title("proporçao de arvore e grama por dimensao")
plt.xlabel("dimensao")
plt.ylabel("proporçao")
plt.show()

