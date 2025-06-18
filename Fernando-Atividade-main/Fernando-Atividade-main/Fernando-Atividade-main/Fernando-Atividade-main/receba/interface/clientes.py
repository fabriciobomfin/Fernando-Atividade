"""
Nome do arquivo: pecas_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

import os
from tkinter import *
from tkinter import messagebox

ARQUIVO_CLIENTES = "data/clientes.txt"

def abrir_clientes():
    def salvar_cliente(d_cliente, nome, cpf, cnpj, observacoes, endereco, contato):
        if not (d_cliente and nome and cpf and cnpj and endereco and contato):
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos obrigatórios!")
            return

        pasta = os.path.dirname(ARQUIVO_CLIENTES)
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        with open(ARQUIVO_CLIENTES, "a") as arquivo:
            arquivo.write(f"{d_cliente};{nome};{cpf};{cnpj};{observacoes};{endereco};{contato}\n")

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_d_cliente.delete(0, END)
        entry_nome.delete(0, END)
        entry_cpf.delete(0, END)
        entry_cnpj.delete(0, END)
        entry_observacoes.delete(0, END)
        entry_endereco.delete(0, END)
        entry_contato.delete(0, END)

    def listar_clientes():
        if not os.path.exists(ARQUIVO_CLIENTES):
            messagebox.showinfo("Lista vazia", "Nenhum cliente cadastrado ainda.")
            return

        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            dados = arquivo.readlines()

        lista_text.delete(1.0, END)
        for linha in dados:
            campos = linha.strip().split(";")
            if len(campos) >= 7:
                d_cliente, nome, cpf, cnpj, observacoes, endereco, contato = campos
                lista_text.insert(END, f"ID: {d_cliente} | Nome: {nome} | CPF: {cpf} | CNPJ: {cnpj} | Obs: {observacoes} | Endereço: {endereco} | Contato: {contato}\n")

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

    clientes_view = Toplevel()
    clientes_view.title("Cadastro de Clientes")
    clientes_view.geometry("750x600")
    clientes_view.configure(bg="#f4f4f4")
    clientes_view.resizable(False, False)

    Label(clientes_view, text="Cadastro de Clientes", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

    frame_form = Frame(clientes_view, bg="#f4f4f4")
    frame_form.pack(pady=10)

    labels = ["ID Cliente:", "Nome:", "CPF:", "CNPJ:", "Observações:", "Endereço:", "Contato:"]
    entries = []

    for i, texto in enumerate(labels):
        Label(frame_form, text=texto, font=("Arial", 12), bg="#f4f4f4").grid(row=i, column=0, sticky=W, pady=5)
        entry = Entry(frame_form, width=50)
        entry.grid(row=i, column=1, pady=5)
        entries.append(entry)

    entry_d_cliente, entry_nome, entry_cpf, entry_cnpj, entry_observacoes, entry_endereco, entry_contato = entries

    frame_botoes = Frame(clientes_view, bg="#f4f4f4")
    frame_botoes.pack(pady=10)

    Button(frame_botoes, text="Cadastrar", width=12, bg="#4682B4", fg="white",
           command=lambda: salvar_cliente(
               entry_d_cliente.get(), entry_nome.get(), entry_cpf.get(),
               entry_cnpj.get(), entry_observacoes.get(), entry_endereco.get(), entry_contato.get()
           )).grid(row=0, column=0, padx=5)

    Button(frame_botoes, text="Listar", width=12, bg="#4682B4", fg="white",
           command=listar_clientes).grid(row=0, column=1, padx=5)

    Button(frame_botoes, text="Deletar", width=12, bg="#4682B4", fg="white",
           command=deletar_cliente).grid(row=0, column=2, padx=5)

    Button(clientes_view, text="Sair", width=12, bg="#B22222", fg="white", font=("Arial", 12, "bold"),
           command=sair).pack(pady=15)

    lista_text = Text(clientes_view, height=15, width=90)
    lista_text.pack(pady=10)
