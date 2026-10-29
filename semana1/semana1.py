#nome = input("qual o seu nome?")

#idade = int(input("qual a sua idade?"))

#print("ola",nome)
#print("ano que vem voce tera", idade + 1, "anos")

#if idade >= 18:
#    print("voce é maior de idade")
#else:
#    print("voce é menor de idade")

#anoNascimento = 2026

#anoNovo = int(input("qual a sua o ano de seu nascimento?"))

#anoNascimento = anoNascimento - anoNovo

#print("voce tem", anoNascimento, "anos!")

#numero1 = int(input("escolha um numero "))
#numero2 = int(input("escolha mais um numero "))

#resultado1 = numero1 + numero2
#resultado2 = numero1 - numero2
#resultado3 = numero1 * numero2

#if numero2 == 0:
#    print("nao é possivel dividir por zero")
#else:
#    divisao = numero1 / numero2
#    print("divisao:", divisao)

#print("sua resposta é", resultado1)
#print("sua resposta é", resultado2)
#print("sua resposta é", resultado3)

#for i in range(6): #for: repete um numero definido de vezes
#    print("volta numero", 1)

#contador = 1 
#while contador <=3:
#    print("contador:", contador)
#    contador = contador + 1
#ex1
#for i in range(1, 11):
#    print(i)

#ex2
#numero = int(input("diga um numero: "))
#for i in range(1, 11):
#   print(numero, "x", i, "=", numero * i)
 
#ex3
#senha_correta = 12345
#tentativa = int(input("digite a senha: "))

#while tentativa != senha_correta:
#    print("senha incorreta, tente novamente")
#    tentativa = int(input("tente novamente"))

#print("senha correta!")

#numeros = [5, 12, 8, 20, 3, 15]
#total = 0
#contador = 0

#for numero in numeros:
#    if numero > 10:
#        contador = contador + 1
#        print(numero, "é maior que 10")

#for numero in numeros:
#    if numero % 2 == 0:
#        print(numero)

#for numero in numeros:
#    if numero > 10:
#        total = total + numero

#print(total)
#print(contador)

#def saudacao(nome):
#    print("ola", nome)

#saudacao("ana")
#saudacao("lucas")

#def somar(a, b):
#    resultado = a + b
#    return resultado

#total = somar(3, 4)
#print(total)
#print(somar(10, 20))

#def triplo(numero):
#    return numero * 3
#print(triplo(4))

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(eh_par(4))
print(eh_par(7))

def soma_lista(lista):
    total = 0
    for numero in lista:
        total = total + numero
    return total

print(soma_lista([10, 20, 30]))
