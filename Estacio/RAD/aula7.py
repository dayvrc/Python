import shutil
import os

def copiar_arquivos(origem, destino):
    try:
        for arquivo in os.listdir(origem):
            caminho_origem = os.path.join(origem, arquivo)
            caminho_destino = os.path.join(destino,arquivo)

            shutil.copy(caminho_origem, caminho_destino)
            print(f"Arquivo {arquivo} copiado!")

    except Exception as e:
        print(f"Erro ao copiar: {e}")

pasta_origem = r"Estacio\RAD\Origem"
pasta_destino = r"Estacio\RAD\Destino"

copiar_arquivos(pasta_origem, pasta_destino)
    