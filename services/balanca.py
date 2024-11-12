import serial
import time

class Balanca:
    def __init__(self, porta_serial, baudrate=9600):
        self.porta_serial = porta_serial
        self.baudrate = baudrate
        self.conexao = serial.Serial(self.porta_serial, self.baudrate)
        time.sleep(2)  # Aguarda conexão

    def capturar_peso(self):
        if self.conexao.isOpen():
            peso_bruto = float(self.conexao.readline().decode('utf-8').strip())
            peso_tara = float(self.conexao.readline().decode('utf-8').strip())
            return peso_bruto, peso_tara
        else:
            print("Erro: Conexão serial não está aberta.")
            return None, None

    def fechar_conexao(self):
        self.conexao.close()