##Define a classe Veiculo, que representa um veículo com atributos placa, modelo e tipo
class Veiculo:
    ##O método __init__ é o construtor da classe, chamado automaticamente quando uma instância de Veiculo é criada
    def __init__(self, placa, modelo, tipo):
        ##Atribui os valores passados para os parâmetros aos atributos da instância (objeto) da classe
        self.placa = placa  # Atributo placa do veículo
        self.modelo = modelo  # Atributo modelo do veículo
        self.tipo = tipo  # Atributo tipo do veículo (por exemplo, carro, caminhão, etc.)

    ##Método para salvar os dados do veículo no banco de dados
    def salvar_veiculo(self, banco_dados):
        ##Define o comando SQL para inserir os dados do veículo na tabela "veiculos"
        comando = "INSERT INTO veiculos (placa, modelo, tipo) VALUES (%s, %s, %s)"
        
        ##Cria uma tupla com os dados do veículo que serão inseridos na tabela
        dados = (self.placa, self.modelo, self.tipo)

        ##Chama o método 'executar_comando' do objeto banco_dados, passando o comando SQL e os dados
        banco_dados.executar_comando(comando, dados)
        