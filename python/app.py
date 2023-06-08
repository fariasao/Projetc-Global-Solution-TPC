from functions_app import login, cadastrar_empresa, cadastrar
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
print("2 - Cadastrar novo usuário")
print()
login_dados = input("Digite a opção desejada: ")
print()

while True:
    if login_dados == '1':  
        login("agrotech", "123", "PR")
        ID = 1
        mostrar_menu()
        break

    elif login_dados == '2':
        cadastrar()
        if login() == True:
            cadastrar_empresa()
            mostrar_menu()
        

    else:
        print("Opção inválida. Tente novamente.")
        login_dados = input("Digite a opção desejada: ")
        