import random
print("======================================")
print("------JOGO DO ADIVINHE O NÚMERO------")
print("======================================")

while True:

    numero_secrt = random.randint(1,20)

    
    tentativa = int(input("\nTente adivinhar o número secreto:"))

    if tentativa == numero_secrt:
        print("Parabéns, acertou!!!")
        break
    else:
        print("\nErrou!!!, Tente novamente")
        print("-================================-")
        
    
    
        
