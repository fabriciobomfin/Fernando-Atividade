"""
Nome do arquivo: tela_login_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
import os
from tela_cadastro import abrir_tela_cadastro
from menu_inicial import abrir_menu_inicial  # menu_inicial.py deve ter a função abrir_menu_inicial(tipo_usuario)

ARQUIVO_USUARIOS = "usuarios.txt"

def verificar_credenciais(usuario, senha):
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            for linha in f:
                dados = linha.strip().split(";")
                if len(dados) == 3 and usuario == dados[0] and senha == dados[1]:
                    return dados[2]  # tipo de usuário
    return None

def abrir_tela_login():
    def realizar_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        tipo_usuario = verificar_credenciais(usuario, senha)
        if tipo_usuario:
            messagebox.showinfo("Login", f"Login realizado como {tipo_usuario}!")
            login.destroy()
            abrir_menu_inicial(tipo_usuario)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    def abrir_cadastro():
        login.destroy()
        abrir_tela_cadastro()

    login = Tk()
    login.title("Login - GestorTrans")
    login.geometry("350x250")
    login.configure(bg="#f4f4f4")

    Label(login, text="Login do Sistema", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

    Label(login, text="Usuário (e-mail):", bg="#f4f4f4").pack()
    entrada_usuario = Entry(login, width=30)
    entrada_usuario.pack(pady=5)

    Label(login, text="Senha:", bg="#f4f4f4").pack()
    entrada_senha = Entry(login, show="*", width=30)
    entrada_senha.pack(pady=5)

    Button(login, text="Entrar", width=25, bg="#4682B4", fg="white", command=realizar_login).pack(pady=10)
    Button(login, text="Cadastrar", width=25, command=abrir_cadastro).pack()

    login.mainloop()


if __name__ == "__main__":
    abrir_tela_login()
