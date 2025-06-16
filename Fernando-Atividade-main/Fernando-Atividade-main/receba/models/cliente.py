"""
Nome do arquivo: cliente.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Cliente:
    def __init__(self, id_cliente, tipo, nome, cpf, cnpj, observacoes, id_endereco, id_contato):
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.nome = nome
        self.cpf = cpf
        self.cnpj = cnpj
        self.observacoes = observacoes
        self.id_endereco = id_endereco
        self.id_contato = id_contato
        self.caminho_arquivo = "PROJETO-IOT/data/cliente.txt"

    def __str__(self):
        return (f"ID: {self.id_cliente}, Tipo: {self.tipo}, Nome: {self.nome}, CPF: {self.cpf}, "
                f"CNPJ: {self.cnpj}, Observações: {self.observacoes}, ID Endereço: {self.id_endereco}, "
                f"ID Contato: {self.id_contato}")
    
    def to_line(self):
        return (f"{self.id_cliente},{self.tipo},{self.nome},{self.cpf},{self.cnpj},"
                f"{self.observacoes},{self.id_endereco},{self.id_contato}\n")
    
    # CRUD

    # Create
    def inserir_cliente(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    # Read
    def buscar_cliente(self, id_cliente):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_cliente},"):
                    return linha.strip()
        return None
        
    # Update
    def atualizar_cliente(self, id_cliente):
        clientes = self.listar_clientes()
        with open(self.caminho_arquivo, "w") as arquivo:
            for cliente in clientes:
                if cliente.startswith(f"{id_cliente},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(cliente)

    # Delete
    def excluir_cliente(self, id_cliente):
        clientes = self.listar_clientes()
        with open(self.caminho_arquivo, "w") as arquivo:
            for cliente in clientes:
                if not cliente.startswith(f"{id_cliente},"):
                    arquivo.write(cliente)
    