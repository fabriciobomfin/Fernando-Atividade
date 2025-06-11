"""
Nome do arquivo: manutencao.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Manutencao:
    def __init__(self, id_manutencao, data_ingresso, data_saida, id_caminhao, id_funcionario, servico, id_produtos):
        self.id_manutencao = id_manutencao
        self.data_ingresso = data_ingresso
        self.data_saida = data_saida
        self.caminhao = id_caminhao
        self.mecanico = id_funcionario
        self.servico = servico
        self.pecas = id_produtos
        self.caminho_arquivo = "PROJETO-IOT/data/manutencao.txt"
    
    def __str__(self):
        return (f"ID: {self.id_manutencao}, Data de Ingresso: {self.data_ingresso}, "
                f"Data de Saída: {self.data_saida}, Caminhão: {self.caminhao}, "
                f"Mecânico: {self.mecanico}, Serviço: {self.servico}, Peças: {self.pecas}")
    
    def to_line(self):
        return (f"{self.id_manutencao},{self.data_ingresso},{self.data_saida},"
                f"{self.caminhao},{self.mecanico},{self.servico},{self.pecas}\n")
    
    # CRUD

    # Create
    def inserir_manutencao(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    # Read
    def buscar_manutencao(self, id_manutencao):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_manutencao},"):
                    return linha.strip()
        return None
    
    # Update
    def atualizar_manutencao(self, id_manutencao):
        manutencoes = self.listar_manutencoes()
        with open(self.caminho_arquivo, "w") as arquivo:
            for manutencao in manutencoes:
                if manutencao.startswith(f"{id_manutencao},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(manutencao)
    
    # Delete
    def excluir_manutencao(self, id_manutencao):
        manutencoes = self.listar_manutencoes()
        with open(self.caminho_arquivo, "w") as arquivo:
            for manutencao in manutencoes:
                if not manutencao.startswith(f"{id_manutencao},"):
                    arquivo.write(manutencao)

