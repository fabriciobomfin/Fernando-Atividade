"""
Nome do arquivo: produtos.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Produtos:
    def __init__(self, id_produto, descricao, tipo, quantidade, validade, observacoes):
        self.id_produto = id_produto
        self.descricao = descricao
        self.tipo = tipo
        self.quantidade = quantidade
        self.validade = validade
        self.observacoes = observacoes
        self.caminho_arquivo = "PROJETO-IOT/data/produtos.txt"


    def __str__(self):
        return (f"ID: {self.id_produto}, Descrição: {self.descricao}, Tipo: {self.tipo}, "
                f"Quantidade: {self.quantidade}, Validade: {self.validade}, Observações: {self.observacoes}")
    
    def to_line(self):
        return (f"{self.id_produto},{self.descricao},{self.tipo},{self.quantidade},"
                f"{self.validade},{self.observacoes}\n")
    
    # CRUD

    # Create
    def inserir_produto(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    # Read
    def buscar_produto(self, id_produto):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_produto},"):
                    return linha.strip()
        return None
        
    # Update
    def atualizar_produto(self, id_produto):
        produtos = self.listar_produtos()
        with open(self.caminho_arquivo, "w") as arquivo:
            for produto in produtos:
                if produto.startswith(f"{id_produto},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(produto)
