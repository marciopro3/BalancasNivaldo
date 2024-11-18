##Importa a biblioteca 'serial'
import serial
##Importa a biblioteca 'time', que permite utilizar funções de tempo, como pausas no código.
import time

##Define a classe Balanca, que representa uma balança conectada a uma porta serial.
class Balanca:
    ##O método __init__ é o construtor da classe, chamado automaticamente quando uma instância de Balanca é criada.
    def __init__(self, porta_serial, baudrate=9600):
        ##Atributo porta_serial recebe o nome ou caminho da porta serial onde a balança está conectada.
        self.porta_serial = porta_serial
        
        ##Atributo baudrate recebe a taxa de transmissão de dados para a porta serial, o valor padrão é 9600.
        self.baudrate = baudrate
        
        ##Estabelece a conexão com a porta serial, criando um objeto de conexão para ler e escrever dados.
        self.conexao = serial.Serial(self.porta_serial, self.baudrate)
        
        ##Aguarda 2 segundos para garantir que a conexão com a balança seja estabelecida corretamente.
        time.sleep(2)

    ##Método para capturar o peso bruto e o peso tara da balança.
    def capturar_peso(self):
        ##Verifica se a conexão com a balança está aberta (ou seja, a porta serial está ativa).
        if self.conexao.isOpen():
            ##Lê uma linha de dados da balança (peso bruto), decodifica e remove espaços em branco.
            peso_bruto = float(self.conexao.readline().decode('utf-8').strip())
            
            ##Lê outra linha de dados (peso tara), decodifica e remove espaços em branco.
            peso_tara = float(self.conexao.readline().decode('utf-8').strip())
            
            ##Retorna os valores de peso bruto e peso tara capturados da balança.
            return peso_bruto, peso_tara
        else:
            ##Caso a conexão com a balança não esteja aberta, exibe um erro.
            print("Erro: Conexão serial não está aberta.")
            
            ##Retorna 'None' para indicar que não foi possível capturar os pesos.
            return None, None

    ##Método para fechar a conexão com a balança quando não for mais necessária.
    def fechar_conexao(self):
        ##Fecha a conexão com a porta serial.
        self.conexao.close()