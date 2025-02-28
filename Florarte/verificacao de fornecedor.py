import cv2
import numpy as np
import pandas as pd
import os

def hex_to_bgr(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (4, 2, 0))

def encontrar_bolinha_cinza(imagem_caminho, cor_hex, tamanho_imagem, tamanho_circulo):
    # Adicionar a extensão ".jpg" ao caminho da imagem, se necessário
    if not imagem_caminho.endswith(".jpg"):
        imagem_caminho += ".jpg"

    # Carregar a imagem
    imagem = cv2.imread(imagem_caminho)
    
    # Redimensionar a imagem para o tamanho fixo
    imagem = cv2.resize(imagem, tamanho_imagem)

    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detectar círculos usando a Transformada de Hough
    circulos = cv2.HoughCircles(imagem_cinza, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=tamanho_circulo, maxRadius=tamanho_circulo)

    cor_bgr = hex_to_bgr(cor_hex)

    if circulos is not None:
        # Convertendo os parâmetros dos círculos encontrados
        circulos = np.round(circulos[0, :]).astype("int")

        for (x, y, r) in circulos:
            # Verificar se o círculo está no canto inferior esquerdo
            if abs(x - 28) < 10 and abs(y - 912) < 10:
                # Verificar se o círculo é da cor especificada
                mascara = np.zeros_like(imagem_cinza)
                cv2.circle(mascara, (x, y), r, 255, -1)
                media_cor = cv2.mean(imagem, mask=mascara[:,:])[0:3]
                
                if all(abs(media_cor[i] - cor_bgr[i]) < 40 for i in range(3)):
                    return True

    return False

def processar_imagens(diretorio, cor_hex, tamanho_imagem, tamanho_circulo):
    bolinha_encontrada = []
    bolinha_nao_encontrada = []

    # Listar todos os arquivos na pasta
    for imagem_nome in os.listdir(diretorio):
        # Verificar se o arquivo tem a extensão ".jpg"
        if imagem_nome.endswith(".jpg"):
            imagem_caminho = os.path.join(diretorio, imagem_nome)
            if encontrar_bolinha_cinza(imagem_caminho, cor_hex, tamanho_imagem, tamanho_circulo):
                bolinha_encontrada.append(imagem_nome)
            else:
                bolinha_nao_encontrada.append(imagem_nome)

    # Criar um DataFrame
    df = pd.DataFrame({
        'Imagens Fornecedor': pd.Series(bolinha_encontrada),
        'Imagens Interna': pd.Series(bolinha_nao_encontrada)
    })

    # Exportar para CSV
    df.to_csv(r'C:\Users\drdc\Downloads\codigos_fornecedor.txt', index=False)
    print("Resultados exportados para 'codigos_fornecedor.txt'")

# Exemplo de uso
diretorio_fixo = r"D:\\"
tamanho_imagem_fixo = (1000, 1000)  # Exemplo de tamanho fixo da imagem (largura, altura)
tamanho_circulo_fixo = 59  # Exemplo de tamanho fixo do círculo

processar_imagens(diretorio_fixo, "#969696", tamanho_imagem_fixo, tamanho_circulo_fixo)  # Hexadecimal da cor cinza
