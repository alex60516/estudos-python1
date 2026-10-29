#pessoa = {"nome": "ana", "idade": "25", "cidade": "cuiaba"}

#print(pessoa)
#print(pessoa["nome"])
#print(pessoa["idade"])

#pessoa["idade"] = 26
#pessoa["profissao"] = "analista"
#print(pessoa)

#for chave in pessoa:
#    print(chave, "->", pessoa[chave])

#ex1
player1 = {"nome": "steve", "idade": 50, "local": "overworld"}

print(player1["local"])

#ex2
nome = input("fala seu nome: ")
idade = int(input("fala sua idade: "))

player2 = {"nome": nome, "idade": idade}
print(player2)

#ex3
player4 = {"nome": "steve", "idade": 50, "local": "overworld"}
player5 = {"nome": "lucas", "idade": 50, "local": "end"}
player6 = {"nome": "luan", "idade": 50, "local": "nether"}

jogadores = [player4, player5, player6]

for jogador in jogadores:
    print(jogador["nome"])