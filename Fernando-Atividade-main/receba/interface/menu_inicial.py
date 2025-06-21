"""
Nome do arquivo: menu_inicial.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox

from funcionarios_view import abrir_tela_funcionarios
from clientes_view import abrir_clientes
from fornecedores_view import abrir_tela_fornecedores
from caminhoes_view import abrir_tela_caminhoes
from manutencao_view import abrir_tela_manutencao
from sensores_view import abrir_tela_sensores
from controle_luzes_view import abrir_tela_controle_luzes
from endereco_view import abrir_tela_endereco
from contato_view import abrir_tela_contato
from entrada_saida_view import abrir_tela_entrada_saida
from produtos_view import abrir_tela_produtos


COR_FUNDO = "#f4f4f4"
COR_BOTAO = "#4682B4"
COR_BOTAO_HOVER = "#346799"
COR_TEXTO = "#ffffff"
FONTE_TITULO = ("Arial", 20, "bold")
FONTE_BOTAO = ("Arial", 12, "bold")


def abrir_menu_inicial():
    menu_inicial = Tk()
    menu_inicial.title("GestorTrans - Sistema de Controle de Transportadora")
    menu_inicial.geometry("700x600+400+50")
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
        elif nome == "Manutenção":
            abrir_tela_manutencao()
        elif nome == "Entrada/Saída Caminhões":
            abrir_tela_entrada_saida()
        elif nome == "Sensores":
            abrir_tela_sensores()
        elif nome == "Controle Manual de Luzes":
            abrir_tela_controle_luzes()
        elif nome == "Endereços":
            abrir_tela_endereco()
        elif nome == "Contatos":
            abrir_tela_contato()
        elif nome == "Produtos":
            abrir_tela_produtos()
        else:
            messagebox.showinfo("Abrir Módulo", f"Você abriu o módulo: {nome}")

    def sair():
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja sair do sistema?"):
            menu_inicial.destroy()

    def on_enter(e):
        e.widget['background'] = COR_BOTAO_HOVER

    def on_leave(e):
        e.widget['background'] = COR_BOTAO

    titulo_frame = Frame(menu_inicial, bg=COR_FUNDO)
    titulo_frame.pack(pady=10)
    Label(titulo_frame, text="Gerenciamento inicial", font=FONTE_TITULO, bg=COR_FUNDO, fg="#333").pack()
    Label(titulo_frame, text="Sistema de Gerenciamento da Transportadora", font=("Arial", 12), bg=COR_FUNDO).pack(pady=5)

    frame_externo = Frame(menu_inicial, bg=COR_FUNDO)
    frame_externo.pack(fill=BOTH, expand=True, padx=20, pady=10)

    canvas = Canvas(frame_externo, bg=COR_FUNDO, highlightthickness=0)
    scrollbar = Scrollbar(frame_externo, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    frame_scroll = Frame(canvas, bg=COR_FUNDO)
    canvas.create_window((0, 0), window=frame_scroll, anchor="n", width=640)

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scroll.bind("<Configure>", ajustar_scroll)

    def rolar_mouse(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", rolar_mouse)

    botoes = [
        ("Funcionários", "👷"),
        ("Clientes", "🧑‍🤝‍🧑"),
        ("Caminhões", "🚚"),
        ("Manutenção", "🔧"),
        ("Fornecedores", "🏭"),
        ("Entrada/Saída Caminhões", "📥📤"),
        ("Sensores", "🏠"),
        ("Controle Manual de Luzes", "💡"),
        ("Endereços", "📍"),
        ("Contatos", "📞"),
        ("Produtos", "📦"),
    ]

    for nome, icone in botoes:
        btn = Button(frame_scroll, text=f"{icone}  {nome}", width=30, height=2, bg=COR_BOTAO, fg=COR_TEXTO,
                     font=FONTE_BOTAO, relief=FLAT, command=lambda n=nome: abrir_modulo(n))
        btn.pack(pady=6)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    btn_sair = Button(frame_scroll, text="❌  Sair", width=30, height=2, bg="#B22222", fg=COR_TEXTO,
                      font=FONTE_BOTAO, relief=FLAT, command=sair)
    btn_sair.pack(pady=20)
    btn_sair.bind("<Enter>", lambda e: e.widget.config(bg="#7f1414"))
    btn_sair.bind("<Leave>", lambda e: e.widget.config(bg="#B22222"))

    Label(menu_inicial, text="Versão 1.0", bg=COR_FUNDO, font=("Arial", 9, "italic")).pack(side=BOTTOM, pady=10)

    menu_inicial.mainloop()


if __name__ == "__main__":
    abrir_menu_inicial()
