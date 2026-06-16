print("=====================================")
print("   Controle de Entrada de um evento  ")
print("=====================================")


pessoa_perm = 0
pessoa_negada = 0
nomes = []

while True:

    nomes.append(str(input("\nDigite seu nome: ")))

    idade = int(input("\nDigite sua idade: "))

    if idade >= 18:
        print("Entrada permitida!")
        pessoa_perm += 1
        

    elif idade <18:
        print("Entrada negada!")
        pessoa_negada += 1
        

    else:
        print("Idade inválida, tente novamente!")
    
    continuar = str(input("\n Deseja continuar? (s/n): "))
    print("=====================================")
    if continuar == "n":
        break

print(" Total de pessoas que foram negadas: ", pessoa_negada)
print(" Total de pessoas que entraram: ", pessoa_perm) 

print(" lista de pessoas: ", nomes)