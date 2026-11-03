gastos =[]
while True:
    print("1 - adicionar gastos")
    print("2 - ver gastos")
    print("3 - atualizar dados")
    print("4 - sair")
    opcao = input("escolha: ")

    if opcao == "1":
        descricao = input("descriçao: ")
        valor = float(input("valor: "))
        gastos.append({"descriçao": descricao, "valor": valor})
        print("gasto adicionado")
    elif opcao == "2":
        for gasto in gastos:
            print(gasto["descriçao"], "-", gasto["valor"])
    elif opcao == "3":
        for i in range(len(gastos)):
            print(i + 1, "_", gastos[i]["descriçao"], "_", gastos[i]["valor"])
        numero = int(input("qual gasto editar? "))
        nova = input("nova descriçao ")
        gastos[numero - 1]["descriçao"] = nova
        print("descriçao atualizada ")
    elif opcao == "4":
        print("ate logo")
        break
    else:
        print("opçao invalida")