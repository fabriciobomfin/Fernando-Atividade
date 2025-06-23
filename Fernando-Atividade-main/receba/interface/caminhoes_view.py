"""
Nome do arquivo: caminhoes_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *

def abrir_tela_caminhoes():
    janela = Toplevel()
    janela.title("Cadastro de Caminhões")
    janela.geometry("400x550")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Caminhão", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    Label(frame, text="ID Caminhão:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=0, column=1, pady=5)

    Label(frame, text="Renavan:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=1, column=1, pady=5)

    Label(frame, text="Modelo:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=2, column=1, pady=5)

    Label(frame, text="Marca:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=3, column=1, pady=5)

    Label(frame, text="Cor:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=4, column=1, pady=5)

    Label(frame, text="Placa:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=5, column=1, pady=5)

    Label(frame, text="Chassi:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=6, column=1, pady=5)

    Label(frame, text="Status:", bg="#f0f0f0").grid(row=7, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=7, column=1, pady=5)

    Label(frame, text="Tipo:", bg="#f0f0f0").grid(row=8, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=8, column=1, pady=5)

    Label(frame, text="Peso (kg):", bg="#f0f0f0").grid(row=9, column=0, sticky="w", pady=5)
    Entry(frame, width=30).grid(row=9, column=1, pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2).grid(row=1, column=1, padx=10, pady=10)
