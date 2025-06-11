"""
Nome do arquivo: pecas_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: G91234
Semestre: 2025.1
"""

import os
from tkinter import *
from tkinter import messagebox

ARQUIVO_CLIENTES = "data/clientes.txt"

def abrir_clientes():
    def salvar_cliente(nome, cpf, telefone):
        if not (nome and cpf and telefone):
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        pasta = os.path.dirname(ARQUIVO_CLIENTES)
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        with open(ARQUIVO_CLIENTES, "a") as arquivo:
            arquivo.write(f"{nome};{cpf};{telefone}\n")

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, END)
        entry_cpf.delete(0, END)
        entry_telefone.delete(0, END)

    def listar_clientes():
        if not os.path.exists(ARQUIVO_CLIENTES):
            messagebox.showinfo("Lista vazia", "Nenhum cliente cadastrado ainda.")
            return

        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            dados = arquivo.readlines()

        lista_text.delete(1.0, END)
        for linha in dados:
            nome, cpf, telefone = linha.strip().split(";")
            lista_text.insert(END, f"Nome: {nome} | CPF: {cpf} | Tel: {telefone}\n")

    def deletar_cliente():
        cpf_alvo = entry_cpf.get()
        if not cpf_alvo:
            messagebox.showwarning("CPF obrigatório", "Informe o CPF do cliente para deletar.")
            return

        if not os.path.exists(ARQUIVO_CLIENTES):
            return

        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            linhas = arquivo.readlines()

        with open(ARQUIVO_CLIENTES, "w") as arquivo:
            removido = False
            for linha in linhas:
                if cpf_alvo not in linha:
                    arquivo.write(linha)
                else:
                    removido = True

        if removido:
            messagebox.showinfo("Removido", "Cliente removido com sucesso.")
        else:
            messagebox.showinfo("Não encontrado", "Cliente não encontrado.")
        listar_clientes()
        limpar_campos()

    def sair():
        resposta = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
        if resposta:
            clientes_view.destroy()

    clientes_view = Toplevel()  # Usar Toplevel para abrir janela filha da principal
    clientes_view.title("Cadastro de Clientes")
    clientes_view.geometry("600x550")
    clientes_view.configure(bg="#f4f4f4")
    clientes_view.resizable(False, False)

    Label(clientes_view, text="Cadastro de Clientes", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

    frame_form = Frame(clientes_view, bg="#f4f4f4")
    frame_form.pack(pady=10)

    Label(frame_form, text="Nome:", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, sticky=W, pady=5)
    entry_nome = Entry(frame_form, width=40)
    entry_nome.grid(row=0, column=1, pady=5)

    Label(frame_form, text="CPF:", font=("Arial", 12), bg="#f4f4f4").grid(row=1, column=0, sticky=W, pady=5)
    entry_cpf = Entry(frame_form, width=40)
    entry_cpf.grid(row=1, column=1, pady=5)

    Label(frame_form, text="Telefone:", font=("Arial", 12), bg="#f4f4f4").grid(row=2, column=0, sticky=W, pady=5)
    entry_telefone = Entry(frame_form, width=40)
    entry_telefone.grid(row=2, column=1, pady=5)

    frame_botoes = Frame(clientes_view, bg="#f4f4f4")
    frame_botoes.pack(pady=10)

    Button(frame_botoes, text="Cadastrar", width=12, bg="#4682B4", fg="white",
           command=lambda: salvar_cliente(entry_nome.get(), entry_cpf.get(), entry_telefone.get())).grid(row=0, column=0, padx=5)

    Button(frame_botoes, text="Listar", width=12, bg="#4682B4", fg="white",
           command=listar_clientes).grid(row=0, column=1, padx=5)

    Button(frame_botoes, text="Deletar", width=12, bg="#4682B4", fg="white",
           command=deletar_cliente).grid(row=0, column=2, padx=5)

    Button(clientes_view, text="Sair", width=12, bg="#B22222", fg="white", font=("Arial", 12, "bold"),
           command=sair).pack(pady=15)

    lista_text = Text(clientes_view, height=15, width=70)
    lista_text.pack(pady=10)

# Se quiser testar só esse arquivo diretamente, descomente o código abaixo:
# if __name__ == "__main__":
#     from tkinter import Tk
#     root = Tk()
#     root.withdraw()  # Esconde janela root
#     abrir_clientes()
#     root.mainloop()
