import os
import shutil
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox

def copiar_fotos(origem, destino, nomes_arquivos):
    erros = []
    for nome_arquivo in nomes_arquivos:
        nome_arquivo = nome_arquivo.strip()
        if not nome_arquivo.lower().endswith('.jpg'):
            nome_arquivo += '.jpg'

        caminho_origem = os.path.join(origem, nome_arquivo)
        caminho_destino = os.path.join(destino, nome_arquivo)

        try:
            shutil.copy2(caminho_origem, caminho_destino)
        except FileNotFoundError:
            erros.append(nome_arquivo)

    return erros

def selecionar_origem():
    caminho = filedialog.askdirectory(title="Selecione a pasta onde estão as fotos")
    if caminho:
        entrada_origem.delete(0, END)
        entrada_origem.insert(0, caminho)

def selecionar_destino():
    caminho = filedialog.askdirectory(title="Selecione a pasta onde colocar as fotos separadas")
    if caminho:
        entrada_destino.delete(0, END)
        entrada_destino.insert(0, caminho)

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(title="Selecione o arquivo .txt", filetypes=[("Text files", "*.txt")])
    if caminho:
        entrada_txt.delete(0, END)
        entrada_txt.insert(0, caminho)

def iniciar_copia():
    origem = entrada_origem.get()
    destino = entrada_destino.get()
    arquivo_txt = entrada_txt.get()

    if not (origem and destino and arquivo_txt):
        messagebox.showwarning("Campos vazios", "Preencha todos os campos antes de iniciar.")
        return

    if not os.path.exists(arquivo_txt):
        messagebox.showerror("Erro", "Arquivo de texto não encontrado.")
        return

    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        nomes = f.readlines()

    erros = copiar_fotos(origem, destino, nomes)

    if erros:
        messagebox.showwarning("Concluído com erros", f"{len(erros)} arquivos não encontrados:\n" + "\n".join(erros))
    else:
        messagebox.showinfo("Sucesso", "Todos os arquivos foram copiados com sucesso!")

# ----- INTERFACE GRÁFICA MODERNA -----
janela = tb.Window(themename="flatly")
janela.title("SAF - Separador Automatico de Fotos")
janela.geometry("500x350")
janela.resizable(False, False)

# Caminho origem
tb.Label(janela, text="Selecione a pasta onde estão as fotos", bootstyle=PRIMARY).pack(pady=(10, 0))
entrada_origem = tb.Entry(janela, width=60)
entrada_origem.pack()
tb.Button(janela, text="Selecionar pasta", command=selecionar_origem, bootstyle=INFO).pack(pady=(10, 10))

# Caminho destino
tb.Label(janela, text="Selecione a pasta onde colocar as fotos separadas", bootstyle=PRIMARY).pack()
entrada_destino = tb.Entry(janela, width=60)
entrada_destino.pack()
tb.Button(janela, text="Selecionar pasta", command=selecionar_destino, bootstyle=INFO).pack(pady=(10, 10))

# Arquivo .txt
tb.Label(janela, text="Selecione o arquivo .txt com os códigos dos produtos:", bootstyle=PRIMARY).pack()
entrada_txt = tb.Entry(janela, width=60)
entrada_txt.pack()
tb.Button(janela, text="Selecionar arquivo", command=selecionar_arquivo, bootstyle=INFO).pack(pady=(10, 10))

# Botão de iniciar
tb.Button(janela, text="Iniciar cópia", command=iniciar_copia, bootstyle=SUCCESS, width=20).pack(pady=10)

janela.mainloop()
