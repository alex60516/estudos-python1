#try:
#    numero = int(input("digite um numero: "))
#    print("o dobro é", numero * 2)
#except ValueError:
#    print("isso é um erro")

#print("o programa continua normalmente")

#try: #cloud, vou colocar alguns rascunhos tipo esse e vc le pra nao ficar perdido (ex1)
#    numero = int(input("digite um numero: "))
#    print("o valor da divisao por zero é", numero / 0)
#except ZeroDivisionError:
#    print("é um erro")

#print("roda normal")

#try: #ex1 com uma variacao no codigo que fiz pra experimentar
#    numero1 = 0
#    print("o resultado da divisao é", numero1 / 0)
#except ZeroDivisionError:
#    print("erro")

#print("normal")

while True:
    try:
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite um numero: "))
        resultado = numero1 / numero2
        break
    except ValueError:
        print("isso nao é um numero, tente novamnete")
    except ZeroDivisionError:
        print("nao da pra dividir por zero, tente de novo")

print("resultado", resultado)