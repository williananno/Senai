#26/08/2024 Professor Gilberto - Aluno: Willian - Exercicio 1
import tkinter as tk   #Precisa instalar o Tkinter, ir no terminal e digitar: pip install tk
from tkinter import simpledialog, messagebox
'''
#Função para substituir o print
def print_to_gui(text):
    messagebox.showinfo("Print",text)

#Função para substituir o input
def input_from_gui (prompt):
    return simpledialog.askstring("Input",prompt)
'''

#Configuração básica da interface gráfica:

root = tk.Tk()
root.withdraw() #Esconde a janela principal

'''
#Exemplo de uso
print_to_gui ("Olá, mundo!")
user_input = input_from_gui ("Qual é o seu nome?")
print_to_gui(f"Seu nome é {user_input}")
'''

#Exemplo de uso 2
messagebox.showinfo("Informação","Olá, mundo!") # O primeiro parametro é o nome da Janela.
nomeDigitado = simpledialog.askstring("Identificação","Qual é o seu nome?")
nomeSobrenome = simpledialog.askstring("Identificação","Qual é o seu sobrenome?")
idade = simpledialog.askstring("Identificação","Qual é a sua idade?")
messagebox.showinfo("Tchau", f"Seu nome é {nomeDigitado} {nomeSobrenome} e sua idade é {idade}")