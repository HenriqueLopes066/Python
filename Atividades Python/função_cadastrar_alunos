alunos = []


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    aluno = {
        "nome": nome,
        "idade": idade
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
    else:
        print("\n--- ALUNOS CADASTRADOS ---")

        for aluno in alunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print("------------------------")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


menu()
