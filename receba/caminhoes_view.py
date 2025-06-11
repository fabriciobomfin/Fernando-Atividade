"""
Nome do arquivo: pecas_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: G91234
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox

caminhoes = []  # lista simples para armazenar caminhões (exemplo)

def abrir_tela_caminhoes():
    def adicionar_caminhao():
        placa = entrada_placa.get().strip().upper()
        modelo = entrada_modelo.get().strip()
        ano = entrada_ano.get().strip()

        if not placa or not modelo or not ano:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return
        if not ano.isdigit() or int(ano) < 1900 or int(ano) > 2100:
            messagebox.showwarning("Atenção", "Ano inválido.")
            return

        caminhao = {"placa": placa, "modelo": modelo, "ano": ano}
        caminhoes.append(caminhao)
        messagebox.showinfo("Sucesso", f"Caminhão {placa} cadastrado!")
        atualizar_lista()
        entrada_placa.delete(0, END)
        entrada_modelo.delete(0, END)
        entrada_ano.delete(0, END)

    def atualizar_lista():
        lista_caminhoes.delete(0, END)
        for i, c in enumerate(caminhoes, start=1):
            lista_caminhoes.insert(END, f"{i}. {c['placa']} - {c['modelo']} ({c['ano']})")

    janela = Toplevel()
    janela.title("GestorTrans - Caminhões")
    janela.geometry("450x400")
    janela.resizable(False, False)

    # Labels e Entradas
    Label(janela, text="Placa:").pack(pady=5)
    entrada_placa = Entry(janela)
    entrada_placa.pack()

    Label(janela, text="Modelo:").pack(pady=5)
    entrada_modelo = Entry(janela)
    entrada_modelo.pack()

    Label(janela, text="Ano:").pack(pady=5)
    entrada_ano = Entry(janela)
    entrada_ano.pack()

    btn_adicionar = Button(janela, text="Adicionar Caminhão", command=adicionar_caminhao, bg="#4682B4", fg="white")
    btn_adicionar.pack(pady=10)

    lista_caminhoes = Listbox(janela, width=50)
    lista_caminhoes.pack(pady=10)

    atualizar_lista()
