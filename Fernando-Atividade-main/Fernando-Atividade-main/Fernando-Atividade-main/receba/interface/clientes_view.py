### ✅ Nome do arquivo: `clientes.py`


"""
Nome do arquivo: clientes_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *

def abrir_clientes():
    janela = Toplevel()
    janela.title("Cadastro de Clientes")
    janela.geometry("500x560")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Cliente", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    Label(frame, text="ID Cliente:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=0, column=1, pady=5)

    Label(frame, text="Tipo:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=1, column=1, pady=5)

    Label(frame, text="Data Saída:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=2, column=1, pady=5)

    Label(frame, text="Nome:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=3, column=1, pady=5)

    Label(frame, text="CPF:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=4, column=1, pady=5)

    Label(frame, text="CNPJ:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=5, column=1, pady=5)

    Label(frame, text="Observações:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=6, column=1, pady=5)

    Label(frame, text="Endereço (ID):", bg="#f0f0f0").grid(row=7, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=7, column=1, pady=5)

    Label(frame, text="Motorista (ID Funcionário):", bg="#f0f0f0").grid(row=8, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=8, column=1, pady=5)

    Label(frame, text="Contato (ID):", bg="#f0f0f0").grid(row=9, column=0, sticky="w", pady=5)
    Entry(frame, width=35).grid(row=9, column=1, pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=30)

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2).grid(row=1, column=1, padx=10, pady=10)

