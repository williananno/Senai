#28/08/2024 Professor Gilberto - Aluno: Willian - Exercicio 1
import tkinter as tk   #Precisa instalar o Tkinter, ir no terminal e digitar: pip install tk
from tkinter import messagebox,ttk

janela = tk.Tk()
janela.title ("Cadastro")

def Salvar():
    resultadoNomeTutor = entryNomeTutor.get()
    resultadoNomePet = entryNomePet.get()
    resultadoData = entryData.get()
    resultadoEspecie = comboboxEspecie.get()
    resultadoRaca = entryRaca.get()
    messagebox.showinfo("Os dados do PET", f"Nome do tutor do PET: {resultadoNomeTutor}\n Nome do Pet: {resultadoNomePet} \n Data de Nascimento: {resultadoData}\n Espécie do Pet: {resultadoEspecie}\n Raça do Pet: {resultadoRaca}")

#Cadastro do Nome do Tutor.
labelNomeTutor = tk.Label (janela, text="Nome do tutor do PET", font=11)
labelNomeTutor.pack(padx=50, pady=5)

entryNomeTutor = tk.Entry (janela, width = 40, font =10)
entryNomeTutor.pack(padx=50, pady = 5)

#Cadastro do Nome do PET

labelNomePet = tk.Label (janela, text="Nome PET", font=11)
labelNomePet.pack(padx=50, pady=5)

entryNomePet = tk.Entry (janela, width = 40, font =10)
entryNomePet.pack(padx=50, pady = 5)

#Cadastro Data de Nascimento do PET

labelData = tk.Label (janela, text="Data de Nascimento", font=11)
labelData.pack(padx=50, pady=5)

entryData = tk.Entry (janela, width = 40, font =10)
entryData.pack(padx=50, pady = 5)

#Cadastro Espécie do PET       -----------------

labelEspecie = tk.Label (janela, text="Espécie do Pet", font=11)
labelEspecie.pack(padx=50, pady=5)
'''
#Código antigo, sem lista suspensa
entryEspecie = tk.Entry (janela, width = 40, font =10)
entryEspecie.pack(padx=50, pady = 5)
'''
especies = ["Cachorro", "Gato", "Pássaro", "Peixe"] #Lista de Espécies do PET
comboboxEspecie = ttk.Combobox(janela, values=especies, state="readonly", font=11) # Criação da combobox para espécies, state="readonly efine o estado da Combobox para "somente leitura". Isso significa que o usuário pode selecionar apenas um dos itens disponíveis na lista suspensa, mas não pode digitar valores novos ou alterar o texto manualmente
comboboxEspecie.pack(padx=50, pady=5)

#Fim Cadastro do Espécie do PET  -----------------

# Cadastro Raça do PET 

labelRaca = tk.Label (janela, text="Raça do Pet", font=11)
labelRaca.pack(padx=50, pady=5)

entryRaca = tk.Entry (janela, width = 40, font =10)
entryRaca.pack(padx=50, pady = 5)

#Criação do Botão Salvar
buttonSalvar = tk.Button(janela, text="Salvar", font=10, command=Salvar)
buttonSalvar.pack(pady=10)

#Executa o loop principal da interface gráfica
janela.mainloop()