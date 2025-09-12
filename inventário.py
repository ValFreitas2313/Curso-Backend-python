inventario = [] # lista que vai guardar os itens

continuar = True

while continuar: 
    print("\n=== controle de inventario ===")

    print("1. adicionar item")
    print("2. remover item")
    print("4. sair")

    opcao = input("escolha uma opção:")
    if opcao == "1":
        nome = input("nome do item:")
        quantidade = int(input("qualidade: "))
        inventario.append({"nome": nome, "quantidade": quantidade})
        print("item adicionado com sucesso!")
    elif opcao == "2":
        nome = input("nome do item a remover: ")
        encontrado = False

        del(inventario[nome])
        print("item removido!")

        if not encontrado: print("item nao encontrado")
    elif opcao == "3":
        if len(inventario) == 0:
            print("inventario vazio.")
        else:print("\n itens no inventario:")
        for item in inventario:
            print(f"-{item['nome']}: {item['quantidade']}")
        
    else:
        continuar = False
        break
        print("opcao invalida, tente novamente.")
