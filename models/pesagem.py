class Pesagem:
    def __init__(self, veiculo, peso_bruto, peso_tara):
        self.veiculo = veiculo
        self.peso_bruto = peso_bruto
        self.peso_tara = peso_tara
        self.peso_liquido = None  # O peso_liquido será consultado depois

    def salvar_pesagem(self, banco_dados):
        # A coluna peso_liquido será calculada automaticamente pelo banco de dados
        comando = """
        INSERT INTO pesagens (veiculo_id, peso_bruto, peso_tara)
        VALUES ((SELECT id FROM veiculos WHERE placa = %s), %s, %s)
        """
        dados = (self.veiculo.placa, self.peso_bruto, self.peso_tara)
        banco_dados.executar_comando(comando, dados)

        # Consultar o peso_liquido calculado automaticamente pelo MySQL
        comando_consulta = """
        SELECT peso_liquido 
        FROM pesagens 
        WHERE veiculo_id = (SELECT id FROM veiculos WHERE placa = %s) 
        ORDER BY id DESC LIMIT 1
        """
        banco_dados.cursor.execute(comando_consulta, (self.veiculo.placa,))
        resultado = banco_dados.cursor.fetchone()

        if resultado:
            self.peso_liquido = resultado[0]  # Atribui o valor do peso_liquido