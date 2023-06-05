from functions_app import consultar_perfil, buscar_produtor_por_id, remover_produtor, visualizar_produtores, editar_produtor, visualizar_empresas
def mostrar_menu():
    while True:
        print("Escolha uma opção:")
        print("1. Ver minhas Informações")
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
            i = input("Deseja editar o seu perfil? \nDigite 1 para SIM \nDigite 0 para NAO \nOpcao desejada: ")
            if i == "1":
                print("====================================")
                print("Informe qual informacao deseja alterar:")
                print("1. Nome")
                print("2. Email")
                print("3. Telefone")
                print("4. Nome Fantasia")
                print("5. Area de Plantio")
                y = input("Opcao desejada: ")
                match y:
                    case "1":
                        alt = input("Digite o novo nome: ")
                        editar_produtor(1, 'nome', alt)
                    case "2":
                        alt = input("Digite o novo email: ")
                        editar_produtor(1, 'email', alt)
                    case "3":
                        alt = input("Digite o novo telefone: ")
                        editar_produtor(1, 'telefone', alt)
                    case "4":
                        alt = input("Digite o novo nome fantasia: ")
                        editar_produtor(1, 'nome_fantasia', alt)
                    case "5":
                        alt = int(input("Digite a nova area de plantio: "))
                        editar_produtor(1, 'area_plantio', alt)
                print("====================================")
                print(" ")
            
        elif opcao == "2":
            visualizar_produtores()
            op_edit = input("Deseja ver o perfil completo de algum produtor? \nDigite 1 para SIM \nDigite 0 para NAO \nOpcao desejada:  ")
            if op_edit == "1":
                num = int(input("Digite o ID do produtor: "))
                buscar_produtor_por_id(num)
                print("====================================")
                i = input("Deseja remover ou editar o produtor? \nDigite 1 para remover \nDigite 2 para Editar \nOpcao desejada: ")
                if i == "1":
                    remover_produtor(num)
                    print("Produtor removido com sucesso!")
                elif i == "2":
                    editar_produtor(num)

        elif opcao == "3":
            visualizar_empresas()
            
        elif opcao == "6":
            print("Programa encerrado.")
            break
            
        else:
            print("Opção inválida. Tente novamente.\n")


