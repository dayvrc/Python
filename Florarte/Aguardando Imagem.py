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

caminho_pasta = r'R:\\'  # Caminho para a pasta das imagens
#caminho_pasta = r'G:\.shortcut-targets-by-id\1-3XgYQ4XYUPIPVphK-DQPv4MYWJZ62vR\Imagens\\'  # Caminho para a pasta das imagens

# Lista de códigos de imagens que você quer procurar
 
#CODIGOS ATUALIZADOS 17/09/2025
nomes_imagens = [
    '84102001',
    '83338001',
    '83287001',
    '84762001',
    '85414006',
    '84679001',
    '84708001',
    '84711001',
    '84298001',
    '48400004',
    '68564',
    '68565',
    '68566',
    '68567',
    '68569',
    '68575',
    '68576',
    '84305001',
    '68683',
    '68684',
    '68685',
    '68686',
    '68687',
    '68688',
    '68689',
    '84307001',
    '56151001',
    '70027',
    '72596001',
    '79956001',
    '84313001',
    '84321001',
    '84322001',
    '84324001',
    '78106001',
    '87692001',
    '89810001',
    '85285001',
    '85070001',
    '42376001',
    '42376002',
    '42432001',
    '43958001',
    '49281001',
    '49530001',
    '69204001',
    '84598001',
    '89014001',
    '87585001',
    '89019001',
    '89023001',
    '89024001',
    '95055001',
    '95057001',
    '95058001',
    '89606002',
    '90420002',
    '95059001',
    '95059002',
    '95059003',
    '95060001',
    '95061001',
    '95062001',
    '95377001',
    '95382001',
    '95382002',
    '95382003',
    '95384001',
    '95384002',
    '95386001',
    '42172009',
    '85585001',
    '88285002',
    '96479001',
    '96480001',
    '89810002',
    '89810004',
    '34206001',
    '68590',
    '85414005',
    '89810003',

   ]

with Image.open(r'D:\56158.jpg') as imagem_exemplo:
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