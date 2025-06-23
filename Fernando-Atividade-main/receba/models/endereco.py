"""
Nome do arquivo: endereco.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Endereco:
    def __init__(self, id_endereco, logradouro, numero, bairro, cep, cidade, uf, complemento):
        self.id_endereco = id_endereco
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.complemento = complemento
        self.caminho_arquivo = "PROJETO-IOT/data/endereco.txt"

    def __str__(self):
        return f"ID: {self.id_endereco}, Logradouro: {self.logradouro}, Número: {self.numero}, Bairro: {self.bairro}, CEP: {self.cep}, Cidade: {self.cidade}, UF: {self.uf}, Complemento: {self.complemento}"

    def to_line(self):
        return f"{self.id_endereco},{self.logradouro},{self.numero},{self.bairro},{self.cep},{self.cidade},{self.uf},{self.complemento}\n"    
    
    #CRUD

    #Create
    def inserir_endereco(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())
    
    #Read
    def buscar_endereco(self, id_endereco):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_endereco},"):
                    return linha.strip()
        return None
    
    #Update
    def atualizar_endereco(self, id_endereco):
        enderecos = self.listar_enderecos()
        with open(self.caminho_arquivo, "w") as arquivo:
            for endereco in enderecos:
                if endereco.startswith(f"{id_endereco},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(endereco)
    
    #Delete
    def excluir_endereco(self, id_endereco):
        enderecos = self.listar_enderecos()
        with open(self.caminho_arquivo, "w") as arquivo:
            for endereco in enderecos:
                if not endereco.startswith(f"{id_endereco},"):
                    arquivo.write(endereco)


    