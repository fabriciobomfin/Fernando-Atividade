"""
Nome do arquivo: fornecedores_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import messagebox

def abrir_tela_fornecedores():
    janela = tk.Tk()
    janela.title("Cadastro de Fornecedores")
    janela.geometry("600x400")

    # Título
    tk.Label(janela, text="Cadastro de Fornecedores", font=("Arial", 16, "bold")).pack(pady=10)

    # Frame principal
    frame = tk.Frame(janela)
    frame.pack(pady=10)

    # Campos de entrada
    tk.Label(frame, text="Razão Social:").grid(row=0, column=0, sticky="e")
    entry_razao_social = tk.Entry(frame, width=40)
    entry_razao_social.grid(row=0, column=1)

    tk.Label(frame, text="CNPJ:").grid(row=1, column=0, sticky="e")
    entry_cnpj = tk.Entry(frame, width=40)
    entry_cnpj.grid(row=1, column=1)

    tk.Label(frame, text="Endereço:").grid(row=2, column=0, sticky="e")
    entry_endereco = tk.Entry(frame, width=40)
    entry_endereco.grid(row=2, column=1)

    tk.Label(frame, text="Telefone:").grid(row=3, column=0, sticky="e")
    entry_telefone = tk.Entry(frame, width=40)
    entry_telefone.grid(row=3, column=1)

    tk.Label(frame, text="Email:").grid(row=4, column=0, sticky="e")
    entry_email = tk.Entry(frame, width=40)
    entry_email.grid(row=4, column=1)

    # Funções simuladas (trocar pelos seus métodos reais depois)
    def cadastrar():
        razao_social = entry_razao_social.get()
        cnpj = entry_cnpj.get()
        endereco = entry_endereco.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        if razao_social and cnpj:
            messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Preencha ao menos a razão social e o CNPJ.")

    def listar():
        messagebox.showinfo("Listar", "Listando todos os fornecedores...")

    def atualizar():
        messagebox.showinfo("Atualizar", "Função de atualizar fornecedor...")

    def excluir():
        messagebox.showinfo("Excluir", "Função de excluir fornecedor...")

    # Botões de ação
    botoes = tk.Frame(janela)
    botoes.pack(pady=20)

    tk.Button(botoes, text="Cadastrar", command=cadastrar, width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
    tk.Button(botoes, text="Listar", command=listar, width=15).grid(row=0, column=1, padx=5)
    tk.Button(botoes, text="Atualizar", command=atualizar, width=15).grid(row=0, column=2, padx=5)
    tk.Button(botoes, text="Excluir", command=excluir, width=15).grid(row=0, column=3, padx=5)

    # Botão de sair
    tk.Button(janela, text="Sair", command=janela.destroy, width=10, bg="#f44336", fg="white").pack(pady=10)

    janela.mainloop()

# Para testes isolados (remova se for importar no menu principal)
if __name__ == "__main__":
    abrir_tela_fornecedores()
