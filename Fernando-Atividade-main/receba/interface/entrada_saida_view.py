"""
Nome do arquivo: pecas_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *

def abrir_tela_entrada_saida():
    janela = Tk()
    janela.title("Registro de Entrada e Saída de Caminhões")
    janela.geometry("600x450")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Registro de Entrada e Saída", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

    frame_principal = Frame(janela, bg="#f0f0f0")
    frame_principal.pack(pady=10)

    # ======= ENTRADA ========
    frame_entrada = LabelFrame(frame_principal, text="Entrada", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#f0f0f0")
    frame_entrada.grid(row=0, column=0, padx=20, pady=10)

    Label(frame_entrada, text="Data Entrada:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
    Entry(frame_entrada).grid(row=0, column=1)

    Label(frame_entrada, text="Hora Entrada:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
    Entry(frame_entrada).grid(row=1, column=1)

    Label(frame_entrada, text="KM Chegada:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
    Entry(frame_entrada).grid(row=2, column=1)

    # ======= SAÍDA ========
    frame_saida = LabelFrame(frame_principal, text="Saída", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#f0f0f0")
    frame_saida.grid(row=0, column=1, padx=20, pady=10)

    Label(frame_saida, text="Data Saída:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
    Entry(frame_saida).grid(row=0, column=1)

    Label(frame_saida, text="Hora Saída:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
    Entry(frame_saida).grid(row=1, column=1)

    Label(frame_saida, text="KM Saída:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
    Entry(frame_saida).grid(row=2, column=1)

    Label(frame_saida, text="Destino:", bg="#f0f0f0").grid(row=3, column=0, sticky="w")
    Entry(frame_saida).grid(row=3, column=1)

    Label(frame_saida, text="Roteiro:", bg="#f0f0f0").grid(row=4, column=0, sticky="w")
    Entry(frame_saida).grid(row=4, column=1)

    Label(frame_saida, text="Peso (kg):", bg="#f0f0f0").grid(row=5, column=0, sticky="w")
    Entry(frame_saida).grid(row=5, column=1)

    # ======= DADOS GERAIS ========
    frame_dados = LabelFrame(janela, text="Dados Complementares", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#f0f0f0")
    frame_dados.pack(pady=10)

    Label(frame_dados, text="Caminhão (ID/Placa):", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
    Entry(frame_dados).grid(row=0, column=1)

    Label(frame_dados, text="Motorista (ID/Nome):", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
    Entry(frame_dados).grid(row=1, column=1)

    # ======= BOTÕES ========
    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    Button(frame_botoes, text="Inserir", width=12, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
    Button(frame_botoes, text="Pesquisar", width=12, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
    Button(frame_botoes, text="Alterar", width=12, bg="#FFC107", fg="black").grid(row=0, column=2, padx=5)
    Button(frame_botoes, text="Excluir", width=12, bg="#F44336", fg="white").grid(row=0, column=3, padx=5)
    janela.mainloop()
