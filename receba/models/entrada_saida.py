"""
Nome do arquivo: entrada_saida.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Entrada_Saida:
    def __init__(self, id_entrada_saida, data_entrada, data_saida, hora_entrada, hora_saida, destino, roteiro, peso, km_saida, km_chegada, id_caminhao, id_funcionario):
        self.id_entrada_saida = id_entrada_saida
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.destino = destino
        self.roteiro = roteiro
        self.peso = peso
        self.km_saida = km_saida
        self.km_chegada = km_chegada
        self.id_caminhao = id_caminhao
        self.motorista = id_funcionario
        self.caminho_arquivo = "PROJETO-IOT/data/entrada_saida.txt"

    def __str__(self):
        return (f"ID: {self.id_entrada_saida}, Data Entrada: {self.data_entrada}, Data Saída: {self.data_saida}, "
                f"Hora Entrada: {self.hora_entrada}, Hora Saída: {self.hora_saida}, Destino: {self.destino}, "
                f"Roteiro: {self.roteiro}, Peso: {self.peso}, KM Saída: {self.km_saida}, "
                f"KM Chegada: {self.km_chegada}, ID Caminhão: {self.id_caminhao}, ID Funcionário: {self.motorista}")
    
    def to_line(self):
        return (f"{self.id_entrada_saida},{self.data_entrada},{self.data_saida},{self.hora_entrada},"
                f"{self.hora_saida},{self.destino},{self.roteiro},{self.peso},{self.km_saida},"
                f"{self.km_chegada},{self.id_caminhao},{self.motorista}\n")
    
    # CRUD

    # Create
    def inserir_entrada_saida(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    # Read
    def buscar_entrada_saida(self, id_entrada_saida):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_entrada_saida},"):
                    return linha.strip()
        return None
        
    # Update
    def atualizar_entrada_saida(self, id_entrada_saida):
        entradas_saidas = self.listar_entradas_saidas()
        with open(self.caminho_arquivo, "w") as arquivo:
            for entrada_saida in entradas_saidas:
                if entrada_saida.startswith(f"{id_entrada_saida},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(entrada_saida)

    # Delete
    def excluir_entrada_saida(self, id_entrada_saida):
        entradas_saidas = self.listar_entradas_saidas()
        with open(self.caminho_arquivo, "w") as arquivo:
            for entrada_saida in entradas_saidas:
                if not entrada_saida.startswith(f"{id_entrada_saida},"):
                    arquivo.write(entrada_saida)
