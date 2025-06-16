"""
Nome do arquivo: saida_caminhoes_view.py
Equipe: Fabrício Bomfim, 
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Dados temporários para exemplo (depois substituir por banco de dados)
saidas = []

def abrir_tela_saida_caminhoes():
    tela = Toplevel()
    tela.title("Saída de Caminhões")
    tela.geometry("600x400+550+150")
    tela.resizable(False, False)

    # Função para registrar saída
    def registrar_saida():
        placa = entrada_placa.get().strip()
        motorista = entrada_motorista.get().strip()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if not placa or not motorista:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        
        saida = {"placa": placa, "motorista": motorista, "data_hora": data_hora}
        saidas.append(saida)
        atualizar_lista()
        entrada_placa.delete(0, END)
        entrada_motorista.delete(0, END)
        messagebox.showinfo("Sucesso", "Saída registrada com sucesso!")

    # Função para atualizar listbox
    def atualizar_lista():
        listbox_saidas.delete(0, END)
        for i, s in enumerate(saidas, 1):
            listbox_saidas.insert(END, f"{i}. Placa: {s['placa']} | Motorista: {s['motorista']} | Hora: {s['data_hora']}")

    # Layout
    Label(tela, text="Registrar Saída de Caminhão", font=("Arial", 14, "bold")).pack(pady=10)

    frame_form = Frame(tela)
    frame_form.pack(pady=10)

    Label(frame_form, text="Placa do Caminhão:", font=("Arial", 12)).grid(row=0, column=0, sticky=W, padx=5, pady=5)
    entrada_placa = Entry(frame_form, width=20, font=("Arial", 12))
    entrada_placa.grid(row=0, column=1, padx=5, pady=5)

    Label(frame_form, text="Nome do Motorista:", font=("Arial", 12)).grid(row=1, column=0, sticky=W, padx=5, pady=5)
    entrada_motorista = Entry(frame_form, width=30, font=("Arial", 12))
    entrada_motorista.grid(row=1, column=1, padx=5, pady=5)

    btn_registrar = Button(tela, text="Registrar Saída", bg="#4682B4", fg="white", font=("Arial", 12), width=20, command=registrar_saida)
    btn_registrar.pack(pady=10)

    Label(tela, text="Saídas Registradas:", font=("Arial", 14, "bold")).pack(pady=10)

    listbox_saidas = Listbox(tela, width=80, height=10, font=("Arial", 10))
    listbox_saidas.pack(padx=10, pady=5)

    btn_fechar = Button(tela, text="Fechar", bg="#B22222", fg="white", font=("Arial", 12), width=15, command=tela.destroy)
    btn_fechar.pack(pady=15)

    atualizar_lista()
    tela.mainloop()
