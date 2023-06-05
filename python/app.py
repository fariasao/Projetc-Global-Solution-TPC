from functions_app import login, consultar_perfil, visualizar_produtores
from menu import mostrar_menu

# login
print("###########################################################################")
print("##  ####     #####   #####     ####    ######   #####     ####    ##  ## ##")
print("## ##  ##   ##       ##  ##   ##  ##     ##     ##       ##  ##   ##  ## ##")
print("## ######   ## ###   #####    ##  ##     ##     ####     ##       ###### ##")
print("## ##  ##   ##  ##   ## ##    ##  ##     ##     ##       ##  ##   ##  ## ##")
print("## ##  ##    ####    ##  ##    ####      ##     #####     ####    ##  ## ##")
print("###########################################################################")

print("Bem-vindo ao AgroTech! Escolha com qual usuário deseja logar:")
print("1 - Produtor Rural")
print("2 - Empresa Rural")
print("3 - Empresa de Instituição de Pesquisa")
login_dados = input("Digite a opção desejada: ")

if login_dados == '1':
    login("agrotech", "123", "PR")
    ID = 1

    mostrar_menu()

    op = input("Selecione uma Opção: ")
    if op == "1":
        consultar_perfil(ID)

    elif op == "2":
        visualizar_produtores()

    elif op == "3":
        print()
    else:
        print("Opção inválida!")




elif login_dados == '2':
    login("produtor", "123", "ER")


elif login_dados == '3':
    login("instituicao", "123", "IP")
    





