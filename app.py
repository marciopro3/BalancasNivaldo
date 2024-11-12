from models.veiculo import Veiculo
from models.pesagem import Pesagem
from database.banco_dados import BancoDeDados
from services.balanca import Balanca

class AplicacaoPesagem:
    def __init__(self, banco_dados, balanca):
        self.banco_dados = banco_dados
        self.balanca = balanca

    def realizar_pesagem(self, placa, modelo, tipo):
        veiculo = Veiculo(placa, modelo, tipo)
        veiculo.salvar_veiculo(self.banco_dados)

        peso_bruto, peso_tara = self.balanca.capturar_peso()
        if peso_bruto is not None and peso_tara is not None:
            pesagem = Pesagem(veiculo, peso_bruto, peso_tara)
            pesagem.salvar_pesagem(self.banco_dados)
            print(f"Pesagem salva com sucesso! Peso líquido: {pesagem.peso_liquido} kg")
        else:
            print("Falha ao capturar peso.")

    def finalizar(self):
        self.banco_dados.fechar_conexao()
        self.balanca.fechar_conexao()