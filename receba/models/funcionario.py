"""
Nome do arquivo: funcionario.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Funcionario:
    def __init__(self, id_funcionario, nome, cpf, cargo, dta_nascimento, id_endereco, id_contato):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.dta_nascimento = dta_nascimento
        self.endereco = id_endereco
        self.contato = id_contato
        self.caminho_arquivo = "PROJETO-IOT/data/funcionario.txt"

def __str__(self):
    return (f"ID: {self.id_funcionario}, Nome: {self.nome}, CPF: {self.cpf}, RG: {self.rg}, "
            f"Cargo: {self.cargo}, Salário: {self.salario}, ID Endereço: {self.id_endereco}, "
            "ID Contato: {self.id_contato}")

def to_line(self):
    return f"{self.id_funcionario},{self.nome},{self.cpf},{self.rg},{self.cargo},{self.salario},{self.id_endereco},{self.id_contato}\n"

# CRUD

# Create
def inserir_funcionario(self):
    with open(self.caminho_arquivo, "a") as arquivo:
        arquivo.write(self.to_line())

# Read
def buscar_funcionario(self, id_funcionario):
    with open(self.caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            if linha.startswith(f"{id_funcionario},"):
                return linha.strip()
    return None

# Update
def atualizar_funcionario(self, id_funcionario):
    funcionarios = self.listar_funcionarios()
    with open(self.caminho_arquivo, "w") as arquivo:
        for funcionario in funcionarios:
            if funcionario.startswith(f"{id_funcionario},"):
                arquivo.write(self.to_line())
            else:
                arquivo.write(funcionario)

# Delete
def excluir_funcionario(self, id_funcionario):
    funcionarios = self.listar_funcionarios()
    with open(self.caminho_arquivo, "w") as arquivo:
        for funcionario in funcionarios:
            if not funcionario.startswith(f"{id_funcionario},"):
                arquivo.write(funcionario)