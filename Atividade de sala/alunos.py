print("===============================")
print(        "Cadastrar Alunos     ")
print("===============================")

alunos = []

while True:

    print("\n1-Cadastrar Alunos")
    print(" \n2-Listar Alunos")
    print(" \n3-Sair")

    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:

        alunos.append(str(input("\nDigite o nome do aluno: ")))


    elif opcao == 2:
        if len(alunos) == 0:
            print("\nNenhum aluno cadastrado!")
        else:
            print("\nAlunos cadastrados:")
            for aluno in alunos:
                print(aluno)
            
    elif opcao == 3:    
        break
    else:
        print("\nOpção inválida, tente novamente!")













    continuar = str(input("\nDeseja continuar? (s/n): "))
    print("=====================================")
    if continuar == "n":
        break

