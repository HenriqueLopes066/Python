print("===================")
print("   Temperatura   ")
print("===================")

temperatura = int(input("Digite a temperatura: "))
chuva = input("Está chovendo? (s/n): ")
if temperatura < 15 and chuva == "s":
    print("Está frio e chovendo, use casaco impermeável e bota.")
elif temperatura < 15 and chuva == "n":
    print("Está frio, mas não está chovendo, use casaco pesado.")
elif temperatura >= 15 or chuva == "n":
    print("Está quente, use casaco leve.")

















