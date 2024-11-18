from models.veiculo import Veiculo 
from models.pesagem import Pesagem                         ##Importação das classes e os metodos de inserções no banco
from database.banco_dados import BancoDeDados 
from services.balanca import Balanca 

class AplicacaoPesagem:                                    ##Define a classe AplicacaoPesagem, que gerencia o processo de pesagem e interação com o banco de dados e a balança                           
    def __init__(self, banco_dados, balanca):              ##Inicializa a classe com uma instância de BancoDeDados e Balanca
        self.banco_dados = banco_dados
        self.balanca = balanca
    ##Método para realizar a pesagem de um veículo
    def realizar_pesagem(self, placa, modelo, tipo):
        ##Cria uma instância de Veiculo com os dados fornecidos (placa, modelo e tipo)
        veiculo = Veiculo(placa, modelo, tipo)
        
        ##Chama o método salvar_veiculo para armazenar os dados do veículo no banco de dados
        veiculo.salvar_veiculo(self.banco_dados)

        ##Captura o peso bruto e o peso tara da balança
        peso_bruto, peso_tara = self.balanca.capturar_peso()

        ##Verifica se os pesos foram capturados corretamente (não são None)
        if peso_bruto is not None and peso_tara is not None:
            ##Cria uma instância de Pesagem com o veículo e os pesos capturados
            pesagem = Pesagem(veiculo, peso_bruto, peso_tara)

            ##Salva os dados da pesagem no banco de dados
            pesagem.salvar_pesagem(self.banco_dados)

            ##Imprime uma mensagem de sucesso, mostrando o peso líquido calculado
            print(f"Pesagem salva com sucesso! Peso líquido: {pesagem.peso_liquido} kg")
        else:
            ##Imprime uma mensagem de erro caso a captura dos pesos falhe
            print("Falha ao capturar peso.")

    ##Método para finalizar a aplicação, fechando as conexões com o banco de dados e a balança
    def finalizar(self):
        ##Fecha a conexão com o banco de dados
        self.banco_dados.fechar_conexao()

        ##Fecha a conexão com a balança
        self.balanca.fechar_conexao()