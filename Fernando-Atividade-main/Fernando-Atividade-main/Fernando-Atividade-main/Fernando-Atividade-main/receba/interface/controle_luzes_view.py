# controle_luzes_view.py
from tkinter import *
from tkinter import messagebox

# Apenas interface gráfica – simulação de controle manual
def abrir_tela_controle_luzes():
    janela = Toplevel()
    janela.title("Controle Manual de Luzes")
    janela.geometry("400x250+600+300")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    def ligar_luz():
        messagebox.showinfo("Luz", "Luz LIGADA com sucesso.")

    def desligar_luz():
        messagebox.showinfo("Luz", "Luz DESLIGADA com sucesso.")

    titulo = Label(janela, text="Controle Manual de Luzes", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
    titulo.pack(pady=20)

    botao_ligar = Button(janela, text="Ligar Luz", width=20, height=2, bg="#32CD32", fg="white", font=("Arial", 12), command=ligar_luz)
    botao_ligar.pack(pady=10)

    botao_desligar = Button(janela, text="Desligar Luz", width=20, height=2, bg="#B22222", fg="white", font=("Arial", 12), command=desligar_luz)
    botao_desligar.pack(pady=5)

    janela.mainloop()
