print("=====================")
print("   Valor do Imóvel   ")
print("=====================")


valor_imovel = int(input("\nDigite o valor do imóvel: "))

salario = int(input("Digite o valor do seu salário: "))

prazo_financeamento = int(input("Digite quantos anos de financiamento: "))

idade = int(input("Digite a sua idade: "))

valor_entrada = int(input("Digite o valor da entrada: "))


prestacao_mensal = (valor_imovel - valor_entrada) / (prazo_financeamento * 12)


print("Valor da prestação mensal: R$", prestacao_mensal)

if prestacao_mensal > salario * 0.3:
    print("O financiamento foi aprovado.")
else:
    print("O financiamento foi negado.")

    if prazo_financeamento > 30 or valor_entrada < valor_imovel * 0.10:
        print("O financiamento não foi aprovado. O prazo de financiamento é superior a 30 anos ou a entrada é inferior a 10% do valor do imóvel.")
    else: 
        print("O financiamento foi aprovado.")










