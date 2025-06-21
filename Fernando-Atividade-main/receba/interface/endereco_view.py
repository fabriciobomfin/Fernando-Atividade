"""
Nome do arquivo: endereco_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *

def abrir_tela_endereco():
    janela = Toplevel()
    janela.title("Cadastro de Endereço")
    janela.geometry("700x700")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Endereço", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    Label(frame, text="ID Endereço:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=0, column=1, pady=5)

    Label(frame, text="Logradouro:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=1, column=1, pady=5)

    Label(frame, text="Número:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=2, column=1, pady=5)

    Label(frame, text="Bairro:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=3, column=1, pady=5)

    Label(frame, text="CEP:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=4, column=1, pady=5)

    Label(frame, text="Cidade:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=5, column=1, pady=5)

    Label(frame, text="UF:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=6, column=1, pady=5)

    Label(frame, text="Complemento:", bg="#f0f0f0").grid(row=7, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=7, column=1, pady=5)

    Label(frame, text="Data de Saída:", bg="#f0f0f0").grid(row=8, column=0, sticky="w", pady=5)
    Entry(frame, width=40).grid(row=8, column=1, pady=5)

    # Botões
    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=30)

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2).grid(row=1, column=1, padx=10, pady=10)
