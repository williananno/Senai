#03/09/2024 Professor Gilberto - Aluno: Willian 
import tkinter as tk
from tkinter import messagebox
import requests

def buscar_endereco():
    estado = entry_estado.get().strip()
    cidade = entry_cidade.get().strip()
    endereco = entry_endereco.get().strip()

    if len(estado) != 2:
        messagebox.showerror("Erro", "Digite um Estado Válido de 2 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{estado}/{cidade}/{endereco}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()

        # Se `dados` for uma lista, pegue o primeiro item
        if isinstance(dados, list) and len(dados) > 0:
            dados = dados[0]

        # Verifique se `dados` é um dicionário e se não contém erro
        if isinstance(dados, dict) and "erro" not in dados:
            retornoAPi = (
                f"Logradouro: {dados.get('logradouro', 'Não disponível')}\n"
                f"Bairro: {dados.get('bairro', 'Não disponível')}\n"
                f"Cidade: {dados.get('localidade', 'Não disponível')}\n"
                f"Estado: {dados.get('uf', 'Não disponível')}\n"
                f"CEP: {dados.get('cep', 'Não disponível')}\n"
            )
            label_resultado.config(text=retornoAPi)
        else:
            messagebox.showerror("Erro", "Não encontrado o endereço mencionado.")
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")

root = tk.Tk()
root.title("Busca de Endereço")
root.geometry("400x600")

label_estado = tk.Label(root, text="Digite o Estado:")
label_estado.pack(pady=5)
entry_estado = tk.Entry(root)
entry_estado.pack(pady=5)

label_cidade = tk.Label(root, text="Digite a cidade:")
label_cidade.pack(pady=5)
entry_cidade = tk.Entry(root)
entry_cidade.pack(pady=5)

label_endereco = tk.Label(root, text="Digite o Endereço:")
label_endereco.pack(pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

botao_buscar = tk.Button(root, text="Buscar Endereço", command=buscar_endereco)
botao_buscar.pack(pady=10)

label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

root.mainloop()
