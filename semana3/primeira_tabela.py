import pandas as pd

#dados = {
#    "nomes": ["ana", "lucas", "maria", "pedro", "julia"],
#    "notas": [8.5, 5.0, 9.5, 6.5, 4.0]
#}

#tabela = pd.DataFrame(dados)


#print(tabela)
#print(tabela["notas"].mean())
#print(tabela[tabela["notas"] >= 6])

dados = {
    "cartas": [" ""mega cavaleiro", "valkiria", "corredor", "bola de neve", "bola de fogo", "bruxa", "horda de servos", "barril de goblins"],
    "elixirCartas": [ 7, 4, 4, 3, 4, 5, 5, 3,],
}

tabela = pd.DataFrame(dados)

print(tabela)
print(tabela["elixirCartas"].mean())
print(tabela["elixirCartas"].sum())
print(tabela[tabela["elixirCartas"] >= 4])
print(tabela["elixirCartas"].max())
print(tabela["elixirCartas"].min())