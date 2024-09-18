#27/08/2024 Professor Gilberto - Aluno: Willian - Exercicio 1
import tkinter as tk
from tkinter import Toplevel

def salvar():
    resultadoNome = entryNome.get()
    resultadoTelefone = entryTelefone.get()
    resultadoEmail = entryEmail.get()
    
    # Criar uma nova janela
    info_janela = Toplevel(janela)
    info_janela.title("Resultado")
    
    # Configurar o tamanho da nova janela
    info_janela.geometry("400x200")
    
    # Criar um Label para mostrar o resultado com fonte maior
    resultado_texto = f"Seu nome é: {resultadoNome}\nSeu telefone é: {resultadoTelefone}\nSeu e-mail é: {resultadoEmail}"
    labelResultado = tk.Label(info_janela, text=resultado_texto, font=("Arial", 14))
    labelResultado.pack(padx=20, pady=20)

    # Adicionar um botão para fechar a janela
    buttonFechar = tk.Button(info_janela, text="Fechar", command=info_janela.destroy, font=("Arial", 12))
    buttonFechar.pack(pady=10)

janela = tk.Tk()
janela.title("Cadastro de Cliente")

# *** Cadastro do nome do Cliente
labelNome = tk.Label (janela, text ="Nome", font=11, fg="blue", bg="yellow")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela, width=40, font=10)
entryNome.pack(padx=50 , pady= 5)

# *** Cadastro do nome do Telefone
labelTelefone = tk.Label (janela, text ="Telefone", font=11)
labelTelefone.pack(padx=50, pady=5)

entryTelefone = tk.Entry(janela, width=40, font=10)
entryTelefone.pack(padx=50 , pady= 5)

# *** Cadastro do nome do Email
labelEmail = tk.Label (janela, text ="Email", font=11)
labelEmail.pack(padx=50, pady=5)

entryEmail = tk.Entry(janela, width=40, font=10)
entryEmail.pack(padx=50 , pady= 5)

#Criação do Botão Salvar
buttonSalvar = tk.Button(janela, text="Salvar", font=10, command=salvar)
buttonSalvar.pack(pady=10)

janela.geometry("400x300")
janela.mainloop()