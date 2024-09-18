#04/09/2024 Professor Gilberto - Aluno: Willian 
import tkinter as tk
from tkinter import messagebox
import requests

def calcular_total():
    try:
        lanche = str(entry_lanche.get().strip())
        quantidade = int(entry_quantidade.get().strip())
        preco = float(entry_preco.get().strip())
        totalPedido = float(entry_preco.get().strip())

        totalPedido=quantidade*preco
        totalPedido = (f"O seu Lanche é {lanche} , sendo {quantidade} quantidade ,"
                    f"\n no valor Total de R$ {totalPedido:.2f} reais")
        label_resultado.config(text=totalPedido, font=12)
    except ValueError:
        messagebox.showerror("Erro", "Digite números no campo Quantidade e Preço")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

root = tk.Tk()
root.title("Sistema IRango 1.0")
root.geometry("700x700")

label_pedido = tk.Label(root, text = "Faça o seu pedido:", font=("Arial",20))
label_pedido.pack(padx=5)

label_lanche = tk.Label(root, text = "Lanche", font=("Arial",16))
label_lanche.pack(anchor='w',padx=20)
entry_lanche = tk.Entry((root), font=("Arial",12))
entry_lanche.pack(anchor='w',padx=20)

label_quantidade = tk.Label(root, text = "Quantidade", font=("Arial",16))
label_quantidade.pack(anchor='w',padx=20)
entry_quantidade = tk.Entry((root), font=("Arial",12))
entry_quantidade.pack(anchor='w',padx=20)

label_preco = tk.Label(root, text = "Preço", font=("Arial",16))
label_preco.pack(anchor='w',padx=20)
entry_preco = tk.Entry((root), font=("Arial",12))
entry_preco.pack(anchor='w',padx=20)

label_totalPedido = tk.Label(root, text = "Total Pedido", font=("Arial",16))
label_totalPedido.pack(anchor='w',padx=20)
label_resultado = tk.Label(root, text="", font=("Arial",16))
label_resultado.pack(pady=10)

botao_calcular = tk.Button(root, text="Calcular Total", command=calcular_total, font=11)
botao_calcular.pack(pady=10)

root.mainloop()