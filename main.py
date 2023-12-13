from modelos.crudgenerico import CRUDGenerico

banco = CRUDGenerico(
        banco_dados='elogie_aqui.db',
        usuario='admin',
        senha='admin'
        
    )

print("""
    1 - Novo Registro
    2 - Consultar Registro
    3 - Alterar Registro
    4 - Apagar Registro
""")
opcao = input("Informe a opção desejada: ")

match opcao:
    case '1':
        tabela = input("Nome da tabela: ")
        nome = input("Digite o nome completo: ")
        cpf = input("Digite o cpf: ")
        email = input("Digite o email: ")
        telefone = input("Digite o Telefone: ")
        data_cadastro = input("Digite a data: ")
        banco.inserir(
            tabela=tabela,
            colunas=("nome", "cpf", "email", "telefone", "data_cadastro"),
            valores=(nome, cpf, email, telefone, data_cadastro)
        )

    case '2':
        tabela = input("Nome da tabela: ")
        id = int(input("Digite o ID: "))
        consultar = banco.consultar(
            tabela=tabela,
            id=id
        )
        print(consultar)

    case '3':
        tabela = input("Nome da tabela: ")
        id = int(input("Digite o ID: "))
        coluna = input("Digite a coluna: ")
        novo_valor = input("Digite o novo valor: ")

        banco.alterar(
            tabela=tabela,
            id=id,
            coluna=coluna,
            novo_valor=novo_valor
        )