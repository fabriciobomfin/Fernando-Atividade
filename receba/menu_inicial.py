"""
Nome do arquivo: menu_inicial.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: G91234
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox

# Importações das interfaces dos módulos
from funcionarios_view import abrir_tela_funcionarios
from clientes import abrir_clientes
from fornecedores_view import abrir_tela_fornecedores
from caminhoes_view import abrir_tela_caminhoes
from pecas_view import abrir_tela_pecas
from controle_galpao_view import abrir_tela_controle_galpao  # <-- Importa o módulo Controle Galpão

# Cores e fontes
COR_FUNDO = "#f4f4f4"
COR_BOTAO = "#4682B4"
COR_TEXTO = "#ffffff"
FONTE_TITULO = ("Arial", 18, "bold")
FONTE_BOTAO = ("Arial", 12)

# Lógica para abrir cada módulo
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
    elif nome == "Saída de Caminhões":
        messagebox.showinfo("Módulo em desenvolvimento", "O módulo Saída de Caminhões ainda será implementado.")
    elif nome == "Controle de Galpão (Sensores)":
        abrir_tela_controle_galpao()
    else:
        messagebox.showinfo("Abrir Módulo", f"Você abriu o módulo: {nome}")

def sair():
    resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja sair do sistema?")
    if resposta:
        menu_inicial.destroy()

# Criação da janela principal
menu_inicial = Tk()
menu_inicial.title("GestorTrans - Sistema de Controle de Transportadora")
menu_inicial.geometry("500x580+500+100")
menu_inicial.resizable(False, False)
menu_inicial.configure(bg=COR_FUNDO)

# Título
titulo = Label(menu_inicial, text=" Gerenciamento inicial", font=FONTE_TITULO, bg=COR_FUNDO, fg="#333")
titulo.pack(pady=20)

subtitulo = Label(menu_inicial, text="Sistema de Gerenciamento da Transportadora", font=("Arial", 12), bg=COR_FUNDO)
subtitulo.pack(pady=5)

# Botões principais
botoes = [
    "Funcionários",
    "Clientes",
    "Caminhões",
    "Peças",
    "Fornecedores",
    "Saída de Caminhões",
    "Controle de Galpão (Sensores)",
    "Controle Manual de Luzes"
]

for nome in botoes:
    botao = Button(
        menu_inicial, text=nome, width=30, height=2, bg=COR_BOTAO, fg=COR_TEXTO,
        font=FONTE_BOTAO, command=lambda n=nome: abrir_modulo(n)
    )
    botao.pack(pady=5)

botao_sair = Button(
    menu_inicial, text="Sair", width=30, height=2, bg="#B22222", fg=COR_TEXTO,
    font=FONTE_BOTAO, command=sair
)
botao_sair.pack(pady=15)

Label(menu_inicial, text="Versão 1.0", bg=COR_FUNDO, font=("Arial", 9, "italic")).pack(side=BOTTOM, pady=10)

menu_inicial.mainloop()
