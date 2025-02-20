from PIL import Image
import imagehash  
import os

def comparar_hashes(hash1, hash2):
    return str(hash1) == str(hash2)

def encontrar_imagem_igual(caminho_pasta, nomes_imagens, hash_exemplo):
    imagens_localizadas = []  
    imagens_aguardando_imagem = []  
    imagens_nao_encontradas = []  

    for nome_imagem in nomes_imagens:
        caminho_arquivo = os.path.join(caminho_pasta, f'{nome_imagem}.jpg')

        if os.path.isfile(caminho_arquivo):
            with Image.open(caminho_arquivo) as imagem:
                hash_imagem = imagehash.average_hash(imagem)
                print(f'Hash da imagem {nome_imagem}: {hash_imagem}')

            if comparar_hashes(hash_exemplo, hash_imagem):
                imagens_aguardando_imagem.append(nome_imagem)
                print(f'Imagem aguardando: {nome_imagem}')
            else:
                imagens_localizadas.append(nome_imagem)
                print(f'Imagem localizada: {nome_imagem}')
        else:
            imagens_nao_encontradas.append(nome_imagem)
            print(f'Imagem não encontrada: {nome_imagem}')

    return imagens_localizadas, imagens_aguardando_imagem, imagens_nao_encontradas

caminho_pasta = r'\\fas01wap\EntregaFA-DA\\'  # Caminho para a pasta das imagens

# Lista de códigos de imagens que você quer procurar

nomes_imagens = [
  '69440',
    '96020002',
   ]

with Image.open(r'G:\Meu Drive\# DAYVSON COSTA\AREA DE TRABALHO - PC MARKETING\43878001.jpg') as imagem_exemplo:
    hash_exemplo = imagehash.average_hash(imagem_exemplo)
    print(f'Hash da imagem exemplo: {hash_exemplo}')

imagens_localizadas, imagens_aguardando_imagem, imagens_nao_encontradas = encontrar_imagem_igual(caminho_pasta, nomes_imagens, hash_exemplo)

total_imagens = len(nomes_imagens)
total_localizadas = len(imagens_localizadas)
total_aguardando_imagem = len(imagens_aguardando_imagem)
total_nao_encontradas = len(imagens_nao_encontradas)

resultado = f'Códigos Localizados: {", ".join(imagens_localizadas)}\n'
resultado += f'Códigos Não Localizados: {", ".join(imagens_nao_encontradas)}\n'
resultado += f'Códigos Aguardando Imagem: {", ".join(imagens_aguardando_imagem)}\n'

resultado += f'Quant. de Códigos Procurados: {total_imagens}\n'
resultado += f'Quant. de Códigos Localizados: {total_localizadas}\n'
resultado += f'Quant. de Códigos Não Localizados: {total_nao_encontradas}\n'
resultado += f'Quant. de Códigos Aguardando Imagem: {total_aguardando_imagem}\n'

print(resultado)

# Abra um arquivo txt no modo de escrita ('w')
with open(r'C:\Users\drdc\Downloads\codigos_aguardando_imagem.txt', 'w') as arquivo:
    # Escreva o conteúdo da variável 'resultado' no arquivo
    arquivo.write(resultado)

print("Resultado exportado!")