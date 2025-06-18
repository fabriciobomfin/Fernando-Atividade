"""
Nome do arquivo: funcionario.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Sensores:
    def __init__(self, id_sensores, temperatura, luminosidade, gas, presenca):
        self.id_sensores = id_sensores
        self.temperatura = temperatura
        self.luminosidade = luminosidade
        self.gas = gas
        self.presenca = presenca
        self.caminho_arquivo = "PROJETO-IOT/data/sensores.txt"

    def __str__(self):
        return (f"ID: {self.id_sensores}, Temperatura: {self.temperatura}, "
                f"Luminosidade: {self.luminosidade}, Gás: {self.gas}, Presença: {self.presenca}")
    
    def to_line(self):
        return (f"{self.id_sensores},{self.temperatura},{self.luminosidade},"
                f"{self.gas},{self.presenca}\n")
    
    # CRUD
    
    # Create
    def inserir_sensor(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    # Read
    def buscar_sensor(self, id_sensores):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_sensores},"):
                    return linha.strip()
        return None
