import tkinter as tk
from datetime import datetime
from tkinter import messagebox, simpledialog, ttk, PhotoImage
import json
import os

# Função para obter o próximo número de chamado
def obter_proximo_numero_chamado():
    if os.path.exists("chamados.json"):
        with open("chamados.json", "r") as arquivo:
            chamados = json.load(arquivo)
        if chamados:
            ultimo_chamado = chamados[-1]
            ultimo_numero = int(ultimo_chamado["numero_chamado"])
            return ultimo_numero + 1
    return 1  # Começa com 1 se não houver chamados ainda

# Função para salvar o pedido em um arquivo JSON
def salvar_chamado():
    nome_cliente = entry_nome.get()
    problema = comboboxProblema.get()
    descricao = text_descricao.get("1.0", tk.END).strip()  # Obtém todo o texto da área de texto
    prioridades = comboboxPrioridade.get()
    numero_chamado = str(obter_proximo_numero_chamado())  # Gera o próximo número do chamado
    data = dataNow
    
    if not nome_cliente or not problema or not descricao or not prioridades:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    # Estrutura do pedido
    chamado = {
        "numero_chamado": numero_chamado,
        "nome_cliente": nome_cliente,
        "problema": problema,
        "descricao": descricao,
        "prioridades": prioridades,
        "data": data, 
    }

    # Verifica se o arquivo JSON já existe
    if os.path.exists("chamados.json"):
        with open("chamados.json", "r") as arquivo:
            chamados = json.load(arquivo)
    else:
        chamados = []

    # Adiciona o novo pedido
    chamados.append(chamado)

    # Salva no arquivo JSON
    with open("chamados.json", "w") as arquivo:
        json.dump(chamados, arquivo, indent=4)

    # Exibe o número do chamado na tela
    entry_chamado.config(state=tk.NORMAL)  # Permite editar o campo temporariamente
    entry_chamado.delete(0, tk.END)
    entry_chamado.insert(0, numero_chamado)
    entry_chamado.config(state=tk.DISABLED)  # Desabilita o campo para evitar edições

    messagebox.showinfo("Sucesso", f"Chamado salvo com sucesso! Número do Chamado: {numero_chamado}")

    # Limpa os campos após salvar
    limpar_campos()

# Função para localizar o pedido em um arquivo JSON
def recuperar_chamado():
    if os.path.exists("chamados.json"):
        numero_chamado = simpledialog.askstring("Recuperar Chamado", "Digite o número do chamado:")
        if not numero_chamado:
            return

        with open("chamados.json", "r") as arquivo:
            chamados = json.load(arquivo)

        # Procura o chamado pelo número do chamado
        for chamado in chamados:
            if chamado["numero_chamado"] == numero_chamado:
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, chamado["nome_cliente"])
                
                comboboxProblema.set(chamado["problema"])
                
                text_descricao.delete("1.0", tk.END)
                text_descricao.insert("1.0", chamado["descricao"])
                
                comboboxPrioridade.set(chamado["prioridades"])
                
                entry_data.config(text=chamado["data"])
                
                messagebox.showinfo("Chamado Encontrado", f"Chamado número {numero_chamado} encontrado!")
                return

        messagebox.showinfo("Chamado não encontrado", f"Chamado com número '{numero_chamado}' não encontrado.")
    else:
        messagebox.showinfo("Sem Chamados", "Nenhum chamado cadastrado até o momento.")

# Função para limpar os campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    comboboxProblema.set('')
    text_descricao.delete("1.0", tk.END)
    comboboxPrioridade.set('')
    entry_nome.focus()

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Chamados Técnicos")
janela.geometry("500x500")

# Define o ícone da janela usando um arquivo .png
janela.iconphoto(False, PhotoImage(file='C:/Users/aluno/Downloads/images.png'))

#INICIO - Labels e Entries para os campos
label_nome = tk.Label(janela, text="Nome do Cliente", font=("Arial", 12))
label_nome.grid(row=0, column=0)

entry_nome = tk.Entry(janela, font=("Arial", 12))
entry_nome.grid(row=0, column=1, pady=5)

label_problema = tk.Label(janela, text="Problema", font=("Arial", 12))
label_problema.grid(row=1, column=0, pady=5)

problema = ["Problema de Rede", "Falha de Software", "Erro de Hardware"]
comboboxProblema = ttk.Combobox(janela, values=problema, state="readonly", font=("Arial", 12))
comboboxProblema.grid(row=1, column=1)

label_descricao = tk.Label(janela, text="Descrição do problema", font=("Arial", 12))
label_descricao.grid(row=2, column=0, pady=5)

# Substituindo Entry por Text para descrição
text_descricao = tk.Text(janela, height=4, width=40, font=("Arial", 12))
text_descricao.grid(row=2, column=1, pady=5)

# Cadastro Prioridades
label_prioridade = tk.Label(janela, text="Prioridades", font=("Arial", 12))
label_prioridade.grid(row=3, column=0)

prioridade = ["Baixa", "Média", "Alta"]
comboboxPrioridade = ttk.Combobox(janela, values=prioridade, state="readonly", font=("Arial", 12))
comboboxPrioridade.grid(row=3, column=1)

# Fim Cadastro Prioridades

label_data = tk.Label(janela, text="Data", font=("Arial", 12))
label_data.grid(row=4, column=0, pady=5)

dataNow = datetime.now().strftime("%d/%m/%Y")
entry_data = tk.Label(janela)
entry_data.grid(row=4, column=1, pady=5)
entry_data.config(text=dataNow)

label_chamado = tk.Label(janela, text="Número do Chamado", font=("Arial", 12))
label_chamado.grid(row=5, column=0, pady=5)

entry_chamado = tk.Entry(janela, font=("Arial", 12))
entry_chamado.grid(row=5, column=1, pady=5)
entry_chamado.config(state=tk.DISABLED)  # Inicialmente desabilita o campo

# FINAL - Labels e Entries para os campos

# Botões organizados em duas linhas
botao_salvar = tk.Button(janela, text="Salvar Chamado", width=30, command=salvar_chamado)
botao_salvar.grid(row=6, column=1)

botao_localizar = tk.Button(janela, text="Localizar Chamado", width=30, command=recuperar_chamado)
botao_localizar.grid(row=6, column=0)

botao_novo_chamado = tk.Button(janela, text="Novo Chamado", width=30, command=limpar_campos)
botao_novo_chamado.grid(row=7, column=0)

janela.mainloop()
