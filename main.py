from database.banco_dados import BancoDeDados 
from services.balanca import Balanca               ##Importação das classes e os metodos de inserções no banco
from app import AplicacaoPesagem

##Configuração de conexão do Banco de Dados Mysql encapsulada da aba banco_dados.py
banco_dados = BancoDeDados(host="localhost", user="root", password="Admin123*", database="pesagem_db")

##Configuração da porta que vai receber a string de "peso"
balanca = Balanca(porta_serial="COM10")

##Inicializa o programa
app = AplicacaoPesagem(banco_dados, balanca) 

##Dados do Veículo
placa = input("Digite a placa do veículo: ")
modelo = input("Digite o modelo do veículo: ")
tipo = input("Digite o tipo do veículo: ")

##Realiza a pesagem
app.realizar_pesagem(placa, modelo, tipo)

##Finaliza o programa
app.finalizar()