"""
Nome do arquivo: tela_cadastro.py

Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa

Turma: DB - 91164

Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
import os

ARQUIVO_USUARIOS = "usuarios.txt"

def cadastrar_usuario(nome, senha, tipo):
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            for linha in f:
                dados = linha.strip().split(";")
                if nome == dados[0]:
                    return False
    with open(ARQUIVO_USUARIOS, "a") as f:
        f.write(f"{nome};{senha};{tipo}\n")
    return True

def cadastrar():
    usuario = entrada_usuario.get().strip()
    senha = entrada_senha.get().strip()
    confirmar = entrada_confirmar.get().strip()
    tipo = tipo_var.get()

    if not usuario or not senha or not confirmar:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    if senha != confirmar:
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return

    if tipo not in ["ADM", "ADM GERAL", "ADM OFICINA"]:
        messagebox.showerror("Erro", "Selecione um tipo de usuário.")
        return

    if cadastrar_usuario(usuario, senha, tipo):
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        janela_cadastro.destroy()
        import tela_login_view
        tela_login_view.abrir_tela_login()
    else:
        messagebox.showerror("Erro", "Usuário já existe!")

def voltar_login():
    janela_cadastro.destroy()
    import tela_login_view
    tela_login_view.abrir_tela_login()

def abrir_tela_cadastro():
    global janela_cadastro, entrada_usuario, entrada_senha, entrada_confirmar, tipo_var

    janela_cadastro = Tk()
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("350x350")
    janela_cadastro.configure(bg="#f4f4f4")

    Label(janela_cadastro, text="Cadastrar novo usuário", font=("Arial", 14, "bold"), bg="#f4f4f4").pack(pady=10)

    Label(janela_cadastro, text="Usuário (e-mail):", bg="#f4f4f4").pack()
    entrada_usuario = Entry(janela_cadastro, width=30)
    entrada_usuario.pack(pady=5)

    Label(janela_cadastro, text="Senha:", bg="#f4f4f4").pack()
    entrada_senha = Entry(janela_cadastro, show="*", width=30)
    entrada_senha.pack(pady=5)

    Label(janela_cadastro, text="Confirmar Senha:", bg="#f4f4f4").pack()
    entrada_confirmar = Entry(janela_cadastro, show="*", width=30)
    entrada_confirmar.pack(pady=5)

    Label(janela_cadastro, text="Tipo de Usuário:", bg="#f4f4f4").pack()
    tipo_var = StringVar(janela_cadastro)
    tipo_var.set("Selecione")
    OptionMenu(janela_cadastro, tipo_var, "ADM", "ADM GERAL", "ADM OFICINA").pack(pady=5)

    Button(janela_cadastro, text="Cadastrar", width=25, bg="#4682B4", fg="white", command=cadastrar).pack(pady=10)
    Button(janela_cadastro, text="Voltar para Login", width=25, command=voltar_login).pack()

    janela_cadastro.mainloop()

# Apenas se você quiser testar diretamente:
if __name__ == "__main__":
    abrir_tela_cadastro()
