#escrever: cria o arquivo (apaga o que tinha antes)
#with open("notas.txt", "w") as arquivo:
#    arquivo.write("ana,8.5\n")
#    arquivo.write("lucas,5.0\n")

#acrescentar: adiciona no final sem apagar
#with open("notas.txt", "a") as arquivo:
#    arquivo.write("maria,9.5\n")

#ler: le linha por linha
#with open("notas.txt", "r") as arquivo:
#    for linha in arquivo:
#        print(linha.strip())

#with open("notas.txt", "a") as arquivo:
#    arquivo.write("jao, 4.5\n")


#try:
#    with open("nome.txt", "r") as arquivo:
#        nome = arquivo.read()
#    print("bem-vindo de volta,", nome)
#except FileNotFoundError:
#    nome = input("qual seu nome? ")
#    with open("nome.txt", "w") as arquivo:
#        arquivo.write(nome)
#    print("prazer,", nome)

#with open("compras.txt", "w") as arquivo:
#    arquivo.write("detergente\n" "carne\n" "arroz\n")

#with open("compras.txt", "r") as arquivo:
#    for linhaPORlinha in arquivo:
#        print(linhaPORlinha.strip())

#itemNovo = input("adicionar item ")

#with open("compras.txt", "a") as arquivo:
#    arquivo.write(itemNovo + "\n")

#with open("compras.txt", "r") as arquivo:
#    for linha in arquivo:
#        print(linha.strip())    

import json
import urllib.request

endereco = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

with urllib.request.urlopen(endereco) as resposta:
    dados = json.loads(resposta.read())

cotacao = float(dados["USDBRL"]["bid"])
print("cotaçao do dolar hoje", cotacao)

while True:
    try:
        dolares = float(input("quantos dolares? "))
        reais = dolares * cotacao
        break
    except ValueError:
        print("isso nao é um numero, tente de novo")

print(dolares, "dolares valem", reais, "reais")