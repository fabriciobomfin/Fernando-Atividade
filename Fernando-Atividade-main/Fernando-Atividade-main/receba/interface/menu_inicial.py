from tkinter import *
from tkinter import messagebox

from funcionarios_view import abrir_tela_funcionarios
from clientes import abrir_clientes
from fornecedores_view import abrir_tela_fornecedores
from caminhoes_view import abrir_tela_caminhoes
from pecas_view import abrir_tela_pecas
from controle_galpao_view import abrir_tela_controle_galpao
from controle_luzes_view import abrir_tela_controle_luzes  # <- NOVO: importa o módulo de controle manual de luzes

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
        elif nome == "Saída de Caminhões":
            messagebox.showinfo("Módulo em desenvolvimento", "O módulo Saída de Caminhões ainda será implementado.")
        elif nome == "Controle de Galpão (Sensores)":
            abrir_tela_controle_galpao()
        elif nome == "Controle Manual de Luzes":
            abrir_tela_controle_luzes()  # <- NOVO: chama a interface do controle de luz
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
        "Fornecedores", "Saída de Caminhões",
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