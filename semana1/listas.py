#frutas = ["maça", "banana", "uva"]

#print(frutas)
#print(frutas[0])
#print(frutas[2])
#print(frutas[-1])

#frutas.append("laranja")
#print(frutas)

#print(len(frutas))

#for frutas in frutas:
#    print("eu gosto de", frutas)

#ex1
#numeros = [1, 2, 3, 4, 5]
#print(numeros[0])
#print(numeros[-1])

#ex2
nomes = ["joao", "maria", "pedro"]
novo_nome = input("digite o novo nome: ")

nomes.append(novo_nome)

for nome in nomes:
    print(nome)

#ex3
lista_numero = [2, 2, 2, 2, 2]
total = 0

for numero in lista_numero:
    total = total + numero

    print("e a soma de tudo: ", total)