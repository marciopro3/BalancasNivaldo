import serial ##Necessário para conexão serial
import time ##Usado para aguardar a porta serial ativa
import random ##Gerador de número aleatório, coloquei entre 1000 e 3000

def enviar_peso_aleatorio(porta="COM5", baudrate=9600):
    try:
        conexao = serial.Serial(porta, baudrate)
        time.sleep(2)  ##Aguardo inicial da porta COM5, deixei a valocidade 9600, 8 bits, paridade N e StopBit 1 no Virtual Serial Ports
        
        while True:
            peso = random.randint(1000, 3000)  ##Gera um peso aleatório
            conexao.write(f"{peso}\n".encode())  ##Envia o peso em uma nova linha
            print(f"Peso '{peso}' emulado na {porta}.")
            time.sleep(1)  ##Aguarda 1 segundo, depois mostra outro peso

    except serial.SerialException as e:
        print(f"Erro ao abrir a porta {porta}: {e}") ##Se não encontrar a porta COM5 em 2 segundos mostra esse print de erro
    except KeyboardInterrupt:
        print("Interrompido pelo usuário.") ##Se apertar CTRL+C a conexão é interrompida
    finally:
        if conexao.is_open:
            conexao.close()
            print("Conexão serial fechada.") ##Fecha a conexão pra liberar a porta COM5 emulada no Virtual Serial

##Chama a função para enviar o peso aleatório
enviar_peso_aleatorio()