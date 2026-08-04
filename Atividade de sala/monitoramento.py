print("===================================")
print("  Monitoramento de Dispositivos    ")
print("===================================")

online = 0
offline = 0
qtd_dispositivos = 0
dispositivos = []
ip = []
status = []

while True:

    print("\n=")
    print("     MENU     ")
    print("=")
    print("  1 para - Cadastrar Dispositivo")
    print("=")
    print("  2 para - Listar Dispositivos")
    print("=")
    print("  3 para - Consultar Dispositivo pelo nome")
    print("=")
    print("  4 para - Sair")
    print("=")

    opcao = int(input("\nDigite a opção desejada: "))

    print("=")
    
    if opcao == 1:
    
        dispositivos.append(str(input("\nDigite o nome do dispositivo: ")))
        qtd_dispositivos += 1
        

        ip.append(int(input("\nDigite o IP do dispositivo: ")))

        status.append(str(input("\nDigite o status do dispositivo / on para Online e off para Offline: ")))
        if status == "on":
            online += 1
        elif status == "off":    
            offline += 1
        print("\n CADASTRADO COM SUCESSO!")
        print("=====================================")

    elif opcao == 2:
        if len (dispositivos) == 0:
            print("\nNenhum dispositivo cadastrado!")
            print("=====================================")

        else:
            print(f" Dispositivos Cadastrados: {dispositivos} Quantidade: {qtd_dispositivos} ")
            print(f" Dispositivos Online: {online} ")
            print(f" Dispositivos Offline: {offline} ")
            print("=====================================")

    elif opcao == 3:
        procurar_dispositivo = str(input(" Digite o nome do dispositivo que deseja encontrar: "))
        if procurar_dispositivo in dispositivos:
            print(f" O Dispositivo foi encontrado, Nome: {procurar_dispositivo}, IP: {ip}, Status: {status}")
            print("=====================================")

        else:
            print("\nDispositivo não encontrado!")
            print("=====================================")


    elif opcao == 4:
        print("\nSaindo do programa...")
        print("=====================================")
        break
    else:
        print("\nOpção inválida, tente novamente!")
        print("=====================================")