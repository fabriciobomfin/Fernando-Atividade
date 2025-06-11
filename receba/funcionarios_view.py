"""
Nome do arquivo: pecas_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: G91234
Semestre: 2025.1
"""
import tkinter as tk
from tkinter import messagebox

CAMINHO_ARQUIVO = "dados/funcionarios.txt"

def salvar_funcionario(nome, cpf, cargo, endereco, telefone):
    with open(CAMINHO_ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{nome};{cpf};{cargo};{endereco};{telefone}\n")

def ler_funcionarios():
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def atualizar_funcionario(cpf_alvo, novos_dados):
    linhas = ler_funcionarios()
    atualizado = False
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        for linha in linhas:
            dados = linha.strip().split(";")
            if dados[1] == cpf_alvo:
                f.write(";".join(novos_dados) + "\n")
                atualizado = True
            else:
                f.write(linha)
    return atualizado

def excluir_funcionario(cpf_alvo):
    linhas = ler_funcionarios()
    encontrado = False
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        for linha in linhas:
            dados = linha.strip().split(";")
            if dados[1] != cpf_alvo:
                f.write(linha)
            else:
                encontrado = True
    return encontrado

def abrir_tela_funcionarios():
    janela = tk.Tk()
    janela.title("Cadastro de Funcionários")
    janela.geometry("600x400")

    tk.Label(janela, text="Cadastro de Funcionários", font=("Arial", 16, "bold")).pack(pady=10)

    frame = tk.Frame(janela)
    frame.pack(pady=10)

    # Campos de entrada
    tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="e")
    entry_nome = tk.Entry(frame, width=40)
    entry_nome.grid(row=0, column=1)

    tk.Label(frame, text="CPF:").grid(row=1, column=0, sticky="e")
    entry_cpf = tk.Entry(frame, width=40)
    entry_cpf.grid(row=1, column=1)

    tk.Label(frame, text="Cargo:").grid(row=2, column=0, sticky="e")
    entry_cargo = tk.Entry(frame, width=40)
    entry_cargo.grid(row=2, column=1)

    tk.Label(frame, text="Endereço:").grid(row=3, column=0, sticky="e")
    entry_endereco = tk.Entry(frame, width=40)
    entry_endereco.grid(row=3, column=1)

    tk.Label(frame, text="Telefone:").grid(row=4, column=0, sticky="e")
    entry_telefone = tk.Entry(frame, width=40)
    entry_telefone.grid(row=4, column=1)

    # Funções de ação
    def cadastrar():
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        cargo = entry_cargo.get()
        endereco = entry_endereco.get()
        telefone = entry_telefone.get()

        if nome and cpf:
            salvar_funcionario(nome, cpf, cargo, endereco, telefone)
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_cpf.delete(0, tk.END)
            entry_cargo.delete(0, tk.END)
            entry_endereco.delete(0, tk.END)
            entry_telefone.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Preencha ao menos o nome e CPF.")

    def listar():
        funcionarios = ler_funcionarios()
        if funcionarios:
            texto = "\n".join(funcionarios)
            messagebox.showinfo("Funcionários Cadastrados", texto)
        else:
            messagebox.showinfo("Lista Vazia", "Nenhum funcionário cadastrado.")

    def atualizar():
        cpf = entry_cpf.get()
        novos_dados = [
            entry_nome.get(),
            entry_cpf.get(),
            entry_cargo.get(),
            entry_endereco.get(),
            entry_telefone.get()
        ]
        if atualizar_funcionario(cpf, novos_dados):
            messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Funcionário com esse CPF não encontrado.")

    def excluir():
        cpf = entry_cpf.get()
        if excluir_funcionario(cpf):
            messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")
        else:
            messagebox.showwarning("Erro", "Funcionário com esse CPF não encontrado.")

    # Botões
    botoes = tk.Frame(janela)
    botoes.pack(pady=20)

    tk.Button(botoes, text="Cadastrar", command=cadastrar, width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
    tk.Button(botoes, text="Listar", command=listar, width=15).grid(row=0, column=1, padx=5)
    tk.Button(botoes, text="Atualizar", command=atualizar, width=15).grid(row=0, column=2, padx=5)
    tk.Button(botoes, text="Excluir", command=excluir, width=15).grid(row=0, column=3, padx=5)

    tk.Button(janela, text="Sair", command=janela.destroy, width=10, bg="#f44336", fg="white").pack(pady=10)

    janela.mainloop()

# Executar sozinho
if __name__ == "__main__":
    abrir_tela_funcionarios()
