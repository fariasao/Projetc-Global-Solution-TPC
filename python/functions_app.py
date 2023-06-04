produtores = [
    {
    "codigoProdutor": 1,
    "nome": "Agrotech",
    "tipo": "Pessoa Juridica",
    "areaPlantio": 1000,
    "nomeFantasia": "Agrotech Enterprise",
    "email": "contato@agrotech.com.br",
    "telefone": "11 99999-9999"
    },
    {
    "codigoProdutor": 2,
    "nome": "Fazenda Feliz",
    "tipo": "Pessoa Juridica",
    "areaPlantio": 500,
    "nomeFantasia": "Fazenda Feliz",
    "email": "contato@fazendafeliz.com.br",
    "telefone": "21 88888-8888"
    },
    {
    "codigoProdutor": 3,
    "nome": "Sítio Sol Nascente",
    "tipo": "Pessoa Física",
    "areaPlantio": 150,
    "nomeFantasia": "",
    "email": "contato@sitionsolnascente.com.br",
    "telefone": "31 33333-3333"
    },
    {
    "codigoProdutor": 4,
    "nome": "Fazenda São João",
    "tipo": "Pessoa Jurídica",
    "areaPlantio": 800,
    "nomeFantasia": "São João",
    "email": "contato@fazendasaonjoao.com.br",
    "telefone": "81 44444-4444"
    },
    {
    "codigoProdutor": 5,
    "nome": "Agricultura Orgânica Ltda.",
    "tipo": "Pessoa Jurídica",
    "areaPlantio": 300,
    "nomeFantasia": "Orgânica",
    "email": "contato@agriculturaorganica.com.br",
    "telefone": "21 55555-5555"
    }


]
empresas = []
servicos = []
instituicoes = []
projetos = []

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
    
    return None


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

    while True:
        servico = input("Digite o nome do produto (ou 'sair' para encerrar): ")

        if servico.lower() == 'sair': # verifica se o usuário digitou 'sair'
            break # encerra o loop
        
        descricao = input("Digite a descricao do serviço: ")
    
        # cria um dicionário com as informações do produto e adiciona na lista
        servicos.append({'Nome': servico, 'Descrição': descricao})
    
    # exibe a lista de produtos cadastrados
    print("\nServiços cadastrados:")
    for servico in servicos:
        print(servico)

def visualizar_empresa():
    for servico in servicos:
        print("=======================================================")
        print("ID:", servico["codigoEmpresa"], "Serviço:", servico["nome"])
        print()


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
        "codigoinstituicao": codigoinstituicao,
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
    
        # cria um dicionário com as informações do produto e adiciona na lista
        projetos.append({'Nome': projeto, 'Descrição': descricao})
    
    # exibe a lista de produtos cadastrados
    print("\nProjetos cadastrados:")
    for projeto in projetos:
        print(projeto)


def visualizar_instituicao():
    for instituicao in instituicoes:
        print("=======================================================")
        print("ID:", instituicao["codigoinstituicao"], "Nome:", instituicao["nome"])
        print()


def login(usuario, senha, modalidade):
    users = [
        {'usuario': 'agrotech', 'senha': '123', 'tipo': 'PR'},
        {'usuario': 'produtor', 'senha': '123', 'tipo': 'ER'},
        {'usuario': 'instituicao', 'senha': '123', 'tipo': 'IP'}
    ]
    
    for user in users:
        if user['usuario'] == usuario and user['senha'] == senha and user['tipo'] == modalidade:
            if modalidade == 'PR':
                # Rotina de administrador
                print('Bem-vindo, Logado como Produtor Rural!')
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