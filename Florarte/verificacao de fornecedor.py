import cv2
import numpy as np
import pandas as pd
from PIL import Image
import os

def hex_to_bgr(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (4, 2, 0))

def encontrar_bolinha_cinza(imagem_caminho, cor_hex):
    # Adicionar a extensão ".jpg" ao caminho da imagem
    if not imagem_caminho.endswith(".jpg"):
        imagem_caminho += ".jpg"

    # Carregar a imagem
    imagem = cv2.imread(imagem_caminho)

    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detectar círculos usando a Transformada de Hough
    circulos = cv2.HoughCircles(imagem_cinza, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=5, maxRadius=50)

    cor_bgr = hex_to_bgr(cor_hex)

    if circulos is not None:
        # Convertendo os parâmetros dos círculos encontrados
        circulos = np.round(circulos[0, :]).astype("int")

        for (x, y, r) in circulos:
            # Verificar se o círculo está no canto inferior esquerdo
            if x < imagem.shape[1] // 4 and y > 3 * imagem.shape[0] // 4:
                # Verificar se o círculo é da cor especificada
                mascara = np.zeros_like(imagem_cinza)
                cv2.circle(mascara, (x, y), r, 255, -1)
                media_cor = cv2.mean(imagem, mask=mascara[:,:])[0:3]
                
                if all(abs(media_cor[i] - cor_bgr[i]) < 40 for i in range(3)):
                    return True

    return False

def processar_imagens(lista_imagens, cor_hex, diretorio):
    bolinha_encontrada = []
    bolinha_nao_encontrada = []

    for imagem_nome in lista_imagens:
        imagem_caminho = os.path.join(diretorio, imagem_nome)
        if encontrar_bolinha_cinza(imagem_caminho, cor_hex):
            bolinha_encontrada.append(imagem_nome)
        else:
            bolinha_nao_encontrada.append(imagem_nome)

    # Criar um DataFrame
    df = pd.DataFrame({
        'Imagens com Bolinha': pd.Series(bolinha_encontrada),
        'Imagens sem Bolinha': pd.Series(bolinha_nao_encontrada)
    })

    # Exportar para CSV
    df.to_csv(r'C:\Users\drdc\Downloads\codigos_fornecedor.txt', index=False)
    print("Resultados exportados para 'codigos_fornecedor.txt'")

# Exemplo de uso
lista_imagens = ["90000001_2", "94282001"]
diretorio_fixo = r"D:\\"
processar_imagens(lista_imagens, "#969696", diretorio_fixo)  # Hexadecimal da cor cinza
