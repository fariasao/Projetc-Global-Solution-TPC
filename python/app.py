from functions_app import login, cadastrar_empresa
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
print("1 - Usuário DEMO")
print()
login_dados = input("Digite a opção desejada: ")
print()

while True:
    if login_dados == '1':  
        login("agrotech", "123", "PR")
        ID = 1
        mostrar_menu()

    else:
        print("Opção inválida. Tente novamente.")
        break