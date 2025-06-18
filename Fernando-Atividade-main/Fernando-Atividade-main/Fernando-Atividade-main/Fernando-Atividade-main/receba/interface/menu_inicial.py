"""
Nome do arquivo: menu_inicial.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox

from funcionarios_view import abrir_tela_funcionarios
from clientes import abrir_clientes
from fornecedores_view import abrir_tela_fornecedores
from caminhoes_view import abrir_tela_caminhoes
from pecas_view import abrir_tela_pecas
from controle_galpao_view import abrir_tela_controle_galpao
from controle_luzes_view import abrir_tela_controle_luzes


def abrir_tela_entrada_saida():
    janela = Toplevel()
    janela.title("Registro de Entrada e Saída de Caminhões")
    janela.geometry("800x700")
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

    Button(frame_botoes, text="Salvar Registro", bg="#4CAF50", fg="white", width=20, height=2).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Listar Registros", bg="#2196F3", fg="white", width=20, height=2).grid(row=0, column=1, padx=10)


# Cores e fontes
COR_FUNDO = "#f4f4f4"
COR_BOTAO = "#4682B4"
COR_TEXTO = "#ffffff"
FONTE_TITULO = ("Arial", 18, "bold")
FONTE_BOTAO = ("Arial", 12)


def abrir_menu_inicial():
    menu_inicial = Tk()
    menu_inicial.title("GestorTrans - Sistema de Controle de Transportadora")
    menu_inicial.geometry("500x580+500+100")
    menu_inicial.resizable(False, False)
    menu_inicial.configure(bg=COR_FUNDO)

    def abrir_modulo(nome):
        if nome == "Clientes":
            abrir_clientes()
        elif nome == "Funcionários":
            abrir_tela_funcionarios()
        elif nome == "Fornecedores":
            abrir_tela_fornecedores()
        elif nome == "Caminhões":
            abrir_tela_caminhoes()
        elif nome == "Peças":
            abrir_tela_pecas()
        elif nome == "Entrada/Saída Caminhões":
            abrir_tela_entrada_saida()
        elif nome == "Controle de Galpão (Sensores)":
            abrir_tela_controle_galpao()
        elif nome == "Controle Manual de Luzes":
            abrir_tela_controle_luzes()
        else:
            messagebox.showinfo("Abrir Módulo", f"Você abriu o módulo: {nome}")

    def sair():
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja sair do sistema?")
        if resposta:
            menu_inicial.destroy()

    Label(menu_inicial, text=" Gerenciamento inicial", font=FONTE_TITULO, bg=COR_FUNDO, fg="#333").pack(pady=20)
    Label(menu_inicial, text="Sistema de Gerenciamento da Transportadora", font=("Arial", 12), bg=COR_FUNDO).pack(pady=5)

    botoes = [
        "Funcionários", "Clientes", "Caminhões", "Peças",
        "Fornecedores", "Entrada/Saída Caminhões",
        "Controle de Galpão (Sensores)", "Controle Manual de Luzes"
    ]

    for nome in botoes:
        Button(menu_inicial, text=nome, width=30, height=2, bg=COR_BOTAO, fg=COR_TEXTO,
               font=FONTE_BOTAO, command=lambda n=nome: abrir_modulo(n)).pack(pady=5)

    Button(menu_inicial, text="Sair", width=30, height=2, bg="#B22222", fg=COR_TEXTO,
           font=FONTE_BOTAO, command=sair).pack(pady=15)

    Label(menu_inicial, text="Versão 1.0", bg=COR_FUNDO, font=("Arial", 9, "italic")).pack(side=BOTTOM, pady=10)

    menu_inicial.mainloop()


# Executa o menu diretamente se o script for rodado isoladamente
if __name__ == "__main__":
    abrir_menu_inicial()
