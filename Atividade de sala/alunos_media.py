print("===============================")
print("         Notas da Turma        ")
print("===============================")


nome = []
nota1 = []
maior_nota = 10



while True:

    for i in range(int(input("\nDigite a quantidade de alunos: "))):
        nome.append(str(input("\nDigite o nome do aluno: ")))
        nota1.append(float(input("Digite a nota do aluno: ")))

        soma = sum(nota1)
        media = soma / len(nota1)

        if nota1[i] >= 7 and nota1[i] <= 10:
            print("\nAluno aprovado!")
            print("====================")

        elif nota1[i] >= 5 and nota1[i] < 7:
            print("\nAluno em recuperação!")
            print("=======================")

        else:
            print("\nAluno reprovado!")
            print("=======================")


    print("\nsoma das notas da turma: ", soma)
    print("média da turma: ", media)

    if nota1[i] == maior_nota:
        print(f"\nParabéns {nome[i]}, você tirou a nota máxima!")

    else:
        print(f"\n{nome[i]}, você tirou a nota mínima, estude mais!")
    

    continuar = input("Deseja continuar usando o programa? (s/n): ")

    if continuar == "n":
        break

    else:
        print("\nOpção inválida, tente novamente!")
