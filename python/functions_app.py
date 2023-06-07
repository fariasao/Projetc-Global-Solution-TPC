from arrays import produtores, empresas, servicos, instituicoes, projetos, users

def cadastrar_produtor():
    nome = input("Digite o nome do Produtor: ")
    tipo = input("Digite o tipo do Produtor: ")
    areaPlantio = float(input("Digite a área de Plantio do Produtor: "))
    nomeFantasia = input("Digite o nome Fantasia do Produtor: ")
    email = input("Digite o email do Produtor: ")
    telefone = input("Digite o telefone do Produtor: ")

    codigoProdutor = len(produtores) + 1 # Gera um código automático baseado na posição no array

    produtor = {
        "codigoProdutor": codigoProdutor,
        "nome": nome,
        "tipo": tipo,
        "areaPlantio": areaPlantio,
        "nomeFantasia": nomeFantasia,
        "email": email,
        "telefone": telefone
    }

    produtores.append(produtor)


def visualizar_produtores():
    for produtor in produtores:
        print("=======================================================")
        print("ID:", produtor["codigoProdutor"], "Nome:", produtor["nome"])
        print()

def buscar_produtor_por_id(id):
    for produtor in produtores:
        if produtor["codigoProdutor"] == id:
            print("=======================================================")
            print("                   Resultado da busca:")
            print("=======================================================")
            print("Nome:", produtor["nome"])
            print("Tipo:", produtor["tipo"])
            print("Area Plantio:", produtor["areaPlantio"])
            print("Nome Fantasia:", produtor["nomeFantasia"])
            print("Email:", produtor["email"])
            print("Telefone:", produtor["telefone"])
            print("=======================================================")
            print()
            return produtor
    print("Produtor não encontrado.")
    return None
    

def remover_produtor(codigoProdutor):
    for i in range(len(produtores)):
        if produtores[i]['codigoProdutor'] == codigoProdutor:
            produtores.pop(i)
            return True
    return False

def cadastrar_empresa():
    nome = input("Digite o nome da empresa: ")
    tipo = input("Digite o tipo da empresa: ")
    nomeFantasia = input("Digite o nome fantasia da empresa: ")
    email = input("Digite o e-mail da empresa: ")
    telefone = input("Digite o telefone da empresa: ")
    endereco = input("Digite o endereço da empresa: ")
    representante = input("Digite o nome do representante da empresa: ")
    codigoEmpresa = len(empresas) + 1 # Gera um código automático baseado na posição no array

    empresa = {
        "codigoEmpresa": codigoEmpresa,
        "nome": nome,
        "tipo": tipo,
        "nomeFantasia": nomeFantasia,
        "representante": representante,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }
    empresas.append(empresa)

    print("Empresa cadastrada com sucesso!")
    i = input("Você gostaria de cadastrar um serviço? \nDigite 1 para sim \nDigite 2 para não.")

    if i == '1':
        while True:
            servico = input("Digite o nome do Serviço (ou 'sair' para encerrar): ")

            if servico.lower() == 'sair': 
                break # encerra o loop
        
            descricao = input("Digite a descricao do serviço: ")
    
            
            servicos.append({'codigoEmpresa': codigoEmpresa, 'Nome':servico, 'Descrição': descricao})
    # exibe a lista de produtos cadastrados
    #print("\nServiços cadastrados:")
    #for servico in servicos:
        #print(servico)
     

    

def visualizar_empresas():
    for empresa in empresas:
        print("=======================================================")
        print("ID:", empresa["codigoEmpresa"], "Empresa:", empresa["nome"])
        print("=======================================================")

def buscar_empresa_por_id(id):
    for empresa in empresas:
        if empresa["codigoEmpresa"] == id:
            print("=======================================================")
            print("                   Resultado da busca:")
            print("=======================================================")
            print("Nome:", empresa["nome"])
            print("Tipo:", empresa["tipo"])
            print("Nome Fantasia:", empresa["nomeFantasia"])
            print("Email:", empresa["email"])
            print("Telefone:", empresa["telefone"])
            print("=======================================================")
            print()
            i = input("Deseja ver a lista de servicos desta empresa? \nDigite 1 para SIM \nDigite 0 para NAO \nOpcao desejada:  ")
            if i == "1":
                print("=======================================================")
                print("                        SERVICOS:")
                print("=======================================================")
                visualizar_servicos(id)
            return empresa
        
    print("Nenhuma empresa encontrada!")
    return None
    

def visualizar_servicos(id):
    for servico in servicos:
        if servico["codigoEmpresa"] == id:
            print("=======================================================")
            print("Nome:", servico["nome"], "\nDescrição:", servico["descricao"])
            print("=======================================================")
            return servico
        
        print("Nenhum servico encontrado!")
        return None

def cadastrar_instituicao():
    nome = input("Digite o nome da instituicao: ")
    tipo = input("Digite o tipo da instituicao: ")
    nomeFantasia = input("Digite o nome fantasia da instituicao: ")
    email = input("Digite o e-mail da instituicao: ")
    telefone = input("Digite o telefone da instituicao: ")
    endereco = input("Digite o endereço da instituicao: ")
    representante = input("Digite o nome do representante da instituicao: ")
    codigoinstituicao = len(instituicoes) + 1 # Gera um código automático baseado na posição no array

    instituicao = {
        "codigoInstituicao": codigoinstituicao,
        "nome": nome,
        "tipo": tipo,
        "nomeFantasia": nomeFantasia,
        "representante": representante,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }
    instituicoes.append(instituicao)

     
    while True:
        projeto = input("Digite o nome do projeto (ou 'sair' para encerrar): ")

        if projeto.lower() == 'sair': # verifica se o usuário digitou 'sair'
            break # encerra o loop
        
        descricao = input("Digite a descricao do projeto: ")
    
        
        projetos.append({'Nome': projeto, 'Descrição': descricao})
    
    # exibe a lista de produtos cadastrados
    print("\nProjetos cadastrados:")
    for projeto in projetos:
        print(projeto)


def visualizar_instituicao():
    for instituicao in instituicoes:
        print("=======================================================")
        print("ID:", instituicao["codigoInstituicao"], "Nome:", instituicao["nome"])
        print("=======================================================")

def visualizar_projetos():
    print("=======================================================")
    print("                        PROJETOS:")
    print("=======================================================")
    for projeto in projetos:
        print("=======================================================")
        print("ID:", projeto["codigoProjeto"], "Nome:", projeto["nome"])
        print("=======================================================")
    i = input("Deseja ver mais informacoes sobre algum projeto? \nDigite 1 para SIM \nDigite 0 para NAO \nOpcao desejada:  ")
    if i == "1":
        id = int(input("Digite o ID do projeto: "))
        visualizar_projetos_id(id)



def visualizar_projetos_id(id):
    for projeto in projetos:
        if projeto["codigoProjeto"] == id:
            print("=======================================================")
            print("Nome:", projeto["nome"], "\nDescrição:", projeto["descricao"], "\ninstituicao:", projeto["Instituicao"])
            print("=======================================================")
            return projeto
    print("Nenhum servico encontrado!")
    return None
    
def login(usuario, senha, modalidade):
       
    for user in users:
        if user['usuario'] == usuario and user['senha'] == senha and user['tipo'] == modalidade:
            if modalidade == 'PR':
                # Rotina de administrador
                print("======================================")
                print('Bem-vindo, Logado como Produtor Rural!')
                print("======================================")
                print()
                return True
            elif modalidade == 'ER':
                # Rotina do usuário
                print('Bem-vindo, Logado como Empresa de Tecnologia!')
                return True
            elif modalidade == 'IP':
                # Rotina do usuário
                print('Bem-vindo, Logado como Empresa de Instituicao de Pesquisa!')
                return True
    
    print('Login inválido.')
    return False

def consultar_perfil(codigo):
    for produtor in produtores:
        if produtor["codigoProdutor"] == codigo:
            print("Código do Produtor: ", produtor["codigoProdutor"])
            print("Nome: ", produtor["nome"])
            print("Tipo: ", produtor["tipo"])
            print("Área de Plantio: ", produtor["areaPlantio"])
            print("Nome Fantasia: ", produtor["nomeFantasia"])
            print("Email: ", produtor["email"])
            print("Telefone: ", produtor["telefone"])
            return
    print("Produtor não encontrado")

def editar_produtor(codigo, atributo, alteracao):
    for produtor in produtores:
        if produtor['codigoProdutor'] == codigo:
            produtor[atributo] = alteracao
            print(f"{atributo} do produtor ID: {codigo} foi atualizado para {alteracao}.")
            return
    print(f"Não foi encontrado nenhum produtor com o ID {codigo}.")

def cadastrar():
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    tipo = "PR"
    
    novo_usuario = {'usuario': usuario, 'senha': senha, 'tipo': tipo}
    users.append(novo_usuario)
    
    print("Olá ", usuario,", você se cadastrou com sucesso!")
    print("Agora você pode fazer login no sistema!")
    print("======================================")
    print("             LOGIN")
    print("======================================")
    