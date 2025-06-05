import os
from barcode import EAN13
from barcode.writer import ImageWriter

# Lista de códigos de barras (12 dígitos para EAN-13)
codigos_barras = ["123456789012", "987654321098", "112233445566"]

# Defina o caminho da pasta onde deseja salvar as imagens
pasta_salvar = r"D:\Download"

# Verificar se a pasta existe, caso contrário, criar
if not os.path.exists(pasta_salvar):
    os.makedirs(pasta_salvar)

# Gerar e salvar os códigos de barras
for codigo in codigos_barras:
    try:
        # Criar o código de barras
        barcode = EAN13(codigo, writer=ImageWriter())
        
        # Caminho completo para salvar a imagem
        arquivo_path = os.path.join(pasta_salvar, f"barcode_{codigo}.png")
        
        # Salvar o código de barras como imagem
        barcode.save(arquivo_path)
        print(f"Código de barras {codigo} salvo em {arquivo_path}")
    except Exception as e:
        print(f"Erro ao gerar o código {codigo}: {e}")

print("Processo concluído!")