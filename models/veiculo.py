class Veiculo:
    def __init__(self, placa, modelo, tipo):
        self.placa = placa
        self.modelo = modelo
        self.tipo = tipo

    def salvar_veiculo(self, banco_dados):
        comando = "INSERT INTO veiculos (placa, modelo, tipo) VALUES (%s, %s, %s)"
        dados = (self.placa, self.modelo, self.tipo)
        banco_dados.executar_comando(comando, dados)