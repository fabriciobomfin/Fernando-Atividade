"""
Nome do arquivo: sensores_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
import random

# Simulação de leitura dos sensores
def ler_sensores():
    temperatura = round(random.uniform(15, 35), 1)  # graus Celsius
    luminosidade = random.randint(0, 100)          # percentual
    presenca = random.choice([True, False])        # detecta presença ou não
    return temperatura, luminosidade, presenca

def abrir_tela_sensores():
    janela = Toplevel()
    janela.title("Sensores - Monitoramento e Controle")
    janela.geometry("400x400")
    janela.resizable(False, False)

    # Variáveis para exibir os sensores
    temp_var = StringVar()
    lum_var = StringVar()
    pres_var = StringVar()
    alarme_var = StringVar(value="Desligado")
    luz_var = StringVar(value="Desligada")

    # Função para atualizar leituras
    def atualizar_leituras():
        temp, lum, pres = ler_sensores()
        temp_var.set(f"{temp} °C")
        lum_var.set(f"{lum} %")
        pres_var.set("Sim" if pres else "Não")
        janela.after(3000, atualizar_leituras)  # Atualiza a cada 3 segundos

    # Funções para controlar atuadores
    def alternar_alarme():
        if alarme_var.get() == "Desligado":
            alarme_var.set("Ligado")
            messagebox.showinfo("Alarme", "Alarme ligado!")
        else:
            alarme_var.set("Desligado")
            messagebox.showinfo("Alarme", "Alarme desligado!")

    def alternar_luz():
        if luz_var.get() == "Desligada":
            luz_var.set("Ligada")
            messagebox.showinfo("Luz", "Luz ligada!")
        else:
            luz_var.set("Desligada")
            messagebox.showinfo("Luz", "Luz desligada!")

    # Layout
    Label(janela, text="Monitoramento dos Sensores", font=("Arial", 14, "bold")).pack(pady=15)

    frame_sensores = Frame(janela)
    frame_sensores.pack(pady=10)

    Label(frame_sensores, text="Temperatura:", font=("Arial", 12)).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(frame_sensores, textvariable=temp_var, font=("Arial", 12)).grid(row=0, column=1, sticky=W, padx=10, pady=5)

    Label(frame_sensores, text="Luminosidade:", font=("Arial", 12)).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Label(frame_sensores, textvariable=lum_var, font=("Arial", 12)).grid(row=1, column=1, sticky=W, padx=10, pady=5)

    Label(frame_sensores, text="Presença detectada:", font=("Arial", 12)).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Label(frame_sensores, textvariable=pres_var, font=("Arial", 12)).grid(row=2, column=1, sticky=W, padx=10, pady=5)

    frame_atuadores = Frame(janela)
    frame_atuadores.pack(pady=20)

    Label(frame_atuadores, text="Controle dos Atuadores", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

    Label(frame_atuadores, text="Alarme:", font=("Arial", 12)).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Label(frame_atuadores, textvariable=alarme_var, font=("Arial", 12)).grid(row=1, column=1, sticky=W, padx=10, pady=5)
    Button(frame_atuadores, text="Alternar Alarme", command=alternar_alarme, width=15).grid(row=1, column=2, padx=10, pady=5)

    Label(frame_atuadores, text="Luz:", font=("Arial", 12)).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Label(frame_atuadores, textvariable=luz_var, font=("Arial", 12)).grid(row=2, column=1, sticky=W, padx=10, pady=5)
    Button(frame_atuadores, text="Alternar Luz", command=alternar_luz, width=15).grid(row=2, column=2, padx=10, pady=5)

    atualizar_leituras()

    janela.mainloop()
