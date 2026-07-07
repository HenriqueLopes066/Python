import random

print("=============================")
print("        Jogo do Sapo ")
print("=============================")


sapo = str(input("\nDigite o nome do sapo: "))
pulo = 0

direita = 1
esquerda = 2

while True:
    pedra = random.randint(1, 2)
    tentativa = int(input(" \nEscolha em qual pedra pular, Digite 1 para Direita e 2 para Esquerda: "))
    
    if tentativa == pedra:
        print("Parabens, Você acertou o pulo!")
        pulo += 1
        print("O sapo está na pedra ", pulo)
        
        if pulo >= 5:
            print("O sapo chegou ao fim do rio!")
            break

        
        
    elif tentativa != pedra:
        print("O sapo pulou na pedra errada e caiu na água!")
        pulo = 0
        print("O sapo voltou a pedra inicial ", pulo)


    else:
        print("Opção inválida, tente novamente!")

         
        

