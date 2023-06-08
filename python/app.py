from functions_app import login, cadastrar_empresa, cadastrar, cadastrar_instituicao, cadastrar_produtor
from menu import mostrar_menu

# login
print("###########################################################################")
print("         ##      ####    #####     ####    ##  ##   ######   ######")   
print("        ####    ##  ##   ##  ##   ##  ##   ### ##   ##         ##")  
print("       ##  ##   ##       ##  ##   ##  ##   ######   ##         ##") 
print("       ######   ## ###   #####    ##  ##   ######   ####       ##") 
print("       ##  ##   ##  ##   ####     ##  ##   ## ###   ##         ##") 
print("       ##  ##   ##  ##   ## ##    ##  ##   ##  ##   ##         ##") 
print("       ##  ##    ####    ##  ##    ####    ##  ##   ######     ##") 
print("###########################################################################")

print("Bem-vindo ao AgroNet! Escolha com qual usuário deseja logar:")
print("1 - Usuário DEMO")
print("2 - Cadastrar nova empresa")
print("3 - Cadastrar nova instituição")
print("4 - Cadastrar novo produtor")
print()
login_dados = input("Digite a opção desejada: ")
print()

while True:
    if login_dados == '1':  
        print("========================")
        print("Credenciais de acesso:")
        print("Usuário: agrotech")
        print("Senha: 123")
        print("========================")
        login()
        ID = 1
        mostrar_menu()
        break

    elif login_dados == '2':
        cadastrar()
        if login() == True:
            cadastrar_empresa()
            mostrar_menu()

    elif login_dados == '3':
        cadastrar()
        if login() == True:
            cadastrar_instituicao()
            mostrar_menu()

    elif login_dados == '4':
        cadastrar()
        if login() == True:
            cadastrar_produtor()
            mostrar_menu()

    else:
        print("Opção inválida. Tente novamente.")
        login_dados = input("Digite a opção desejada: ")
        