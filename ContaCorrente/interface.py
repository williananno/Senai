import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Não vamos usar Resampling neste caso
import conta  # Importa as funções do arquivo conta.py

def formatar_saldo(saldo):
    """Formata o saldo para o formato monetário brasileiro."""
    return f"R$ {saldo:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def atualizar_saldo(saldo_label):
    saldo_atual = conta.verificar_saldo()
    saldo_label.config(text=f"Saldo: {formatar_saldo(saldo_atual)}")

def depositar(saldo_label, valor_entry):
    try:
        valor = float(valor_entry.get())
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        conta.depositar(valor)
        atualizar_saldo(saldo_label)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def sacar(saldo_label, valor_entry):
    try:
        valor = float(valor_entry.get())
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        conta.sacar(valor)
        atualizar_saldo(saldo_label)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def criar_interface():
    root = tk.Tk()
    root.title("Conta Bancária")
    root.geometry("300x250")
    root.configure(bg="#f0f0f0")  # Cor de fundo da janela

    # Adiciona imagem
    try:
        # Use Pillow para abrir e converter a imagem
        img = Image.open("banco.png")  # Substitua pelo caminho correto da sua imagem
        img = img.resize((100, 100), Image.LANCZOS)  # Usar Image.LANCZOS em vez de Resampling.LANCZOS
        img = ImageTk.PhotoImage(img)
        
        panel = tk.Label(root, image=img, bg="#f0f0f0")
        panel.image = img  # Mantém uma referência da imagem
        panel.pack(pady=10)

    except FileNotFoundError:
        messagebox.showerror("Erro", "Imagem do banco não encontrada.")

    # Frame para o saldo
    frame_saldo = tk.Frame(root, bg="#f0f0f0")
    frame_saldo.pack(pady=10)

    saldo_label = tk.Label(frame_saldo, text="Saldo: R$ 0,00", font=("Arial", 14), bg="#f0f0f0")
    saldo_label.pack()

    # Frame para entrada e botões
    frame_entrada = tk.Frame(root, bg="#f0f0f0")
    frame_entrada.pack(pady=10)

    tk.Label(frame_entrada, text="Valor:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10)

    valor_entry = tk.Entry(frame_entrada, font=("Arial", 12))
    valor_entry.grid(row=0, column=1, padx=10)

    btn_depositar = tk.Button(frame_entrada, text="Depositar", command=lambda: depositar(saldo_label, valor_entry), font=("Arial", 12), bg="#4CAF50", fg="white")
    btn_depositar.grid(row=1, column=0, pady=10)

    btn_sacar = tk.Button(frame_entrada, text="Sacar", command=lambda: sacar(saldo_label, valor_entry), font=("Arial", 12), bg="#f44336", fg="white")
    btn_sacar.grid(row=1, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
