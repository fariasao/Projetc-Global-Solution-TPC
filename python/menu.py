from functions_app import consultar_perfil, buscar_produtor_por_id
def mostrar_menu():
    while True:
        print("Escolha uma opção:")
        print("1. Ver meinhas Informações")
        print("2. Listar Produtores")
        print("3. Listar Empresas")
        print("4. Listar Instituições")
        print("5. Listar Projetos")
        print("6. Sair")
        
        opcao = input("Opção escolhida: ")
        
        if opcao == "1":
            print("====================================")
            consultar_perfil(1)
            print("====================================")
            print()
            
        elif opcao == "2":
            print("====================================")
            num = int(input("Digite o ID do produtor: "))
            buscar_produtor_por_id(num)
            print("====================================")
            
        elif opcao == "3":
            print("Opção 3 selecionada.")
            
        elif opcao == "6":
            print("Programa encerrado.")
            break
            
        else:
            print("Opção inválida. Tente novamente.\n")


