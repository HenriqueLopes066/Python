print("====================================")
print("CONVERTENDO METROS EM CENTÍMETROS")
print("====================================")

metros = float(input("\nDigite quantos metros: "))
centimetros = float(input("\nDigite quantos centímetros: "))


def converter_centimtros(centimetros):
    return centimetros * 100


print(f"Centímetros em milímetros é: {converter_centimtros(centimetros)}")


def converter_metros(metros):
    return metros * 100


print(f" Metros em centímetros é: {converter_metros(metros)}")




