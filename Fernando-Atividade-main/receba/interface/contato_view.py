"""
Nome do arquivo: contato_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *

def abrir_tela_contato():
    janela = Toplevel()
    janela.title("Cadastro de Contato")
    janela.geometry("400x300")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Contato", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    Label(frame, text="ID Contato:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
    Entry(frame).grid(row=0, column=1)

    Label(frame, text="Telefone:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
    Entry(frame).grid(row=1, column=1)

    Label(frame, text="Celular:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
    Entry(frame).grid(row=2, column=1)

    Label(frame, text="Email:", bg="#f0f0f0").grid(row=3, column=0, sticky="w")
    Entry(frame).grid(row=3, column=1)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=15)

    Button(frame_botoes, text="Inserir", width=12, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
    Button(frame_botoes, text="Pesquisar", width=12, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
    Button(frame_botoes, text="Alterar", width=12, bg="#FFC107", fg="black").grid(row=0, column=2, padx=5)
    Button(frame_botoes, text="Excluir", width=12, bg="#F44336", fg="white").grid(row=0, column=3, padx=5)
