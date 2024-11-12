import mysql.connector

class BancoDeDados:
    def __init__(self, host, user, password, database):
        self.conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexao.cursor()

    def executar_comando(self, comando, dados=None):
        self.cursor.execute(comando, dados)
        self.conexao.commit()
        
    def consultar(self, consulta, dados=None):
        self.cursor.execute(consulta, dados)
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()