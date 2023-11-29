from modelos.crudgenerico import CRUDGenerico

banco = CRUDGenerico(
        banco_dados='elogie_aqui.db',
        usuario='admin',
        senha='admin'
    )

banco.inserir(
    tabela="usuarios",
    colunas=("nome","cpf","email","telefone","data_cadastro"),
    valores=("lucads","171.999.000-98","lucasinteligente@gmail.com","(31)988409320","19/11/2023")
)
   