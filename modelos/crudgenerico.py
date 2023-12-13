import sqlite3 as sql

class CRUDGenerico:
    def __init__(self, banco_dados: str, usuario: str, senha: str) -> None:
        self.banco_dados = banco_dados
        self.usuario     = usuario
        self.senha       = senha

        self.conexao = None
        self.cursor  = None


    # Métodos de conexão
    def logar(self) -> bool:
        USUARIO = 'admin'
        SENHA = 'admin'
        return True if self.usuario == USUARIO and self.senha == SENHA else 'ERRO!!'



    def conectar(self) -> bool:
        if self.logar() == True: #Login sucedido
            self.conexao = sql.connect(self.banco_dados)
            self.cursor = self.conexao.cursor()
            return True
        else:
            return 'Banco de dados não conectado'



    def desconectar(self) -> None:
        if self.conectar() == True: # se estiver conectado
            self.conexao.close()


    # Métodos do CRUD Genérico (manipular banco de dados)]
    def inserir(self, tabela: str, colunas: tuple[str], valores: tuple[any]) -> str: #CREATE
        """
        Esté Método (faz o que?)
        ------

        parametros:
        ---
            tabela(str): nome da tabela que será manipulada
            colunas(tupla[str]): colunas da tabela
            valores(tupla[any]): valores que serão inseridos na tabela
        ----
        retorno:
            None
        """
        if self.conectar() == True: # se estiver conectado
            self.cursor.execute(
                f"INSERT INTO {tabela} {colunas} VALUES {valores}"
            )
            self.conexao.commit()
        else:
            return 'ERRO!! Banco de dados não conectado'



    def consultar(self, tabela: str, id) -> list[tuple[any]]: #READ
        if self.conectar() == True: # se estiver conectado
            dados = self.cursor.execute(
                f"SELECT * FROM {tabela} WHERE id={id}"
            ).fetchall()
            return dados




    def alterar(self, tabela: str, id: int, coluna: str, novo_valor: str) -> list[tuple[any]]: #UPDATE
        backup = self.consultar(tabela=tabela, id=id)
        if self.conectar() == True:
            self.cursor.execute(
                f"UPDATE {tabela} SET {coluna} VALUES {novo_valor} WHERE id={id}"
            )
            self.conexao.commit()
            registro_atualizado = self.consultar(tabela=tabela, id=id)
            return backup, registro_atualizado


    def apagar(self, tabela: str, id: int) -> list[tuple[any]]: #DELETE
        backup = self.consultar(tabela=tabela, id=id)
        if self.conectar() == True:
            self.cursor.execute(
                f"DELETE FROM {tabela} WHERE id = {id}"
            )
            self.conexao.commit()
            return backup

            
            


    
    


# Cláusulas de guarda (dunder objects)
if __name__ == "__main__": # Se o nome do arquivo é igual a ele mesmo
    banco = CRUDGenerico(
        banco_dados='elogie_aqui.db',
        usuario='admin',
        senha='admin'
    )

    banco.inserir(
        tabela='usuarios',
        colunas=('nome',),
        valores=('Lucas',)
    )


