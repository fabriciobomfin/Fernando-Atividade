"""
Nome do arquivo: fornecedor.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Fornecedor:
    def __init__(self, id_fornecedor, cnpj, razao_social, nome_fantasia, area_atuacao, id_contato, id_produtos):
        self.id_fornecedor = id_fornecedor
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.area_atuacao = area_atuacao
        self.contato = id_contato
        self.produtos = id_produtos
        self.caminho_arquivo = "PROJETO-IOT/data/fornecedor.txt"

    def __str__(self):
        return f"ID: {self.id_fornecedor}, CNPJ: {self.cnpj}, Razão Social: {self.razao_social}, Nome Fantasia: {self.nome_fantasia}, Área de Atuação: {self.area_atuacao}, Contato: {self.contato}, Produtos: {self.produtos}"
    
    def to_line(self):
        return f"{self.id_fornecedor},{self.cnpj},{self.razao_social},{self.nome_fantasia},{self.area_atuacao},{self.contato},{self.produtos}\n"
    
    # CRUD

    # Create
    def inserir_fornecedor(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())
    
    # Read
    def buscar_fornecedor(self, id_fornecedor):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_fornecedor},"):
                    return linha.strip()
        return None
    
    # Update
    def atualizar_fornecedor(self, id_fornecedor):
        fornecedores = self.listar_fornecedores()
        with open(self.caminho_arquivo, "w") as arquivo:
            for fornecedor in fornecedores:
                if fornecedor.startswith(f"{id_fornecedor},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(fornecedor)