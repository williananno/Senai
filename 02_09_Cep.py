#02/09/2024 Professor Gilberto - Aluno: Willian 
import tkinter as tk
from tkinter import messagebox
import requests   #Request = Requerimento , Response = Resposta

def buscar_endereco():
    cep = entry_cep.get().strip()  #Strip =O método strip() é usado para remover espaços em branco no início e no final da string obtida pelo get(). Isso é útil para garantir que não haja espaços adicionais que possam causar problemas ao processar o texto.
    
    if len(cep) != 8 or not cep.isdigit():  #len = tamanho da string
        messagebox.showerror("Erro", "Digite um CEP válido de 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200: #200 significa o retorno do site, que é OK, Sucesso, acessou; 400 seria falha.
        dados = response.json()
        
        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
        else:
            endereco = (
                f"Logradouro: {dados['logradouro']}\n"
                f"Bairro: {dados['bairro']}\n"
                f"Cidade: {dados['localidade']}\n"
                f"Estado: {dados['uf']}"
            )
            .config(text=endereclabel_resultadoo)
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")

# Configurando a janela principal
root = tk.Tk()
root.title("Busca de Endereço pelo CEP")
root.geometry("300x250")

# Campo de entrada para o CEP
label_cep = tk.Label(root, text="Digite o CEP:")
label_cep.pack(pady=5)
entry_cep = tk.Entry(root)
entry_cep.pack(pady=5)

# Botão para buscar o endereço
botao_buscar = tk.Button(root, text="Buscar Endereço", command=buscar_endereco)
botao_buscar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executando o loop da interface gráfica
root.mainloop()