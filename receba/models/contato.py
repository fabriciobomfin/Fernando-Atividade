"""
Nome do arquivo: contato.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Contato:
    def __init__(self, id_contato, telefone, celular, email):
        self.id_contato = id_contato
        self.telefone = telefone
        self.celular = celular
        self.email = email
        self.caminho_arquivo = "PROJETO-IOT/data/contato.txt"
    

    def __str__(self):
        return f"ID: {self.id_contato}, Telefone: {self.telefone}, Celular: {self.celular}, Email: {self.email}"
    
    def to_line(self):
        return f"{self.id_contato},{self.telefone},{self.celular},{self.email}\n"
    
    #CRUD
    
    #Create
    def inserir_contato(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    #Read
    def buscar_contato(self, id_contato):
        with open(self.caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{id_contato},"):
                    return linha.strip()
        return None

    #Update
    def atualizar_contato(self, id_contato):
        contatos = self.listar_contatos()
        with open(self.caminho_arquivo, "w") as arquivo:
            for contato in contatos:
                if contato.startswith(f"{id_contato},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(contato)
    
    #Delete
    def excluir_contato(self, id_contato):
        contatos= self.listar_contatos()
        with open(self.caminho_arquivo, 'w') as arquivo:
            for contato in contatos:
                if not contato.startswith(f"{id_contato},"):
                    arquivo.write(contato)

        