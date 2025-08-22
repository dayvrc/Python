import os
import shutil
import tkinter as tk
from tkinter import filedialog
import csv

def copiar_fotos(origem, destino, nomes_arquivos):
    for nome_arquivo in nomes_arquivos:
        caminho_origem = os.path.join(origem, f"{nome_arquivo}.jpg")  # Adiciona a extensão .jpg
        caminho_destino = os.path.join(destino, f"{nome_arquivo}.jpg")  # Adiciona a extensão .jpg
        shutil.copy2(caminho_origem, caminho_destino)  # Usando shutil.copy2 para manter os metadados

def importar_csv():
    root = tk.Tk()
    root.withdraw()
    arquivo_csv = filedialog.askopenfilename(title="Selecione o arquivo CSV")
    return arquivo_csv

def criar_pasta_destino():
    root = tk.Tk()
    root.withdraw()
    pasta_destino = filedialog.askdirectory(title="Selecione a pasta de destino")
    return pasta_destino

def processar_csv_e_copiar_imagens(arquivo_csv, pasta_origem, pasta_destino):
    with open(arquivo_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            nome_arquivo = row[0].strip()  # Remove espaços em branco antes e depois do nome
            copiar_fotos(pasta_origem, pasta_destino, [nome_arquivo])

def main():
    arquivo_csv = importar_csv()
    if not arquivo_csv:
        print("Nenhum arquivo CSV selecionado.")
        return

    pasta_origem = r"G:\.shortcut-targets-by-id\1-3XgYQ4XYUPIPVphK-DQPv4MYWJZ62vR\Imagens"  # Defina o caminho da pasta de origem
    pasta_destino = criar_pasta_destino()

    processar_csv_e_copiar_imagens(arquivo_csv, pasta_origem, pasta_destino)
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
