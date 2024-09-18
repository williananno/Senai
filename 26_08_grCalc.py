#26/08/2024 Professor Gilberto - Aluno: Willian - Exercicio 2
import tkinter as tk   #Precisa instalar o Tkinter, ir no terminal e digitar: pip install tk
from tkinter import messagebox

#Função para somar os números e mostrar o resultado
def somar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"A soma é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def subtrair():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        messagebox.showinfo("Resultado", f"A subtração é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

#Configuração da janela principal
root = tk.Tk()
root.title("Soma de Números")   #Titulo da Janela principal.

#Criação dos widgets
label_num1 = tk.Label(root,text = "Digite o primeiro número:")
label_num1.pack(padx=90,pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack(padx=90,pady=5)

label_num2 = tk.Label(root,text = "Digite o segundo número:")
label_num2.pack(padx=90,pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(padx=90,pady=5)

button_somar = tk.Button(root, text="Somar", command=somar)
button_somar.pack(pady=20)

button_subtrair = tk.Button(root, text="Subtrair", command=subtrair)
button_subtrair.pack(pady=20)

#Executa o loop principal da interface gráfica
root.mainloop()
