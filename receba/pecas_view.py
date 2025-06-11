"""
Nome do arquivo: pecas_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: G91234
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox

def abrir_tela_pecas():
    tela_pecas = Toplevel()
    tela_pecas.title("GestorTrans - Gerenciamento de Peças")
    tela_pecas.geometry("400x400+600+150")
    tela_pecas.resizable(False, False)

    label_titulo = Label(tela_pecas, text="Gerenciamento de Peças", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=20)

    # Funções simuladas para as ações - só mensagem por enquanto
    def cadastrar_peca():
        messagebox.showinfo("Cadastro", "Aqui você implementa o cadastro de peças.")

    def listar_pecas():
        messagebox.showinfo("Listar", "Aqui você implementa a listagem de peças.")

    def editar_peca():
        messagebox.showinfo("Editar", "Aqui você implementa a edição de peças.")

    def excluir_peca():
        messagebox.showinfo("Excluir", "Aqui você implementa a exclusão de peças.")

    # Botões
    btn_cadastrar = Button(tela_pecas, text="Cadastrar Peça", width=25, command=cadastrar_peca)
    btn_cadastrar.pack(pady=10)

    btn_listar = Button(tela_pecas, text="Listar Peças", width=25, command=listar_pecas)
    btn_listar.pack(pady=10)

    btn_editar = Button(tela_pecas, text="Editar Peça", width=25, command=editar_peca)
    btn_editar.pack(pady=10)

    btn_excluir = Button(tela_pecas, text="Excluir Peça", width=25, command=excluir_peca)
    btn_excluir.pack(pady=10)

    tela_pecas.mainloop()
