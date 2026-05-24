print("=============================")
print("IDADE DO NADADOR")
print("=============================")

nome = input("\nDigite seu nome: ")

idade = int(input("Digite sua idade: "))

if idade < 5:
    print("Sua Classe é: Muito Jovem")
elif idade >= 5 and idade <= 7:
    print("Sua Classe é: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Sua Classe é: Infantil B")
elif idade >= 11 and idade <= 17:
    print("Sua Classe é: Juvenil")
else:
    print("Sua Classe é: Sênior")
