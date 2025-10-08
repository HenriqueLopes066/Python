while True:
    print("="*30)
    print("Cadastro de usuários")
    print("="*30)
    print("1- Cadastrar usuário")
    print("2- Atualizar Usuário")
    print("3- Deletar Usuário")
    print("4- Listar Usuário")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    
    if opcao == "1":
        nome = input("Digite seu nome: ")
        "usuarios".append(nome)
    elif opcao == "2":
        atualizar_usuario = input("digite seu novo nome: ")
        "usuarios".appende("novo nome")
        
        pass
    elif opcao == "3":
        deletar_usuario = input("qual usuario pretende remover?: ")
        "usuarios".remove(nome)
        pass
    elif opcao == "4":
        pass
    elif opcao == "q":
        pass
    else:
        print("Resposta Inválida")
    