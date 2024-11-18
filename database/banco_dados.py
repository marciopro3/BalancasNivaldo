import mysql.connector  ##Importa a biblioteca mysql.connector para conectar e interagir com o banco de dados MySQL

##Define a classe BancoDeDados, responsável pela conexão e manipulação do banco de dados
class BancoDeDados:
    ##O método __init__ é chamado quando uma nova instância de BancoDeDados é criada
    def __init__(self, host, user, password, database):
        ##Estabelece uma conexão com o banco de dados usando as credenciais fornecidas (host, user, password, database)
        self.conexao = mysql.connector.connect(
            host=host,       
            user=user,      
            password=password,  
            database=database  
        )
        ##Cria um cursor para executar comandos SQL no banco de dados
        self.cursor = self.conexao.cursor()

    ##Método para executar um comando SQL (como INSERT, UPDATE, DELETE) no banco de dados
    def executar_comando(self, comando, dados=None):
        ##Executa o comando SQL fornecido
        self.cursor.execute(comando, dados)
        # Faz a confirmação (commit) da transação no banco de dados, garantindo que as mudanças sejam salvas
        self.conexao.commit()

    ##Método para realizar uma consulta SELECT
    def consultar(self, consulta, dados=None):
        ##Executa a consulta SQL fornecida
        self.cursor.execute(consulta, dados)
        ##Retorna todos os resultados da consulta, que são armazenados em uma lista
        return self.cursor.fetchall()

    ##Método para fechar a conexão com o banco de dados de forma segura
    def fechar_conexao(self):
        ##Fecha o cursor, liberando os recursos associados a ele
        self.cursor.close()
        ##Fecha a conexão com o banco de dados
        self.conexao.close()